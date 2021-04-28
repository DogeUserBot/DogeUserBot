# Copyright © 2021 Doge UserBot in Telegram App
# All rights reserved.
#
# Licensed under the Doge UserBot Public License;
# you may not use this file except in compliance with the License.
#
# @MUTLCC | @SanalMafya
#

""" Telegram'daki profil detaylarınızı değişmeye yarayan UserBot modülüdür. """

import os
import logging
import time

from telethon.errors import ImageProcessFailedError, PhotoCropSizeSmallError
from telethon.errors.rpcerrorlist import (PhotoExtInvalidError,
                                          UsernameOccupiedError)
from telethon.tl.functions.account import (UpdateProfileRequest,
                                           UpdateUsernameRequest)
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest
from telethon.tl.functions.photos import (DeletePhotosRequest,
                                          GetUserPhotosRequest,
                                          UploadProfilePhotoRequest)
from telethon.tl.types import InputPhoto, MessageMediaPhoto, User, Chat, Channel
from telethon.events import NewMessage
from telethon.tl.custom import Dialog

from userbot import bot, CMD_HELP
from userbot.events import register
from userbot.cmdhelp import CmdHelp

# ====================== CONSTANT ===============================
# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("profile")

# ████████████████████████████████ #

INVALID_MEDIA = LANG['INVALID_MEDIA']
PP_CHANGED = LANG['PP_CHANGED']
PP_TOO_SMOL = LANG['PP_TOO_SMOL']
PP_ERROR = LANG['PP_ERROR']

BIO_SUCCESS = LANG['BIO_SUCCESS']

NAME_OK = LANG['NAME_OK']
USERNAME_SUCCESS = LANG['USERNAME_SUCCESS']
USERNAME_TAKEN = LANG['USERNAME_TAKEN']

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
logger = logging.getLogger(__name__)

def make_mention(user):
    if user.username:
        return f"@{user.username}"
    else:
        return inline_mention(user)


def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"[{full_name}](tg://user?id={user.id})"


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    full_name = ' '.join(names)
    return full_name

# ===============================================================


@register(outgoing=True, pattern="^.reserved$")
async def mine(event):
    """ .reserved komutu ayırdığınız kullanıcı adlarını listeler. """
    result = await bot(GetAdminedPublicChannelsRequest())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f"{channel_obj.title}\n@{channel_obj.username}\n\n"
    await event.edit(output_str)


@register(outgoing=True, pattern="^.name")
async def update_name(name):
    """ .name komutu Telegram'daki isminizi değişir. """
    newname = name.text[6:]
    if " " not in newname:
        firstname = newname
        lastname = ""
    else:
        namesplit = newname.split(" ", 1)
        firstname = namesplit[0]
        lastname = namesplit[1]

    await name.client(
        UpdateProfileRequest(first_name=firstname, last_name=lastname))
    await name.edit(NAME_OK)


@register(outgoing=True, pattern="^.setpfp$")
async def set_profilepic(propic):
    """ .profilepic komutu Telegram'daki profil resminizi yanıtladığınız resimle değişir. """
    replymsg = await propic.get_reply_message()
    photo = None
    if replymsg.media:
        if isinstance(replymsg.media, MessageMediaPhoto):
            photo = await propic.client.download_media(message=replymsg.photo)
        elif "image" in replymsg.media.document.mime_type.split('/'):
            photo = await propic.client.download_file(replymsg.media.document)
        else:
            await propic.edit(INVALID_MEDIA)

    if photo:
        try:
            await propic.client(
                UploadProfilePhotoRequest(await
                                          propic.client.upload_file(photo)))
            os.remove(photo)
            await propic.edit(PP_CHANGED)
        except PhotoCropSizeSmallError:
            await propic.edit(PP_TOO_SMOL)
        except ImageProcessFailedError:
            await propic.edit(PP_ERROR)
        except PhotoExtInvalidError:
            await propic.edit(INVALID_MEDIA)


@register(outgoing=True, pattern="^.setbio (.*)")
async def set_biograph(setbio):
    """ .setbio komutu Telegram'da yeni bir biyografi ayarlamanızı sağlar. """
    newbio = setbio.pattern_match.group(1)
    await setbio.client(UpdateProfileRequest(about=newbio))
    await setbio.edit(BIO_SUCCESS)


@register(outgoing=True, pattern="^.username (.*)")
async def update_username(username):
    """ .username komutu Telegram'da yeni bir kullanıcı adı belirlemenizi sağlar. """
    newusername = username.pattern_match.group(1)
    try:
        await username.client(UpdateUsernameRequest(newusername))
        await username.edit(USERNAME_SUCCESS)
    except UsernameOccupiedError:
        await username.edit(USERNAME_TAKEN)


@register(outgoing=True, pattern=r"^.count(?: |$)(.*)")
@register(outgoing=True, pattern=r"^.bilgi(?: |$)(.*)")
async def count(event: NewMessage.Event) -> None:  # pylint: disable = R0912, R0914, R0915
    """Istatistikler için bir komut"""
    waiting_message = await event.edit('**🐶 Hesabınızın bilgilerini analiz ediyorum...**')
    start_time = time.time()
    private_chats = 0
    bots = 0
    groups = 0
    broadcast_channels = 0
    admin_in_groups = 0
    creator_in_groups = 0
    admin_in_broadcast_channels = 0
    creator_in_channels = 0
    unread_mentions = 0
    unread = 0
    largest_group_member_count = 0
    largest_group_with_admin = 0
    dialog: Dialog
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity

        if isinstance(entity, Channel):
            # participants_count = (await event.get_participants(dialog, limit=0)).total
            if entity.broadcast:
                broadcast_channels += 1
                if entity.creator or entity.admin_rights:
                    admin_in_broadcast_channels += 1
                if entity.creator:
                    creator_in_channels += 1

            elif entity.megagroup:
                groups += 1
                # if participants_count > largest_group_member_count:
                #     largest_group_member_count = participants_count
                if entity.creator or entity.admin_rights:
                    # if participants_count > largest_group_with_admin:
                    #     largest_group_with_admin = participants_count
                    admin_in_groups += 1
                if entity.creator:
                    creator_in_groups += 1

        elif isinstance(entity, User):
            private_chats += 1
            if entity.bot:
                bots += 1

        elif isinstance(entity, Chat):
            groups += 1
            if entity.creator or entity.admin_rights:
                admin_in_groups += 1
            if entity.creator:
                creator_in_groups += 1

        unread_mentions += dialog.unread_mentions_count
        unread += dialog.unread_count
    stop_time = time.time() - start_time

    full_name = inline_mention(await event.client.get_me())
    response = f'**🐶 {full_name} HESAP İSTATİSTİKLERİNİZ**\n\n'
    response += f'**👤 Mesajlaştığınız hesapların sayısı: **`{private_chats}`\n'
    response += f'**ㅤㅤ📊 Kişiler: ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ  **`{private_chats - bots}`\n'
    response += f'**ㅤㅤ📊 Botlar: ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ **`{bots}`\n\n'
    response += f'**👥 Katıldığınız gruplar: ㅤㅤㅤㅤㅤ     **`{groups}`\n\n'
    response += f'**📣 Katıldığınız kanallar: ㅤㅤㅤㅤㅤ   **`{broadcast_channels}`\n\n'
    response += f'**👮 Yönetici olduğunuz gruplar: ㅤㅤ  **`{admin_in_groups}`\n'
    response += f'**ㅤㅤ📊 Oluşturduğunuz gruplar:ㅤㅤ**`{creator_in_groups}`\n'
    response += f'**ㅤㅤ📊 Yönetici olduğunuz gruplar:   **`{admin_in_groups - creator_in_groups}`\n\n'
    response += f'**👮 Yönetici olduğunuz kanallar: ㅤㅤ**`{admin_in_broadcast_channels}`\n'
    response += f'**ㅤㅤ📊 Kurucu olduğunuz kanallar:   **`{creator_in_channels}`\n'
    response += f'**ㅤㅤ📊 Yönetici olduğunuz kanallar: **`{admin_in_broadcast_channels - creator_in_channels}`\n\n'
    response += f'**✉️ Okunmamış mesajlarınız: ㅤㅤㅤ  **`{unread}`\n\n'
    response += f'**📧 Okunmamış etiketli mesajlarınız: **`{unread_mentions}`\n\n'
    response += f'**⏱ {stop_time:.02f}** saniyede istatistiklerinizi hesapladım.\n'

    await event.edit(response)


@register(outgoing=True, pattern=r"^.delpfp")
async def remove_profilepic(delpfp):
    """ .delpfp komutu Telegram'daki şu anki profil resminizi kaldırır. """
    group = delpfp.text[8:]
    if group == 'all':
        lim = 0
    elif group.isdigit():
        lim = int(group)
    else:
        lim = 1

    pfplist = await delpfp.client(
        GetUserPhotosRequest(user_id=delpfp.from_id,
                             offset=0,
                             max_id=0,
                             limit=lim))
    input_photos = []
    for sep in pfplist.photos:
        input_photos.append(
            InputPhoto(id=sep.id,
                       access_hash=sep.access_hash,
                       file_reference=sep.file_reference))
    await delpfp.client(DeletePhotosRequest(id=input_photos))
    await delpfp.edit(
        LANG['DELPFP'] % len(input_photos))


CmdHelp('profile').add_command(
    'username', '<yeni kullanıcı adı>', 'Telegram\'daki kullanıcı adınızı değişir.'
).add_command(
    'name', '<isim> or .name <isim> <soyisim>', 'Telegram\'daki isminizi değişir. (Ad ve soyad ilk boşluğa dayanarak birleştirilir.)'
).add_command(
    'setpfp', None, 'Bir resmi Telegram\'da profil resmi yapmak için .setpfp komutuyla cevap verin.'
).add_command(
    'setbio', '<yeni biyografi>', 'Telegram\'daki biyografinizi bu komutu kullanarak değiştirin.'
).add_command(
    'delpfp', '<numara/all>', 'Telegram profil fotoğrafınızı kaldırır.'
).add_command(
    'reserved', None, 'Rezerve ettiğiniz kullanıcı adlarını gösterir.'
).add_command(
    'count', None, 'Gruplarınızı, sohbetlerinizi, aktif botları vs. sayar.'
).add()

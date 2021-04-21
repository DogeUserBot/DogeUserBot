# Copyright © 2021 Doge UserBot in Telegram App
# All rights reserved.
#
# Licensed under the Doge UserBot Public License;
# you may not use this file except in compliance with the License.
#
# @MUTLCC | @SanalMafya
#

from telethon.tl.types import ChannelParticipantsAdmins
from userbot import CMD_HELP, bot
from userbot.events import register
from userbot.cmdhelp import CmdHelp

@register(outgoing=True, pattern="^.all (.*)")
async def all (event):
    if event.fwd_from:
        return
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    input_str = event.pattern_match.group(1)
    if not input_str:
        return await event.edit("❓ Nasıl yapılır?\n🔔 `.all Buraya gelin!`.")

    mentions = input_str
    chat = await event.get_input_chat()
    async for x in event.client.iter_participants(chat, 100):
        mentions += f"[\u2063](tg://user?id={x.id})"
    await reply_to_id.reply(mentions)
    await event.delete()

@register(outgoing=True, pattern="^.tagall$")
async def _(event):
    if event.fwd_from:
        return
    mentions = "@tag"
    chat = await event.get_input_chat()
    leng = 0
    async for x in bot.iter_participants(chat):
        if leng < 4092:
            mentions += f"[\u2063](tg://user?id={x.id})"
            leng += 1
    await event.reply(mentions)
    await event.delete()

@register(outgoing=True, pattern="^.admin")
async def _(event):
    if event.fwd_from:
        return
    mentions = "@admin"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f"[\u2063](tg://user?id={x.id})"
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()

CmdHelp('tagall').add_command(
    'tagall', None, 'Bu komutu kullandığınızda sohbet içerisinde ki herkesi etiketler.'
).add_command(
    'admin', None, 'Bu komutu kullandığınızda sohbet içerisinde ki yöneticileri etiketler.'
).add_command(
    'all', '<mesaj>', '🔔 Bu komutu kullandığınızda sohbet içerisindeki herkesi etiketler.', 'all Buraya gelin!'
).add_info('**👤 @DogeUserBot tarafından 💚 ile yapıldı!**').add()
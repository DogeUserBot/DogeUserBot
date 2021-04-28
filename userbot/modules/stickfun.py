# Copyright © 2021 Doge UserBot in Telegram App
# All rights reserved.
#
# Licensed under the Doge UserBot Public License;
# you may not use this file except in compliance with the License.
#
# @MUTLCC | @SanalMafya
#

import random
import re
from io import BytesIO
from os import remove
from requests import get
from asyncio import sleep
from textwrap import wrap
from PIL import Image, ImageChops, ImageDraw, ImageFont
from telethon.tl.types import InputMessagesFilterDocument
from userbot.events import register 
from userbot import CMD_HELP, bot
from userbot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value

# ████████████████████████████████


EMOJI_PATTERN = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats
    "]+"
)


def deEmojify(inputString: str) -> str:
    return re.sub(EMOJI_PATTERN, "", inputString)


@register(outgoing=True, pattern="^\.[wW][sS][cC](?: |$)(.*)")
async def waifu(animu):
    text = animu.pattern_match.group(1)
    if not text:
        if animu.is_reply:
            text = (await animu.get_reply_message()).message
        else:
            await animu.answer("**🐾 Bana bir metin ver!**")
            return
    animus = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        30,
        31,
        32,
        33,
        34,
        35,
        36,
        37,
        38,
        39,
        40,
        41,
        42,
        43,
        44,
        45,
        46,
        47,
        48,
        49,
        50,
        51,
        52,
        53,
        54,
        55,
        56,
        57,
        58,
        59,
        60,
        61,
        62,
        63,
    ]
    sticcers = await bot.inline_query(
        "stickerizerbot", f"#{random.choice(animus)}{(deEmojify(text))}"
    )
    try:
        await sticcers[0].click(
            animu.chat_id,
            reply_to=animu.reply_to_msg_id,
            silent=True if animu.is_reply else False,
            hide_via=True,
        )
    except Exception:
        return await animu.edit(
            "**😟 Sanırım burada satır içi botlara izin verilmiyor.\n\n🐾 Bu yüzden Waifu çıkartmaları gönderemeyeceğim.**"
        )
    await sleep(1)
    await animu.delete()


@register(outgoing=True, pattern="^.[aA][sS][cC](?: |$)(.*)")
async def amogus(event):
    sticktext = event.pattern_match.group(1).strip()

    if len(sticktext) < 1:
        await event.edit(f"**ඞ Bana bir metin ver!**")
        return

    arr = random.randint(1, 12)
    fontsize = 110
    FONT_FILE = await get_font_file(event.client, "@DogeFonts")
    url = 'https://raw.githubusercontent.com/DOGEUSERBOT/DogeUserBot/tree/master/userbot/resources/amongus_sticker/'
    font = ImageFont.truetype(FONT_FILE, size=fontsize)

    imposter = Image.open(BytesIO(get(f'{url}{arr}.png').content))
    stick_text = '\n'.join(['\n'.join(wrap(part, 30)) for part in sticktext.split('\n')])
    w, h = ImageDraw.Draw(Image.new('RGB', (1, 1))).multiline_textsize(
        stick_text, font, stroke_width=2
    )
    text = Image.new('RGBA', (w + 40, h + 40))
    ImageDraw.Draw(text).multiline_text(
        (15, 15), stick_text, '#FFF', font, stroke_width=2, stroke_fill='#000'
    )
    w = imposter.width + text.width + 30
    h = max(imposter.height, text.height)
    image = Image.new('RGBA', (w, h))
    image.paste(imposter, (0, h - imposter.height), imposter)
    image.paste(text, (w - text.width, 0), text)
    image.thumbnail((512, 512))

    output = BytesIO()
    output.name = 'sus.webp'
    image.save(output, 'WebP')
    output.seek(0)

    await event.client.send_file(event.chat_id, output, reply_to=event.message.reply_to_msg_id)
    try:
        remove(FONT_FILE)
    except:
        pass

@register(outgoing=True, pattern="^.[dD][sS][cC](?: |$)(.*)")
async def amogus(event):
    sticktext = event.pattern_match.group(1).strip()

    if len(sticktext) < 1:
        await event.edit(f"**🐶 Bana bir metin ver!**")
        return

    arr = random.randint(1, 15)
    fontsize = 110
    FONT_FILE = await get_font_file(event.client, "@DogeFonts")
    url = 'https://raw.githubusercontent.com/DOGEUSERBOT/DogeUserBot/tree/master/userbot/resources/doge_sticker/'
    font = ImageFont.truetype(FONT_FILE, size=fontsize)

    doge = Image.open(BytesIO(get(f'{url}{arr}.png').content))
    stick_text = '\n'.join(['\n'.join(wrap(part, 30)) for part in sticktext.split('\n')])
    w, h = ImageDraw.Draw(Image.new('RGB', (1, 1))).multiline_textsize(
        stick_text, font, stroke_width=2
    )
    text = Image.new('RGBA', (w + 40, h + 40))
    ImageDraw.Draw(text).multiline_text(
        (15, 15), stick_text, '#FFF', font, stroke_width=2, stroke_fill='#000'
    )
    w = doge.width + text.width + 30
    h = max(doge.height, text.height)
    image = Image.new('RGBA', (w, h))
    image.paste(doge, (0, h - doge.height), doge)
    image.paste(text, (w - text.width, 0), text)
    image.thumbnail((512, 512))

    output = BytesIO()
    output.name = 'hav.webp'
    image.save(output, 'WebP')
    output.seek(0)

    await event.client.send_file(event.chat_id, output, reply_to=event.message.reply_to_msg_id)
    try:
        remove(FONT_FILE)
    except:
        pass


@register(outgoing=True, pattern="^.[rR][gG][bB](?: |$)(.*)")
async def sticklet(event):
    R = random.randint(0,256)
    G = random.randint(0,256)
    B = random.randint(0,256)

    # Giriş metnini al
    sticktext = event.pattern_match.group(1).strip()

    if len(sticktext) < 1:
        await event.edit(f"**🌈 Bana bir metin ver!**")
        return

    # https://docs.python.org/3/library/textwrap.html#textwrap.wrap
    sticktext = wrap(sticktext, width=10)
    # Listeyi bir dizeye dönüştür
    sticktext = '\n'.join(sticktext)

    image = Image.new("RGBA", (512, 512), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    fontsize = 230

    FONT_FILE = await get_font_file(event.client, "@DogeFonts")

    font = ImageFont.truetype(FONT_FILE, size=fontsize)

    while draw.multiline_textsize(sticktext, font=font) > (512, 512):
        fontsize -= 10
        font = ImageFont.truetype(FONT_FILE, size=fontsize)

    width, height = draw.multiline_textsize(sticktext, font=font)
    draw.multiline_text(((512-width)/2,(512-height)/2), sticktext, font=font, fill=(R, G, B))

    image_stream = BytesIO()
    image_stream.name = "@rgb.webp"

    def trim(im):
        bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
        diff = ImageChops.difference(im, bg)
        diff = ImageChops.add(diff, diff, 2.0, -100)
        bbox = diff.getbbox()
        return im.crop(bbox) if bbox else im

    image = trim(image)
    image.save(image_stream, "WebP")
    image_stream.seek(0)

    # mesajı sil
    await event.delete()

    await event.client.send_file(event.chat_id, image_stream, reply_to=event.message.reply_to_msg_id)
    # Temizlik
    try:
        remove(FONT_FILE)
    except:
        pass


async def get_font_file(client, channel_id):
    font_file_message_s = await client.get_messages(
        entity=channel_id,
        filter=InputMessagesFilterDocument,
        # Bu işlem çok fazla kullanıldığında
        # FLOOD_WAIT'e neden olabilir
        limit=None
    )
    font_file_message = random.choice(font_file_message_s)
    return await client.download_media(font_file_message)


CmdHelp('stickfun').add_command(
    'wsc', '<metin>', 'Metninizi Waifu anime çıkartmalarına dönüştürür.', 'wsc Naber?'
).add_command(
    'asc', '<metin>', 'Metninizi Among Us çıkartmalarına dönüştürür.', 'asc İyiyim, sen?'
).add_command(
    'dsc', '<metin>', 'Metninizi Doge çıkartmalarına dönüştürür.', 'dsc Ben de iyiyim.'
).add_command(
    'rgb', '<metin>', 'Metninizi rastgele bir renkte çıkartmaya dönüştürür.', 'rgb Hep iyi ol!'
).add()
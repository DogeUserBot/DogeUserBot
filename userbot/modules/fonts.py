# Copyright © 2021 Doge UserBot in Telegram App
# All rights reserved.
#
# Licensed under the Doge UserBot Public License;
# you may not use this file except in compliance with the License.
#
# @MUTLCC | @SanalMafya
#

from userbot.cmdhelp import CmdHelp
from userbot.events import register

normiefont = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
f1font = [
    "卂",
    "乃",
    "匚",
    "刀",
    "乇",
    "下",
    "厶",
    "卄",
    "工",
    "丁",
    "长",
    "乚",
    "从",
    "𠘨",
    "口",
    "尸",
    "㔿",
    "尺",
    "丂",
    "丅",
    "凵",
    "リ",
    "山",
    "乂",
    "丫",
    "乙",
]
f2font = [
    "🅐",
    "🅑",
    "🅒",
    "🅓",
    "🅔",
    "🅕",
    "🅖",
    "🅗",
    "🅘",
    "🅙",
    "🅚",
    "🅛",
    "🅜",
    "🅝",
    "🅞",
    "🅟",
    "🅠",
    "🅡",
    "🅢",
    "🅣",
    "🅤",
    "🅥",
    "🅦",
    "🅧",
    "🅨",
    "🅩",
]
f3font = [
    "𝔄",
    "𝔅",
    "ℭ",
    "𝔇",
    "𝔈",
    "𝔉",
    "𝔊",
    "ℌ",
    "ℑ",
    "𝔍",
    "𝔎",
    "𝔏",
    "𝔐",
    "𝔑",
    "𝔒",
    "𝔓",
    "𝔔",
    "ℜ",
    "𝔖",
    "𝔗",
    "𝔘",
    "𝔙",
    "𝔚",
    "𝔛",
    "𝔜",
    "ℨ",
]
f4font = [
    "ⲁ",
    "ⲃ",
    "ⲥ",
    "ⲇ",
    "ⲉ",
    "ϝ",
    "ⳋ",
    "ⲏ",
    "ⲓ",
    "ⳗ",
    "ⲕ",
    "ⳑ",
    "ⲙ",
    "ⲛ",
    "ⲟ",
    "ⲣ",
    "q",
    "ʀ",
    "ⲋ",
    "ⲧ",
    "υ",
    "ⳳ",
    "ⲱ",
    "ⲭ",
    "ⲩ",
    "ⲍ",
]
f5font = [
    "🄰",
    "🄱",
    "🄲",
    "🄳",
    "🄴",
    "🄵",
    "🄶",
    "🄷",
    "🄸",
    "🄹",
    "🄺",
    "🄻",
    "🄼",
    "🄽",
    "🄾",
    "🄿",
    "🅀",
    "🅁",
    "🅂",
    "🅃",
    "🅄",
    "🅅",
    "🅆",
    "🅇",
    "🅈",
    "🅉",
]
f6font = [
    "ᵃ",
    "ᵇ",
    "ᶜ",
    "ᵈ",
    "ᵉ",
    "ᶠ",
    "ᵍ",
    "ʰ",
    "ᶦ",
    "ʲ",
    "ᵏ",
    "ᶫ",
    "ᵐ",
    "ᶰ",
    "ᵒ",
    "ᵖ",
    "ᶞ",
    "ʳ",
    "ˢ",
    "ᵗ",
    "ᵘ",
    "ᵛ",
    "ʷ",
    "ˣ",
    "ʸ",
    "ᶻ",
]
f7font = [
    "ᴀ",
    "ʙ",
    "ᴄ",
    "ᴅ",
    "ᴇ",
    "ғ",
    "ɢ",
    "ʜ",
    "ɪ",
    "ᴊ",
    "ᴋ",
    "ʟ",
    "ᴍ",
    "ɴ",
    "ᴏ",
    "ᴘ",
    "ǫ",
    "ʀ",
    "s",
    "ᴛ",
    "ᴜ",
    "ᴠ",
    "ᴡ",
    "x",
    "ʏ",
    "ᴢ",
]
f8font = [
    "𝐀",
    "𝐁",
    "𝐂",
    "𝐃",
    "𝐄",
    "𝐅",
    "𝐆",
    "𝐇",
    "𝐈",
    "𝐉",
    "𝐊",
    "𝐋",
    "𝐌",
    "𝐍",
    "𝐎",
    "𝐏",
    "𝐐",
    "𝐑",
    "𝐒",
    "𝐓",
    "𝐔",
    "𝐕",
    "𝐖",
    "𝐗",
    "𝐘",
    "𝐙",
]
f9font = [
   "𝓐",
    "𝓑",
    "𝓒",
    "𝓓",
    "𝓔",
    "𝓕",
    "𝓖",
    "𝓗",
    "𝓘",
    "𝓙",
    "𝓚",
    "𝓛",
    "𝓜",
    "𝓝",
    "𝓞",
    "𝓟",
    "𝓠",
    "𝓡",
    "𝓢",
    "𝓣",
    "𝓤",
    "𝓥",
    "𝓦",
    "𝓧",
    "𝓨",
    "𝓩",
]
f10font = [
   "𝘼",
    "𝘽",
    "𝘾",
    "𝘿",
    "𝙀",
    "𝙁",
    "𝙂",
    "𝙃",
    "𝙄",
    "𝙅",
    "𝙆",
    "𝙇",
    "𝙈",
    "𝙉",
    "𝙊",
    "𝙋",
    "𝙌",
    "𝙍",
    "𝙎",
    "𝙏",
    "𝙐",
    "𝙑",
    "𝙒",
    "𝙓",
    "𝙔",
    "𝙕",
]
f11font = [
    "𝙰",
    "𝙱",
    "𝙲",
    "𝙳",
    "𝙴",
    "𝙵",
    "𝙶",
    "𝙷",
    "𝙸",
    "𝙹",
    "𝙺",
    "𝙻",
    "𝙼",
    "𝙽",
    "𝙾",
    "𝙿",
    "𝚀",
    "𝚁",
    "𝚂",
    "𝚃",
    "𝚄",
    "𝚅",
    "𝚆",
    "𝚇",
    "𝚈",
    "𝚉",
]
f12font = [
    "ꋬ",
    "ꃳ",
    "ꉔ",
    "꒯",
    "ꏂ",
    "ꊰ",
    "ꍌ",
    "ꁝ",
    "꒐",
    "꒻",
    "ꀘ",
    "꒒",
    "ꂵ",
    "ꋊ",
    "ꄲ",
    "ꉣ",
    "ꆰ",
    "ꋪ",
    "ꇙ",
    "꓄",
    "꒤",
    "꒦",
    "ꅐ",
    "ꉧ",
    "ꌦ",
    "ꁴ",
]
f13font = [
    "𝔸",
    "𝔹",
    "ℂ",
    "𝔻",
    "𝔼",
    "𝔽",
    "𝔾",
    "ℍ",
    "𝕀",
    "𝕁",
    "𝕂",
    "𝕃",
    "𝕄",
    "ℕ",
    "𝕆",
    "ℙ",
    "ℚ",
    "ℝ",
    "𝕊",
    "𝕋",
    "𝕌",
    "𝕍",
    "𝕎",
    "𝕏",
    "𝕐",
    "ℤ",
]


@register(outgoing=True, pattern="^.[Ff]1(?: |$)(.*)")
async def fonta(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`Hey, metni çeviremiyorum. Bir mesaja yanıt olarak kullanın`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            f1character = f1font[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, f1character)
    await event.edit(string)


@register(outgoing=True, pattern="^.[Ff]2(?: |$)(.*)")
async def fontb(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`Hey, metni çeviremiyorum. Bir mesaja yanıt olarak kullanın`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            f2character = f2font[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, f2character)
    await event.edit(string)


@register(outgoing=True, pattern="^.[Ff]3(?: |$)(.*)")
async def fontc(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`Hey, metni çeviremiyorum. Bir mesaja yanıt olarak kullanın`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            f3character = f3font[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, f3character)
    await event.edit(string)
    
    
@register(outgoing=True, pattern="^.[Ff]4(?: |$)(.*)")
async def fontd(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`Hey, metni çeviremiyorum. Bir mesaja yanıt olarak kullanın`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            f4character = f4font[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, f4character)
    await event.edit(string)
    
    
@register(outgoing=True, pattern="^.[Ff]5(?: |$)(.*)")
async def fonte(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`Hey, metni çeviremiyorum. Bir mesaja yanıt olarak kullanın`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            f5character = f5font[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, f5character)
    await event.edit(string)


@register(outgoing=True, pattern="^.[Ff]6(?: |$)(.*)")
async def fontf(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`Hey, metni çeviremiyorum. Bir mesaja yanıt olarak kullanın`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            f6character = f6font[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, f6character)
    await event.edit(string)


@register(outgoing=True, pattern="^.[Ff]7(?: |$)(.*)")
async def fontg(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`Hey, metni çeviremiyorum. Bir mesaja yanıt olarak kullanın`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            f7character = f7font[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, f7character)
    await event.edit(string)

@register(outgoing=True, pattern="^.[Ff]8(?: |$)(.*)")
async def fonth(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`Hey, metni çeviremiyorum. Bir mesaja yanıt olarak kullanın`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            f8character = f8font[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, f8character)
    await event.edit(string)


@register(outgoing=True, pattern="^.[Ff]9(?: |$)(.*)")
async def fonti(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`Hey, metni çeviremiyorum. Bir mesaja yanıt olarak kullanın`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            f9character = f9font[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, f9character)
    await event.edit(string)


@register(outgoing=True, pattern="^.[Ff]10(?: |$)(.*)")
async def fontj(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`Hey, metni çeviremiyorum. Bir mesaja yanıt olarak kullanın`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            f10character = f10font[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, f10character)
    await event.edit(string)


@register(outgoing=True, pattern="^.[Ff]11(?: |$)(.*)")
async def fontl(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`Hey, metni çeviremiyorum. Bir mesaja yanıt olarak kullanın`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            f11character = f11font[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, f11character)
    await event.edit(string)


@register(outgoing=True, pattern="^.[Ff]12(?: |$)(.*)")
async def fontq(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`Hey, metni çeviremiyorum. Bir mesaja yanıt olarak kullanın`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            f12character = f12font[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, f12character)
    await event.edit(string)



@register(outgoing=True, pattern="^.[Ff]13(?: |$)(.*)")
async def fontz(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`Hey, metni çeviremiyorum. Bir mesaja yanıt olarak kullanın`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            f13character = f13font[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, f13character)
    await event.edit(string)



CmdHelp('fonts').add_command(
    'f1', '<metin>', '千ㄖ几ㄒ'
).add_command(
    'f2', '<metin>', '🅕🅞🅝🅣'
).add_command(
    'f3', '<metin>', '𝔉𝔒𝔑𝔗'
).add_command(
    'f4', '<metin>', 'ϝⲟⲛⲧ'
).add_command(
    'f5', '<metin>', '🄵🄾🄽🅃'
).add_command(
    'f6', '<metin>', 'ᶠᵒᶰᵗ'
).add_command(
    'f7', '<metin>', 'ғᴏɴᴛ'
).add_command(
    'f8', '<metin>', '𝐅𝐎𝐍𝐓'
).add_command(
    'f9', '<metin>', '𝓕𝓞𝓝𝓣'
).add_command(
    'f10', '<metin>', '𝙁𝙊𝙉𝙏'
).add_command(
    'f11', '<metin>', '𝙵𝙾𝙽𝚃'
).add_command(
    'f12', '<metin>', 'ꊰꄲꋊ꓄'
).add_command(
    'f13', '<metin>', '𝔽𝕆ℕ𝕋'
).add()

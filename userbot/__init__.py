# Copyright © 2021 Doge UserBot in Telegram App
# All rights reserved.
#
# Licensed under the Doge UserBot Public License;
# you may not use this file except in compliance with the License.
#
# @MUTLCC | @SanalMafya
#

import os
from re import compile
from sys import version_info
from logging import basicConfig, getLogger, INFO, DEBUG
from distutils.util import strtobool as sb
from pylast import LastFMNetwork, md5
from pySmartDL import SmartDL
from dotenv import load_dotenv
from sqlite3 import connect
from requests import get
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.sync import TelegramClient, custom
from telethon.sessions import StringSession
from telethon.events import callbackquery, InlineQuery, NewMessage
from math import ceil

load_dotenv("config.env")

# Bot günlükleri kurulumu:
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

ASYNC_POOL = []

if CONSOLE_LOGGER_VERBOSE:
    basicConfig(
        format="%(asctime)s - @DogeUserBot - %(levelname)s - %(message)s",
        level=DEBUG,
    )
else:
    basicConfig(format="%(asctime)s - @DogeUserBot - %(levelname)s - %(message)s",
                level=INFO)
LOGS = getLogger(__name__)

if version_info[0] < 3 or version_info[1] < 6:
    LOGS.info("En az python 3.6 sürümüne sahip olmanız gerekir."
              "Birden fazla özellik buna bağlıdır. Bu yüzden bot kapatılıyor.")
    quit(1)

# Yapılandırmanın önceden kullanılan değişkeni kullanarak düzenlenip düzenlenmediğini kontrol edin.
# Temel olarak, yapılandırma dosyası için kontrol.
CONFIG_CHECK = os.environ.get(
    "___________LUTFEN_______BU_____SATIRI_____SILIN__________", None)

if CONFIG_CHECK:
    LOGS.info(
        "Lütfen ilk hashtag'de belirtilen satırı config.env dosyasından kaldırın"
    )
    quit(1)

# Bot dili
LANGUAGE = os.environ.get("LANGUAGE", "DEFAULT").upper()

if not LANGUAGE in ["EN", "TR", "AZ", "UZ", "DEFAULT"]:
    LOGS.info("Bilinmeyen bir dil yazdınız. Bu yüzden DEFAULT kullanılıyor.")
    LANGUAGE = "DEFAULT"
    
# Doge versiyonu
DOGE_VERSION = "v0.3"

# Telegram API KEY ve HASH
API_KEY = os.environ.get("API_KEY", None)
API_HASH = os.environ.get("API_HASH", None)

SILINEN_PLUGIN = {}
# UserBot Session String
STRING_SESSION = os.environ.get("STRING_SESSION", None)

# Kanal / Grup ID yapılandırmasını günlüğe kaydetme.
BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID", None))

# UserBot günlükleme özelliği.
BOTLOG = sb(os.environ.get("BOTLOG", "False"))
LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "False"))

# PM oto cevaplama
PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))

# Güncelleyici için Heroku hesap bilgileri.
HEROKU_MEMEZ = sb(os.environ.get("HEROKU_MEMEZ", "False"))
HEROKU_APPNAME = os.environ.get("HEROKU_APPNAME", None)
HEROKU_APIKEY = os.environ.get("HEROKU_APIKEY", None)

# Güncelleyici için özel (fork) repo linki.
UPSTREAM_REPO_URL = os.environ.get(
    "UPSTREAM_REPO_URL",
    "https://github.com/DogeUserBot/DogeUserBot.git")

# Ayrıntılı konsol günlügü
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

# SQL Veritabanı
DB_URI = os.environ.get("DATABASE_URL", "sqlite:///doge.db")

# OCR API key
OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)

# remove.bg API key
REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)

# AUTO PP
AUTO_PP = os.environ.get("AUTO_PP", None)

# Warn modül
WARN_LIMIT = int(os.environ.get("WARN_LIMIT", 3))
WARN_MODE = os.environ.get("WARN_MODE", "gmute")

if not WARN_MODE in ["gmute", "gban"]:
    WARN_MODE = "gmute"

# Galeri
GALERI_SURE = int(os.environ.get("GALERI_SURE", 60))

# Google Chrome sürücüsü ve dosyaları
CHROME_DRIVER = os.environ.get("CHROME_DRIVER", None)
GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", None)

PLUGINID = os.environ.get("PLUGIN_CHANNEL_ID", None)
# Plugin için
if not PLUGINID:
    PLUGIN_CHANNEL_ID = "me"
else:
    PLUGIN_CHANNEL_ID = int(PLUGINID)

# OpenWeatherMap API Key
OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
WEATHER_DEFCITY = os.environ.get("WEATHER_DEFCITY", None)

# Lydia API
LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)

# Anti Spambot
ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))
ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "True"))

# Youtube API key
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)

# Saat & Tarih - Ülke ve Saat Dilimi
COUNTRY = str(os.environ.get("COUNTRY", ""))
TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))

# Hoş geldin mesajı
CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))

# Last.fm Modülü
BIO_PREFIX = os.environ.get("BIO_PREFIX", "@DogeUserBot | ")
DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)

LASTFM_API = os.environ.get("LASTFM_API", None)
LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
LASTFM_PASS = md5(LASTFM_PASSWORD_PLAIN)
if LASTFM_API and LASTFM_SECRET and LASTFM_USERNAME and LASTFM_PASS:
    lastfm = LastFMNetwork(api_key=LASTFM_API,
                           api_secret=LASTFM_SECRET,
                           username=LASTFM_USERNAME,
                           password_hash=LASTFM_PASS)
else:
    lastfm = None

# Google Drive Modülü
G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY",
                                         "./downloads")

#Revert yani Klondan Sonra hesabın eski haline dönmesi
DEFAULT_NAME = os.environ.get("DEFAULT_NAME", None)


# Inline bot çalışması için
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
BOT_USERNAME = os.environ.get("BOT_USERNAME", None)

# Genius modülünün çalışması için buradan değeri alın https://genius.com/developers her ikisi de aynı değerlere sahiptir
GENIUS = os.environ.get("GENIUS", None)
CMD_HELP = {}
CMD_HELP_BOT = {}
PM_AUTO_BAN_LIMIT = int(os.environ.get("PM_AUTO_BAN_LIMIT", 4))

SPOTIFY_DC = os.environ.get("SPOTIFY_DC", None)
SPOTIFY_KEY = os.environ.get("SPOTIFY_KEY", None)

PAKET_ISMI = os.environ.get("PAKET_ISMI", "@DogeUserBot Paketi")

# Userbotu kapatmak için gruplar
BL_CHATS = os.environ.get("BL_CHATS", None)
if not BL_CHATS: #Ayarlanmamışsa Doge Support grubu ekle
    BL_CHATS = [-1001310554327]

# Otomatik Katılma
OTOMATIK_KATILMA = sb(os.environ.get("OTOMATIK_KATILMA", "True"))

# Güncellemeler
AUTO_UPDATE = sb(os.environ.get("AUTO_UPDATE", "True"))

# Özel Pattern'ler
PATTERNS = os.environ.get("PATTERNS", ".;!,")
WHITELIST = get('https://raw.githubusercontent.com/MUTLCC/Doge/doge/whitelist.json').json()


# Bot versiyon kontrolü
forceVer = []
if os.path.exists("force-version.check"):
    os.remove("force-version.check")
else:
    LOGS.info("Zorunlu versiyon kontrol dosyası yok, getiriyorum...")

URL = 'https://raw.githubusercontent.com/MUTLCC/Doge/doge/force-version.check' 
with open('force-version.check', 'wb') as load:
    load.write(get(URL).content)

DB = connect("force-version.check")
CURSOR = DB.cursor()
CURSOR.execute("""SELECT * FROM VERSION1""")
ALL_ROWS = CURSOR.fetchall()

for i in ALL_ROWS:
    forceVer.append(i[0])
connect("force-version.check").close() 


# CloudMail.ru ve MEGA.nz ayarlama
if not os.path.exists('bin'):
    os.mkdir('bin')

binaries = {
    "https://raw.githubusercontent.com/yshalsager/megadown/master/megadown":
    "bin/megadown",
    "https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py":
    "bin/cmrudl"
}

for binary, path in binaries.items():
    downloader = SmartDL(binary, path, progress_bar=False)
    downloader.start()
    os.chmod(path, 0o755)

# Bot değişkeni
if STRING_SESSION:
    # pylint: devre dışı=geçersiz ad
    bot = TelegramClient(StringSession(STRING_SESSION), API_KEY, API_HASH)
else:
    # pylint: devre dışı=geçersiz ad
    bot = TelegramClient("userbot", API_KEY, API_HASH)


if os.path.exists("learning-data-root.check"):
    os.remove("learning-data-root.check")
else:
    LOGS.info("Braincheck dosyası yok, getiriyorum...")

URL = 'https://raw.githubusercontent.com/MUTLCC/Doge/doge/learning-data-root.check'
with open('learning-data-root.check', 'wb') as load:
    load.write(get(URL).content)

async def check_botlog_chatid():
    if not BOTLOG_CHATID and LOGSPAMMER:
        LOGS.info(
            "Özel hata günlüğünün çalışması için yapılandırmadan BOTLOG_CHATID değişkenini ayarlamanız gerekir.")
        quit(1)

    elif not BOTLOG_CHATID and BOTLOG:
        LOGS.info(
            "Günlüğe kaydetme özelliğinin çalışması için yapılandırmadan BOTLOG_CHATID değişkenini ayarlamanız gerekir.")
        quit(1)

    elif not BOTLOG or not LOGSPAMMER:
        return

    entity = await bot.get_entity(BOTLOG_CHATID)
    if entity.default_banned_rights.send_messages:
        LOGS.info(
            "Hesabınızın BOTLOG_CHATID grubuna mesaj gönderme yetkisi yok. "
            "Grup ID'sini tekrar kontrol edin!")
        quit(1)
        
if not BOT_TOKEN == None:
    tgbot = TelegramClient(
        "TG_BOT_TOKEN",
        api_id=API_KEY,
        api_hash=API_HASH
    ).start(bot_token=BOT_TOKEN)
else:
    tgbot = None

def butonlastir(sayfa, moduller):
    Satir = 5
    Kolon = 2
    
    moduller = sorted([modul for modul in moduller if not modul.startswith("_")])
    pairs = list(map(list, zip(moduller[::2], moduller[1::2])))
    if len(moduller) % 2 == 1:
        pairs.append([moduller[-1]])
    max_pages = ceil(len(pairs) / Satir)
    pairs = [pairs[i:i + Satir] for i in range(0, len(pairs), Satir)]
    butonlar = []
    for pairs in pairs[sayfa]:
        butonlar.append([
            custom.Button.inline("🐾 " + pair, data=f"bilgi[{sayfa}]({pair})") for pair in pairs
        ])

    butonlar.append([custom.Button.inline("◀️ GERI", data=f"sayfa({(max_pages - 1) if sayfa == 0 else (sayfa - 1)})"), custom.Button.inline("KAPAT", data="close"), custom.Button.inline("ILERI ▶️", data=f"sayfa({0 if sayfa == (max_pages - 1) else sayfa + 1})")])
    return [max_pages, butonlar]

with bot:
    if OTOMATIK_KATILMA:
        try:
            bot(JoinChannelRequest("@DogeUserBot"))
        except:
            pass
    else:
        try:
            bot(JoinChannelRequest("@DogeUserBot"))
            bot(JoinChannelRequest("@DogeSup"))

        except:
            pass

    moduller = CMD_HELP
    me = bot.get_me()
    uid = me.id

    try:
        @tgbot.on(NewMessage(pattern='/start'))
        async def start_bot_handler(event):
            if not event.message.from_id == uid:
                await event.reply(f'**🐶 Merhaba ben @DogeUserBot!\n🐾 Yalnızca **@{me.username}** sahibime yardımcı oluyorum.\nFakat üzülme bunu birlikte çözebiliriz.\nEğer senin de bi` köpeğin olmasını istiyorsan, sen de hesabına beni kurabilirsin. \n\nBeni kurmak için; \n@DogeUserBot kanalımdan yardım alabilirsin\nya da\n@DogeSup grubuma #kur yazabilirsin!**')
            else:
                await event.reply(f'**🐶 Hav hav! 🐾 Doge living...**')

        @tgbot.on(InlineQuery)  # pylint:disable=E0602
        async def inline_handler(event):
            builder = event.builder
            result = None
            query = event.text
            if event.query.user_id == uid and query == "@DogeUserBot":
                rev_text = query[::-1]
                veriler = (butonlastir(0, sorted(CMD_HELP)))
                result = await builder.article(
                    f"Lütfen .yardım ya da .help komutu ile kullanın.",
                    text=f"**ㅤ\n[🐶 𝘿𝙊𝙂𝙀 𝙐𝙎𝙀𝙍𝘽𝙊𝙏](https://Telegram.dog/DogeUserBot)\n\nHerhangi bir komutu öğrenmek için bir butona dokun.\n\nKurulu modüller:** `{len(CMD_HELP)}`\n**Sayfa:** `1 - {veriler[0]}`",
                    buttons=veriler[1],
                    link_preview=False
                )
            elif query.startswith("http"):
                parca = query.split(" ")
                result = builder.article(
                    "Dosyayı yükledim!",
                    text=f"**Dosyayı {parca[2]} sitesine yükledim!\n\nYükleme zamanı:** {parca[1][:3]} saniye\n[‏‏‎ ‎]({parca[0]})",
                    buttons=[
                        [custom.Button.url('URL', parca[0])]
                    ],
                    link_preview=True
                )
            else:
                result = builder.article(
                    "@DogeUserBot",
                    text="""Telegram'da bir köpeğiniz olsun!\nTelegram hesabınıza @DogeUserBot kurup yararlı araçları ve bu eğlenceli komutları Doge sayesinde kullanabilirsiniz.\nUnutmayın, başkasının köpeğine sahip olamazsınız!\nGitHub Repo'm! ya da Grubuma Katıl! butonuna dokunup tüm kurulum detaylarını öğrenebilirsiniz!""",
                    buttons=[
                        [custom.Button.url("Kanalıma Katıl!", "https://t.me/DogeUserBot"), custom.Button.url(
                            "Grubuma Katıl!", "https://t.me/DogeSup")],
                        [custom.Button.url(
                            "GitHub Repo'm!", "https://github.com/DogeUserBot/DogeUserBot")]
                    ],
                    link_preview=False
                )
            await event.answer([result] if result else None)

        @tgbot.on(callbackquery.CallbackQuery(data=compile(b"sayfa\((.+?)\)")))
        async def sayfa(event):
            if not event.query.user_id == uid: 
                return await event.answer("🐶 𝘿𝙊𝙂𝙀 𝙐𝙎𝙀𝙍𝘽𝙊𝙏\n\n🐶 Hav! Bunu yapamam.\n🐾 Sen benim sahibim değilsin!\nSen de bir @DogeUserBot sahiplen!", cache_time=0, alert=True)
            sayfa = int(event.data_match.group(1).decode("UTF-8"))
            veriler = butonlastir(sayfa, CMD_HELP)
            await event.edit(
                f"**ㅤ\n[🐶 𝘿𝙊𝙂𝙀 𝙐𝙎𝙀𝙍𝘽𝙊𝙏](https://Telegram.dog/DogeUserBot)\n\nHerhangi bir komutu öğrenmek için bir butona dokun.\n\nKurulu modüller:** `{len(CMD_HELP)}`\n**Sayfa:** `{sayfa + 1} - {veriler[0]}`",
                buttons=veriler[1],
                link_preview=False
            )
        
        @tgbot.on(callbackquery.CallbackQuery(data=compile(b"close")))
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                await event.delete()

        @tgbot.on(callbackquery.CallbackQuery(data=compile(b"bilgi\[(\d*)\]\((.*)\)")))
        async def bilgi(event):
            if not event.query.user_id == uid: 
                return await event.answer("🐶 𝘿𝙊𝙂𝙀 𝙐𝙎𝙀𝙍𝘽𝙊𝙏\n\n🐶 Hav! Bunu yapamam.\n🐾 Sen benim sahibim değilsin!\nSen de bir @DogeUserBot sahiplen!", cache_time=0, alert=True)

            sayfa = int(event.data_match.group(1).decode("UTF-8"))
            komut = event.data_match.group(2).decode("UTF-8")
            try:
                butonlar = [custom.Button.inline("🐾 " + cmd[0], data=f"komut[{komut}[{sayfa}]]({cmd[0]})") for cmd in CMD_HELP_BOT[komut]['commands'].items()]
            except KeyError:
                return await event.answer("❌ Bu modülde açıklama yok.", cache_time=0, alert=True)

            butonlar = [butonlar[i:i + 2] for i in range(0, len(butonlar), 2)]
            butonlar.append([custom.Button.inline("◀️ GERI", data=f"sayfa({sayfa})")])
            await event.edit(
                f"**ㅤ\n[🐶 𝘿𝙊𝙂𝙀 𝙐𝙎𝙀𝙍𝘽𝙊𝙏](https://Telegram.dog/DogeUserBot)\n\nHerhangi bir komutu öğrenmek için bir butona dokun.\n\n📗 DOSYA:** `{komut}`\n**🔢 KOMUTLAR:** `{len(CMD_HELP_BOT[komut]['commands'])}`",
                buttons=butonlar,
                link_preview=False
            )
        
        @tgbot.on(callbackquery.CallbackQuery(data=compile(b"komut\[(.*)\[(\d*)\]\]\((.*)\)")))
        async def komut(event):
            if not event.query.user_id == uid: 
                return await event.answer("🐶 𝘿𝙊𝙂𝙀 𝙐𝙎𝙀𝙍𝘽𝙊𝙏\n\n🐶 Hav! Bunu yapamam.\n🐾 Sen benim sahibim değilsin!\nSen de bir @DogeUserBot sahiplen!", cache_time=0, alert=True)

            cmd = event.data_match.group(1).decode("UTF-8")
            sayfa = int(event.data_match.group(2).decode("UTF-8"))
            komut = event.data_match.group(3).decode("UTF-8")

            result = f"**🐶 𝘿𝙊𝙂𝙀 𝙐𝙎𝙀𝙍𝘽𝙊𝙏 🐾\n\n🧩 Pʟᴜɢɪɴ:**       `{cmd}`\n"
            if CMD_HELP_BOT[cmd]['info']['info'] == '':
                if not CMD_HELP_BOT[cmd]['info']['warning'] == '':
                    result += f"**🛡 Oꜰꜰɪᴄɪᴀʟ:**     {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n"
                    result += f"**⚠️ Dɪᴋᴋᴀᴛ:**       {CMD_HELP_BOT[cmd]['info']['warning']}\n\n"
                else:
                    result += f"**🛡 Oꜰꜰɪᴄɪᴀʟ:**     {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n\n"
            else:
                result += f"**🛡 Oꜰꜰɪᴄɪᴀʟ:**     {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n"
                if not CMD_HELP_BOT[cmd]['info']['warning'] == '':
                    result += f"**⚠️ Dɪᴋᴋᴀᴛ:**       {CMD_HELP_BOT[cmd]['info']['warning']}\n"
                result += f"**ℹ️ Bɪʟɢɪ:**           {CMD_HELP_BOT[cmd]['info']['info']}\n\n"

            command = CMD_HELP_BOT[cmd]['commands'][komut]
            if command['params'] is None:
                result += f"**🔰 Kᴏᴍᴜᴛ:**        `{PATTERNS[:1]}{command['command']}`\n"
            else:
                result += f"**🔰 Kᴏᴍᴜᴛ:**        `{PATTERNS[:1]}{command['command']} {command['params']}`\n"
                
            if command['example'] is None:
                result += f"**💬 Aᴄɪᴋʟᴀᴍᴀ:**  `{command['usage']}`\n\n"
            else:
                result += f"**💬 Aᴄɪᴋʟᴀᴍᴀ:**  `{command['usage']}`\n"
                result += f"**💡 Öʀɴᴇᴋ:**        `{PATTERNS[:1]}{command['example']}`\n\n"

            await event.edit(
                result,
                buttons=[custom.Button.inline("◀️ GERI", data=f"bilgi[{sayfa}]({cmd})")],
                link_preview=False
            )
    except Exception as e:
        print(e)
        LOGS.info(
            "Botunuzda inline desteği devre dışı bırakıldı. "
            "Etkinleştirmek için bir BOT_TOKEN tanımlayın ve botunuzda inline modunu etkinleştirin. "
            "Eğer bunun dışında bir sorun olduğunu düşünüyorsanız bize ulaşın: T.me/DogeSup"
        )

    try:
        bot.loop.run_until_complete(check_botlog_chatid())
    except:
        LOGS.info(
            "BOTLOG_CHATID eksik ya da yanlış girilmiş."
            "Ortam değişkenlerinizi / config.env dosyanızı kontrol edin."
        )
        quit(1)


# Küresel Değişkenler
SON_GORULME = 0
COUNT_MSG = 0
USERS = {}
MYID = uid
ForceVer = str(forceVer[0])
doge_ = 1
BRAIN_CHECKER = []
COUNT_PM = {}
LASTMSG = {}
FUP = True
ENABLE_KILLME = True
ISAFK = False
AFKREASON = None
ZALG_LIST = [[
    "̖",
    " ̗",
    " ̘",
    " ̙",
    " ̜",
    " ̝",
    " ̞",
    " ̟",
    " ̠",
    " ̤",
    " ̥",
    " ̦",
    " ̩",
    " ̪",
    " ̫",
    " ̬",
    " ̭",
    " ̮",
    " ̯",
    " ̰",
    " ̱",
    " ̲",
    " ̳",
    " ̹",
    " ̺",
    " ̻",
    " ̼",
    " ͅ",
    " ͇",
    " ͈",
    " ͉",
    " ͍",
    " ͎",
    " ͓",
    " ͔",
    " ͕",
    " ͖",
    " ͙",
    " ͚",
    " ",
],
    [
    " ̍", " ̎", " ̄", " ̅", " ̿", " ̑", " ̆", " ̐", " ͒", " ͗",
    " ͑", " ̇", " ̈", " ̊", " ͂", " ̓", " ̈́", " ͊", " ͋", " ͌",
    " ̃", " ̂", " ̌", " ͐", " ́", " ̋", " ̏", " ̽", " ̉", " ͣ",
    " ͤ", " ͥ", " ͦ", " ͧ", " ͨ", " ͩ", " ͪ", " ͫ", " ͬ", " ͭ",
    " ͮ", " ͯ", " ̾", " ͛", " ͆", " ̚"
],
    [
    " ̕",
    " ̛",
    " ̀",
    " ́",
    " ͘",
    " ̡",
    " ̢",
    " ̧",
    " ̨",
    " ̴",
    " ̵",
    " ̶",
    " ͜",
    " ͝",
    " ͞",
    " ͟",
    " ͠",
    " ͢",
    " ̸",
    " ̷",
    " ͡",
]]

# Copyright © 2021 Doge UserBot in Telegram App
# All rights reserved.
#
# Licensed under the Doge UserBot Public License;
# you may not use this file except in compliance with the License.
#
# @MUTLCC | @SanalMafya
#

import asyncio
import os
import sys
import subprocess
from installer import hata, bilgi, onemli, soru
from telethon import TelegramClient, events, version
from telethon.errors import SessionPasswordNeededError, PhoneCodeInvalidError, PasswordHashInvalidError, PhoneNumberInvalidError
from telethon.network import ConnectionTcpAbridged
from telethon.utils import get_display_name
from telethon.sessions import StringSession
from rich.prompt import Prompt
from rich.panel import Panel
from rich.live_render import LiveRender
from random import choice, randint
from .language import LANG
import requests
import bs4

os.system("clear")
loop = asyncio.get_event_loop()
LANG  = LANG['ASTRING']

class InteractiveTelegramClient(TelegramClient):
    # Original Source https://github.com/LonamiWebs/Telethon/master/telethon_examples/interactive_telegram_client.py #

    def __init__(self, session_user_id, api_id, api_hash,
                 telefon=None, proxy=None):
        super().__init__(
            session_user_id, api_id, api_hash,
            connection=ConnectionTcpAbridged,
            proxy=proxy
        )
        self.found_media = {}
        bilgi(LANG['CONNECTING'])
        try:
            loop.run_until_complete(self.connect())
        except IOError:
            hata(LANG['RETRYING'])
            loop.run_until_complete(self.connect())

        if not loop.run_until_complete(self.is_user_authorized()):
            if telefon == None:
                hh = 0
                while hh<1:
                    user_phone = soru(LANG['PHONE_NUMBER'])
                    if user_phone.startswith("+"):
                        hh+=1
                    else:
                        hata(LANG['INVALID_FORMAT'])
            else:
               user_phone = telefon
            try:
                loop.run_until_complete(self.sign_in(user_phone))
                self_user = None
            except PhoneNumberInvalidError:
                hata(LANG['INVALID_NUMBER'])
                exit(1)
            except ValueError:
               hata(LANG['INVALID_NUMBER'])
               exit(1)

            while self_user is None:
               code = soru(LANG['CODE'])
               try:
                  self_user =\
                     loop.run_until_complete(self.sign_in(code=code))
               except PhoneCodeInvalidError:
                  hata(LANG['INVALID_CODE'])
               except SessionPasswordNeededError:
                  bilgi(LANG['2FA'])
                  pw = soru(LANG['PASS'])
                  try:
                     self_user =\
                        loop.run_until_complete(self.sign_in(password=pw))
                  except PasswordHashInvalidError:
                     hata(LANG['INVALID_2FA'])

def main():
    bilgi(f"[1] {LANG['NEW']}\n[2] {LANG['OLD']}")
            
    Sonuc = Prompt.ask(Panel(f"[bold yellow]{LANG['WHICH']}[/]", choices=["1", "2"], default="1"))

    if Sonuc == "2":
        API_ID = soru(LANG['API_ID'])
        if API_ID == "":
            bilgi(LANG['USING_TG'])
            API_ID = 6
            API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
        else:
            API_HASH = soru(LANG['API_HASH'])
        client = InteractiveTelegramClient(StringSession(), API_ID, API_HASH)
        return client.session.save(), API_ID, API_HASH
    elif Sonuc == "1":
        numara = soru(LANG['PHONE_NUMBER_NEW'])
        try:
            rastgele = requests.post("https://my.telegram.org/auth/send_password", data={"phone": numara}).json()["random_hash"]
        except:
            hata(LANG['CANT_SEND_CODE'])
            exit(1)
      
        sifre = soru(LANG['WRITE_CODE_FROM_TG'])
        try:
            cookie = requests.post("https://my.telegram.org/auth/login", data={"phone": numara, "random_hash": rastgele, "password": sifre}).cookies.get_dict()
        except:
            hata(LANG['INVALID_CODE_MY'])
            exit(1)
        app = requests.post("https://my.telegram.org/apps", cookies=cookie).text
        soup = bs4.BeautifulSoup(app, features="html.parser")

        if soup.title.string == "Create new application":
            bilgi(LANG['NEW_APP'])
            hashh = soup.find("input", {"name": "hash"}).get("value")
            app_title = soru(LANG['WHATIS_APPNAME'])
            if app_title == '':
                app_title = choice(["dog", "doge", "dogee", "dogeee", "dogs", "doges"]) + choice(["", "-", "+", " "]) + choice(["user", "bot", "bote", "userb", "ub", "ubot"]) + choice([str(randint(10000, 99999)), ""])
            app_shortname = soru(LANG['WHATIS_SAPPNAME'])
            if app_shortname == '':
                app_shortname = choice(["dog", "doge", "dogee", "dogeee", "dogs", "doges"]) + choice(["", "-", "+", " "]) + choice(["user", "bot", "bote", "userb", "ub", "ubot"]) + choice([str(randint(10000, 99999)), ""])
            AppInfo = {
                "hash": hashh,
                "app_title": app_title,
                "app_shortname": app_shortname,
                "app_url": "",
                "app_platform": choice(["android", "ios", "web", "desktop"]),
                "app_desc": choice(["madelineproto", "pyrogram", "telethon", "", "web", "cli"])
            }
            app = requests.post("https://my.telegram.org/apps/create", data=AppInfo, cookies=cookie).text

            if app == "ERROR":
                hata(LANG['CANT_CREATE_APP'])
                exit(1)

            bilgi(LANG['CREATED'])
            bilgi(LANG['GETTING_API'])
            newapp = requests.get("https://my.telegram.org/apps", cookies=cookie).text
            newsoup = bs4.BeautifulSoup(newapp, features="html.parser")

            g_inputs = newsoup.find_all("span", {"class": "form-control input-xlarge uneditable-input"})

            app_id = g_inputs[0].string
            api_hash = g_inputs[1].string
            bilgi(LANG['INFOS'])
            onemli(f"{LANG['APIID']} {app_id}")
            onemli(f"{LANG['APIHASH']} {api_hash}")
            bilgi(LANG['STRING_GET'])
            client = InteractiveTelegramClient(StringSession(), app_id, api_hash, numara)
        
            return client.session.save(), app_id, api_hash
        elif soup.title.string == "App configuration":
            bilgi(LANG['SCRAPING'])
            g_inputs = soup.find_all("span", {"class": "form-control input-xlarge uneditable-input"})
            app_id = g_inputs[0].string
            api_hash = g_inputs[1].string
            bilgi(LANG['INFOS'])
            onemli(f"{LANG['APIID']} {app_id}")
            onemli(f"{LANG['APIHASH']} {api_hash}")
            bilgi(LANG['STRING_GET'])

            client = InteractiveTelegramClient(StringSession(), app_id, api_hash, numara)
            return client.session.save(), app_id, api_hash
        else:
            hata(LANG['ERROR'])
            exit(1)
    else:
        hata(LANG['ERRCHOOSE'])
        exit(1)

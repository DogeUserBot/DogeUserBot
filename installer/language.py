# Copyright © 2021 Doge UserBot in Telegram App
# All rights reserved.
#
# Licensed under the Doge UserBot Public License;
# you may not use this file except in compliance with the License.
#
# @MUTLCC | @SanalMafya
#

from json import loads
from rich.prompt import Prompt
from rich.panel import Panel
from rich.live_render import LiveRender
from . import logo, console, basarili

def importlang ():
    console.clear()
    logo()
    basarili("\n\n[1] Türkçe\n\n[2] Azərbaycanca\n\n[3] English\n\n[4] O'zbek\n")
    Dil = Prompt.ask(Panel(f"[bold yellow]💬 Bir dil seçin\n💬 Please select a language\n[/]", choices=["1", "2", "3", "4"], default="1"))

    if Dil == "1":
        COUNTRY = "Turkey"
        LANGUAGE = "TR"
        TZ = "Europe/Istanbul"
    elif Dil == "2":
        COUNTRY = "Azerbaijan"
        LANGUAGE = "AZ"
        TZ = "Asia/Baku"
    elif Dil == "3":
        COUNTRY = "United Kingdom"
        LANGUAGE = "EN"
        TZ = "Europe/London"
    elif Dil == "4":
        COUNTRY = "Uzbekistan"
        LANGUAGE = "UZ"
        TZ = "Asia/Tashkent"

    return COUNTRY, LANGUAGE, TZ

COUNTRY, LANGUAGE, TZ = importlang()
LANG = loads(open(f"./installer/language/{LANGUAGE}.dogejson", "r").read())["STRINGS"]

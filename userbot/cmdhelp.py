# Copyright © 2021 Doge UserBot in Telegram App
# All rights reserved.
#
# Licensed under the Doge UserBot Public License;
# you may not use this file except in compliance with the License.
#
# @MUTLCC | @SanalMafya
#

from userbot import PATTERNS, CMD_HELP, CMD_HELP_BOT

class CmdHelp:
    """
    Komut yardımlarını daha iyi üretmek için yazdığım sınıf.
    """

    FILE = ""
    ORIGINAL_FILE = ""
    FILE_AUTHOR = ""
    IS_OFFICIAL = True
    COMMANDS = {}
    PREFIX = PATTERNS[:1]
    WARNING = ""
    INFO = ""

    def __init__(self, file: str, official : bool = True, file_name : str = None):
        self.FILE = file
        self.ORIGINAL_FILE = file
        self.IS_OFFICIAL = official
        self.FILE_NAME = file_name if not file_name == None else file + '.py'
        self.COMMANDS = {}
        self.FILE_AUTHOR = ""
        self.WARNING = ""
        self.INFO = ""

    def set_file_info(self, name : str, value : str):
        if name == 'name':
            self.FILE = value
        elif name == 'author':
            self.FILE_AUTHOR = value
        return self
        
    def add_command(self, command : str, params = None, usage: str = '', example = None):
        """
        Komut ekler.
        """
        
        self.COMMANDS[command] = {'command': command, 'params': params, 'usage': usage, 'example': example}
        return self
    
    def add_warning(self, warning):
        self.WARNING = warning
        return self
    
    def add_info(self, info):
        self.INFO = info
        return self

    def get_result(self):
        """
        Sonuç getirir.
        """

        result = f"**🐶 𝘿𝙊𝙂𝙀 𝙐𝙎𝙀𝙍𝘽𝙊𝙏 🐾\n\n 🧩 Pʟᴜɢɪɴ:** `{self.FILE}`\n"
        if self.WARNING == '' and self.INFO == '':
            result += f"**🛡 Oꜰꜰɪᴄɪᴀʟ:** {'✅' if self.IS_OFFICIAL else '❌'}\n\n"
        else:
            result += f"**🛡 Oꜰꜰɪᴄɪᴀʟ:** {'✅' if self.IS_OFFICIAL else '❌'}\n"
            
            if self.INFO == '':
                if not self.WARNING == '':
                    result += f"**⚠️ Dɪᴋᴋᴀᴛ:** {self.WARNING}\n\n"
            else:
                if not self.WARNING == '':
                    result += f"**⚠️ Dɪᴋᴋᴀᴛ:** {self.WARNING}\n"
                result += f"**ℹ️ Bɪʟɢɪ:** {self.INFO}\n\n"
                     
        for command in self.COMMANDS:
            command = self.COMMANDS[command]
            if command['params'] == None:
                result += f"**🔰 Kᴏᴍᴜᴛ:** `{PATTERNS[:1]}{command['command']}`\n"
            else:
                result += f"**🔰 Kᴏᴍᴜᴛ:** `{PATTERNS[:1]}{command['command']} {command['params']}`\n"
                
            if command['example'] == None:
                result += f"**💬 Aᴄɪᴋʟᴀᴍᴀ:** {command['usage']}\n\n"
            else:
                result += f"**💬 Aᴄɪᴋʟᴀᴍᴀ:** {command['usage']}\n\n"
                result += f"**💡 Öʀɴᴇᴋ:** `{PATTERNS[:1]}{command['example']}`\n\n"
        return result

    def add(self):
        """
        Direkt olarak CMD_HELP ekler.
        """
        CMD_HELP_BOT[self.FILE] = {'info': {'official': self.IS_OFFICIAL, 'warning': self.WARNING, 'info': self.INFO}, 'commands': self.COMMANDS}
        CMD_HELP[self.FILE] = self.get_result()
        return True
    
    def getText(self, text : str):
        if text == 'REPLY_OR_USERNAME':
            return '<kullanıcı adı> <kullanıcı adı/yanıtlama>'
        elif text == 'OR':
            return 'veya'
        elif text == 'USERNAMES':
            return '<kullanıcı ad(lar)ı>'

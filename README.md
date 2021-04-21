<p align="center"><a href="https://t.me/DogeUserBot"><img src="https://raw.githubusercontent.com/DogeUserBot/DogeInstaller/main/DogeUserBot.jpg" width="400"></a></p>
  <h1 align="center">🐶 DOGE USERBOT 🐾</h1>
</p>
<p align="center">
    ❤️ Telegram'da bir köpeğiniz olsun!
    <br>
    ❤️ Have a dog in Telegram!
    <br>
    <br>
        <a href="https://bit.ly/DogeUserBot">📣 Güncelleme Duyuruları | Update News</a>
    <br>
    <br>
        <a href="https://t.me/DogeSup">💬 Destek Grubu | Support Group</a>
    <br>
    <br>
        <a href="https://t.me/DogePlugin">📥 Pluginler | Plugins</a>
    <br>
    <br>
        <a href="https://github.com/DogeUserBot/DogeUserBot#-kolay-kurulumlar">⚡ Kurulumlar | Installations </a>
</p>

----

## 🔗 Kolay Kurulumlar | Easy Installations

### 🌐 Online Kurucu | Online Installer
⬇️ Aşağıdaki butona tıklayın/dokunun:

[![Run on Repl.it](https://repl.it/badge/github/@DogeUserBot/DogeOnline)](https://bit.ly/DogeO)

----

### 🤖 Android
📲 [Termux uygulamasını "buradan" indirin,](https://bit.ly/DogeTermux)

📋 Aşağıdaki kodu Termux'a yapıştırın:

```bash <(curl -L https://bit.ly/Dogeai)```

----

### 🍎 IOS
📲 [TestFlight uygulamasını "buradan" indirin,](https://bit.ly/DogeFlight)

📲 [ISH uygulamasını "buradan" indirip 'Start Testing'e dokunun,](https://bit.ly/DogeISH)

📋 Aşağıdaki kodu ISH'a yapıştırın:

```apk update && apk add bash && apk add curl && curl -L -o doge_installer.sh https://bit.ly/DogeIOS && chmod +x doge_installer.sh && bash doge_installer.sh```

----

### 💻 Windows
🖥️ [Python 3.8'i "buradan" indirin,](https://bit.ly/DogePythonMS)

📋 Aşağıdaki kodu PowerShell'e yapıştırın:

```Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://bit.ly/DogeWindows')```

----

## 🔗 Zor Kurulumlar | Diffucult Installations
### 🌐 Elle Kurulum | Manuel Installation
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://bit.ly/DogeHeroku)

----

### ℹ️ Terminal, Termux, vb.
```sh
git clone https://github.com/DogeUserBot/DogeInstaller 
cd installer
pip install -r requirements.txt
python3 -m doge_installer
```

----

## 🪧 Örnek Plugin Gösterimi | Example Plugin
```python
from userbot.events import register
from userbot.cmdhelp import CmdHelp 
# <-- Bunu ekleyin ve daha sonra herhangi bir metin yazabilirsiniz.

@register(outgoing=True, pattern="^.ornekdeneme")
async def ornekdeneme(event):
    await event.edit('Bu bir örnek deneme pluginidir!')

Help = CmdHelp('deneme') # Bilgi ekleyeceğiz.
Help.add_command('ornekdeneme', # Komutu bu şekilde yazıyoruz.
    None, # Komut parametresi varsa yazın yoksa None yazın.
    'Deneme yapıyor.', # Komut açıklamasını bu şekilde belirtiyoruz.
    'ornekdeneme' # Örnek komut kullanımını burada belirtiyoruz.
    )
Help.add_info('@MUTLCC ve @Yigix tarafından @DogeUserBot için yapıldı.') # Buna benzer bilgi ekleyebilirsiniz.
Help.add_warning('BUNU YAPMA!') # Buraya uyarı ekleyebilirsiniz.
Help.add() # Plugini bu şekilde bitiriyoruz.
```

----

## 👤 Oluşturucular | Creators
💚 [Mutlu](https://t.me/MutluTelegram)

💜 [Yiğit](https://t.me/SanalMafya)

----

## 💬 Bilgilendirme | Information
📍 Herhangi bir soru veya geribildirim için bize [🐶 Doge Destek grubumuzdan](https://t.me/DogeSup) ulaşabilirsiniz.

```
ℹ️ Doge UserBot, açık kaynaklı bir projedir.

💡 UserBot kötüye kullanım sebebiyle;
    
   🚫 Telegram hesabınız kısıtlanabilir/yasaklanabilir.
    
   💣 Her yaptığınız işlemden sorumlu tutulursunuz.
    
   ⛔️ Doge UserBot yöneticileri hiçbir sorumluluk kabul etmemektedir.
    
   📍 Doge UserBot kurarak tüm bu sorumlulukları kabul etmiş olursunuz.
```

### 📝 Lisans | License
<a href="https://tr.m.wikipedia.org/wiki/GNU_Genel_Kamu_Lisans%C4%B1#"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/GPLv3_Logo.svg/1280px-GPLv3_Logo.svg.png" width="150"></a>

🔐 Bu proje GPL-3.0 lisansı ile korunmaktadır.

✅ Tüm hakları saklıdır.


### 🤍 Teşekkürler! | Thanks!
🧑‍💻 [Yusuf Usta](https://github.com/yusufusta)

----

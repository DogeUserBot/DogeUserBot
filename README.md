<p align="center"><a href="https://t.me/DogeUserBot"><img src="https://raw.githubusercontent.com/DogeUserBot/DogeInstaller/main/DogeUserBot.jpg" width="400"></a></p>
  <h1 align="center">🐶 Doge UserBot</h1>
</p>
<p align="center">
    ❤️ Telegram'da bir köpeğiniz olsun!
    <br>
    <br>
        <a href="https://t.me/DogeUserBot">📣 Telegram Kanalı</a>
    <br>
    <br>
        <a href="https://t.me/DogeDestek">💬 Telegram Destek Grubu</a>
    <br>
    <br>
        <a href="https://t.me/DogePlugin">📥 Plugin Kanalı</a>
    <br>
    <br>
        <a href="https://github.com/DogeUserBot/DogeUserBot#-kolay-kurulumlar">⚡ Kurulumlar</a>
</p>

----

## 🔗 Kolay Kurulumlar

### 🌐 Repl.it Online Kurucu
⬇️ Aşağıdaki butona/linke tıklayın/dokunun:

[![Run on Repl.it](https://repl.it/badge/github/@DogeUserBot/DogeOnline)](https://bit.ly/DogeO)

----

### 🤖 Android
📲 [Termux uygulamasını "buradan" indirin,](https://bit.ly/DogeTermux)

📋 Aşağıdaki kodu Termux'a yapıştırın:

```bash <(curl -L https://bit.ly/DogeAndroid)```

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

## 🔗 Zor Kurulumlar
### 🌐 Manuel Kurucu
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

## 🪧 Örnek Plugin Gösterimi
```python
from userbot.events import register
from userbot.cmdhelp import CmdHelp 
# <-- Bunu ekleyin ve daha sonra herhangi bir metin yazabilirsiniz.

@doge(outgoing=True, pattern="^.ornekdeneme")
async def ornekdeneme(event):
    await event.edit('Bu bir örnek deneme pluginidir!')

Help = CmdHelp('deneme') # Bilgi ekleyeceğiz.
Help.add_command('ornekdeneme', # Komutu bu şekilde yazıyoruz.
    None, # Komut parametresi varsa yazın yoksa None yazın.
    'Deneme yapıyor.', # Komut açıklamasını bu şekilde belirtiyoruz.
    'ornekdeneme' # Örnek komut kullanımını burada belirtiyoruz.
    )
Help.add_info('@MUTLCC ve @Yigix tarafından yapılmıştır.') # Buna benzer bilgi ekleyebilirsiniz.
Help.add_warning('UYARI BURAYA!') # Buraya uyarı ekleyebilirsiniz.
Help.add() # Plugini bu şekilde bitiriyoruz.
```

----

## 👤 Creators
💚 [Mutlu](https://t.me/MUTLCC)

💜 [Yiğit](https://t.me/SanalMafya)

----

## 💬 Bilgilendirme
📍 Herhangi bir soru veya geribildirim için bize [🐶 Doge Destek grubumuzdan](https://t.me/DogeDestek) ulaşabilirsiniz.

```
🟩 Doge UserBot, açık kaynaklı bir projedir.

ℹ️ UserBot kötüye kullanım sebebiyle;
    
   🟥 Telegram hesabınız kısıtlanabilir/yasaklanabilir.
    
   🟦 Her yaptığınız işlemden sorumlu tutulursunuz.
    
   🟨 Doge UserBot yöneticileri hiçbir sorumluluk kabul etmemektedir.
    
   🟧 Doge UserBot kurarak tüm bu sorumlulukları kabul etmiş olursunuz.
```

### 📝 Lisans
<a href="https://tr.m.wikipedia.org/wiki/GNU_Genel_Kamu_Lisans%C4%B1#"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/GPLv3_Logo.svg/1280px-GPLv3_Logo.svg.png" width="200"></a>

🔐 Bu proje GPL-3.0 lisansı ile korunmaktadır.

✅ Tüm hakları saklıdır.


### 🤍 Teşekkürler
🧑‍💻 [Yusuf Usta](https://github.com/yusufusta)

----

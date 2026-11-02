Bu proje, bağlantı hızını ölçmek için dosyaların nasıl gönderilip alındığını araştırır.

<h1 align="center">Network Transfer Lab</h1>

<p align="center"><strong>Bir hız testinin nasıl çalıştığını incele.</strong></p>
<p align="center">Tarayıcı zamanlama arayüzünü deneysel bir sunucu aktarım rotasıyla birleştiren Flask ders projesi prototipi.</p>

<p align="center">
  <a href="README.md">English</a> · <strong>Türkçe</strong><br />
  <a href="#yerel-arayüzü-çalıştır"><strong>Yerel arayüzü çalıştır</strong></a> ·
  <a href="#projede-neler-var">Projeye bakış</a> ·
  <a href="#doğrulama-ve-mevcut-sınırlar">Mevcut sınırlar</a>
</p>

---

Bu repo, Kasım 2023 tarihli ders projesinden Python, HTML ve JavaScript tabanlı bir hız testi deneyi içerir. Tarayıcı arayüzü indirme, yükleme ve HTTP isteklerinin zamanlamasını inceler. Ayrı bir sunucu rotası daha büyük bir dosyanın indirilmesini ve speedtest-cli ile yükleme ölçümünü dener.

**Bu, deneysel bir ders projesi prototipidir.** Aktarım rotalarına, zamanlama hesaplarına ve sunucu sonuç şablonuna statik düzeltmeler uygulandı. Proje bir deney olarak kalır ve çıktıları bant genişliği ölçümü olarak doğrulanmadı.

## Yerel arayüzü çalıştır

| Gereksinim | Amaç |
| --- | --- |
| pip ve venv içeren Python 3 | Yalıtılmış geliştirme ortamı |
| Flask, Requests ve speedtest-cli | Uygulamanın içe aktardığı bağımlılıklar |
| JavaScript destekli tarayıcı | Zamanlama arayüzü |

```text
git clone https://github.com/ArdaHFO/network-transfer-lab.git
cd network-transfer-lab
python -m venv .venv
```

Windows Komut İstemi'nde `.venv\Scripts\activate`, macOS/Linux'ta `source .venv/bin/activate` ile ortamı etkinleştir. Kayıtlı bağımlılıkları kur ve yerel önizlemeyi başlat.

```text
python -m pip install -r requirements.txt
python -m flask --app app run --host 127.0.0.1 --port 8000
```

[localhost:8000](http://127.0.0.1:8000) adresini aç. Flask CLI ve uygulamanın ana başlatıcısı varsayılan olarak debug kapalı, yerel erişim kullanır. Bağımlılık sürümleri geçmiş geliştirme ortamına aittir ve güncel Python kurulumlarıyla uyumlulukları yeniden doğrulanmadı.

## Projede neler var?

- **Tarayıcı zamanlama arayüzü.** Ayrı kontroller indirme zamanlamasını, multipart yüklemeyi ve HTTP gidiş-dönüşünü örnekler.
- **Özel sunucu indirmesi.** `speed_test` işlevi, yapılandırılmış dosyayı harici bir uç noktadan akış halinde indirir ve alınan baytları izler.
- **Kütüphane karşılaştırması.** `POST /measure`, speedtest-cli ile yükleme ölçümü içerir ve ping sonucunu okur.
- **Flask blueprint yapısı.** Küçük `views.py` modülü ek sayfa rotaları sağlar.
- **Aktarım örnekleri.** Deneylerde kullanılabilecek çeşitli görsel dosyaları bulunur.

Sunucu kodu, özel aktarım ölçümüyle birlikte speedtest-cli kullanır.

## Tarayıcı ve sunucu yolları

| Bileşen | Amaçlanan eylem | Mevcut durum |
| --- | --- | --- |
| Tarayıcı indirmesi | Paketlenmiş dosyayı getirip hız hesaplamak | Gerçek bayt sayısı ve geçen saniye |
| Tarayıcı yüklemesi | Dosyayı `POST /upload` adresine göndermek | Sunucu uygulama dosyası kaydetmeden bayt sayısını doğrular |
| Tarayıcı ping işlemi | `GET /ping` süresini ölçmek | Önbelleksiz `Pong` yanıtı |
| `POST /measure` | 100 MB indirme ve kütüphane ile yükleme | Sunucu sonuç şablonunu gösterir |
| `GET /views/measure` | Arayüzü açmak | Boş sonuç yerine arayüze yönlendirir |

Tarayıcıdaki HTTP zamanlamasıyla sunucudan başlayan aktarımlar farklı yolları ölçer. Uzak sunucuda üretilen sonuç sunucunun bağlantısını gösterir ve kullanıcının bağlantısını doğrudan temsil etmeyebilir.

## Doğrulama ve mevcut sınırlar

Kaynak statik olarak incelendi. Bu değişiklikler için uygulama, otomatik test, harici aktarım veya performans deneyi çalıştırılmadı.

- Tarayıcı hız hesapları başarılı yanıtları, gerçek bayt sayısını, geçen saniyeyi ve ondalık Mbps dönüşümünü kullanır. İndirme dosyası paketlenmiş `20MB.png` olur ve önbellekleme kapatılır.
- Yükleme istekleri multipart ek yükü dahil 32 MiB ile sınırlıdır. Sunucu kalıcı uygulama dosyası tutmadan tam bayt sayısını doğrular.
- Sunucu indirme hesabı tek bir ölçülen süreyi ve gerçekten alınan baytları kullanır. Sonuç şablonu repoya dahildir. Bu yollar çalışma zamanında denenmedi.
- Tarayıcı zamanlaması HTTP ve uygulama ek yükünü içerir. Yerel Flask sunucusu internet sağlayıcısının bant genişliğini değil yerel yolu ölçer.
- Sunucu ölçüm rotası harici aktarım hizmetlerine ve speedtest-cli kütüphanesine bağlıdır. Güncel erişilebilirlik, doğruluk ve tekrarlanabilirlik belirlenmedi.
- Kullanılmayan sistem ping yardımcısı platforma bağlı kalır. Çağrısında zaman aşımı ve sabit istek sayısı bulunur.

Ölçüm doğruluğu iddiasından önce kontrollü rota kontrolleri ve tekrarlanan aktarım ölçümleri hâlâ gereklidir.

## Proje yapısı

```text
app.py                 Flask rotaları ve sunucu aktarım deneyi
views.py               Ek sayfa rotaları
templates/index.html   Tarayıcı zamanlama arayüzü
templates/measure.html Sunucu aktarım sonuç ekranı
1MB.png, 5MB.png,
10MB.png, 20MB.png      Aktarım örnekleri
requirements.txt       Geçmiş bağımlılık sürümleri
```

## Geliştirme ve katkı

Önerilen değişikliğin tarayıcı mı, sunucu zamanlaması mı etkilediğini belirt. Hata bildirimlerine rota, HTTP durumu, beklenen dosya boyutu ve hesabı ekle. Yerel rota kontrolleriyle ağ ölçümlerini ayır. Sayfanın başarıyla açılması, ölçüm doğruluğunun kanıtı değildir.

## Lisans ve kaynaklar

[MIT lisansı](LICENSE) ile dağıtılır. Flask, Requests, speedtest-cli ve harici hizmetler kendi lisanslarına ve koşullarına tabidir.

<h1 align="center">Speedtest Final</h1>

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

**“Final” adı bu repoyu tanımlar ve doğrulanmış sürüm durumunu ifade etmez.** Mevcut uygulamada eksik rotalar ve hesaplama sorunları vardır. Kaynağı incelemek ve düzeltmeleri planlamak için kullanılabilir, ancak mevcut çıktılar doğrulanmış bant genişliği ölçümü değildir.

## Yerel arayüzü çalıştır

| Gereksinim | Amaç |
| --- | --- |
| pip ve venv içeren Python 3 | Yalıtılmış geliştirme ortamı |
| Flask, Requests ve speedtest-cli | Uygulamanın içe aktardığı bağımlılıklar |
| JavaScript destekli tarayıcı | Zamanlama arayüzü |

```text
git clone https://github.com/ArdaHFO/speedtestFinal.git
cd speedtestFinal
python -m venv .venv
```

Windows Komut İstemi'nde `.venv\Scripts\activate`, macOS/Linux'ta `source .venv/bin/activate` ile ortamı etkinleştir. Kayıtlı bağımlılıkları kur ve yerel önizlemeyi başlat.

```text
python -m pip install -r requirements.txt
python -m flask --app app run --host 127.0.0.1 --port 8000
```

[localhost:8000](http://127.0.0.1:8000) adresini aç. Flask CLI, betikteki tüm ağ arayüzlerini dinleyen debug başlatıcısı yerine önizlemeyi yerel arayüzde tutar. Bağımlılık sürümleri geçmiş geliştirme ortamına aittir ve güncel Python kurulumlarıyla uyumlulukları yeniden doğrulanmadı.

## Projede neler var?

- **Tarayıcı zamanlama arayüzü.** Ayrı kontroller indirme zamanlamasını, multipart yüklemeyi ve HTTP gidiş-dönüşünü örnekler.
- **Özel sunucu indirmesi.** `speed_test` işlevi, yapılandırılmış dosyayı harici bir uç noktadan akış halinde indirir ve alınan baytları izler.
- **Kütüphane karşılaştırması.** `POST /measure`, speedtest-cli ile yükleme ölçümü içerir ve ping sonucunu okur.
- **Flask blueprint yapısı.** Küçük `views.py` modülü ek sayfa rotaları sağlar.
- **Aktarım örnekleri.** Deneylerde kullanılabilecek çeşitli görsel dosyaları bulunur.

Sunucu kodu speedtest-cli kullanır. Önceki README'deki hazır ölçüm işlevlerinin kullanılmadığı iddiası, mevcut `app.py` dosyasını tanımlamaz.

## Tarayıcı ve sunucu yolları

| Bileşen | Amaçlanan eylem | Mevcut durum |
| --- | --- | --- |
| Tarayıcı indirmesi | Harici görseli getirip hız hesaplamak | Sabit boyut varsayımı ve yanlış Mbps dönüşümü |
| Tarayıcı yüklemesi | Dosyayı `POST /upload` adresine göndermek | Karşılık gelen sunucu rotası yok |
| Tarayıcı ping işlemi | `GET /ping` süresini ölçmek | Karşılık gelen sunucu rotası yok |
| `POST /measure` | 100 MB indirme ve kütüphane ile yükleme | Tanımsız değişken ve eksik sonuç şablonu |
| `GET /views/measure` | Sonuç şablonunu göstermek | Şablon yok |

Tarayıcıdaki HTTP zamanlamasıyla sunucudan başlayan aktarımlar farklı yolları ölçer. Uzak sunucuda üretilen sonuç sunucunun bağlantısını gösterir ve kullanıcının bağlantısını doğrudan temsil etmeyebilir.

## Doğrulama ve mevcut sınırlar

Python kodu, şablonlar, rotalar ve bağımlılık dosyası incelendi. Harici aktarım, hız ölçümü veya çalışma zamanı entegrasyon testi yapılmadı.

- `speed_test`, tanımlanmamış olan `startP` değişkenini kullanır.
- İki sonuç rotası da repoda bulunmayan `templates/measure.html` dosyasını ister.
- Tarayıcıdaki yükleme ve ping kontrolleri uygulanmamış uç noktaları çağırır. JavaScript süre sonucunu göstermeden önce HTTP başarısını denetlemez.
- Değerlerin Mbps olarak sunulabilmesi için dosya boyutu varsayımları, süre dönüşümü ve bayttan bite dönüşüm düzeltilmelidir.
- Uzak görsel ve aktarım hizmeti harici bağımlılıklardır. Erişilebilirlikleri ve farklı kaynaktan erişim davranışları doğrulanmadı.
- Kullanılmayan sistem ping yardımcısı platforma bağlıdır. Sunucunun ana başlatıcısı tüm arayüzlerde debug modunu açar. Yukarıdaki yerel önizleme komutunu kullan.

Bunlar mevcut kaynağın sınırlarıdır. Bu belge güncellemesi uygulamayı değiştirmez. Önce rota ve şablon akışını tamamlamak, ardından internet bağlantısını ölçmeden kontrollü örneklerle birimleri ve gerçek bayt sayılarını doğrulamak yararlı olacaktır.

## Proje yapısı

```text
app.py                 Flask rotaları ve sunucu aktarım deneyi
views.py               Ek sayfa rotaları
templates/index.html   Tarayıcı zamanlama arayüzü
1MB.png, 5MB.png,
10MB.png, 20MB.png      Aktarım örnekleri
requirements.txt       Geçmiş bağımlılık sürümleri
```

## Geliştirme ve katkı

Önerilen değişikliğin tarayıcı mı, sunucu zamanlaması mı etkilediğini belirt. Hata bildirimlerine rota, HTTP durumu, beklenen dosya boyutu ve hesabı ekle. Yerel rota kontrolleriyle ağ ölçümlerini ayır. Sayfanın başarıyla açılması, ölçüm doğruluğunun kanıtı değildir.

## Lisans ve kaynaklar

[MIT lisansı](LICENSE) ile dağıtılır. Flask, Requests, speedtest-cli ve harici hizmetler kendi lisanslarına ve koşullarına tabidir.


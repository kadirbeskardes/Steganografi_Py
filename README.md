# 🔐 Steganografi_Py - Görüntü ve Metin Gizleme Aracı

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Cryptography-E91E63?style=for-the-badge" alt="Cryptography"/>
  <img src="https://img.shields.io/badge/Steganography-9C27B0?style=for-the-badge" alt="Steganography"/>
  <img src="https://img.shields.io/badge/Image%20Processing-4CAF50?style=for-the-badge" alt="Image Processing"/>
</p>

**Steganografi_Py**, görüntü verileri üzerine başka görüntü verileri ve metin verileri saklamayı amaçlayan bir güvenlik uygulamasıdır.  Verinin güvenliğini artırmak için şifreleme algoritmaları kullanılmaktadır.  Metin verileri için **Blowfish** şifreleme algoritması, resim verileri için ise **Sezar şifrelemesi** algoritması kullanılmıştır.

## 📋 İçindekiler

- [Özellikler](#-özellikler)
- [Steganografi Nedir?](#-steganografi-nedir)
- [Kullanılan Algoritmalar](#-kullanılan-algoritmalar)
- [Kurulum](#-kurulum)
- [Kullanım](#-kullanım)
- [Teknik Detaylar](#-teknik-detaylar)
- [Katkıda Bulunma](#-katkıda-bulunma)

## ✨ Özellikler

- 🖼️ **Görüntü İçinde Görüntü Gizleme**:  Bir resmin içine başka bir resmi saklama
- 📝 **Görüntü İçinde Metin Gizleme**:  Resimlerin içine gizli mesajlar yerleştirme
- 🔒 **Blowfish Şifreleme**:  Metin verileri için güçlü simetrik şifreleme
- 🔑 **Sezar Şifrelemesi**: Görüntü verileri için klasik şifreleme
- 🔓 **Şifre Çözme**: Gizlenmiş verileri geri çıkarma
- 🖥️ **Kullanıcı Dostu**: Kolay kullanılabilir arayüz

## 🎭 Steganografi Nedir?

Steganografi, bir veriyi başka bir veri içinde gizleme sanatıdır. Kriptografiden farklı olarak, steganografi verinin varlığını gizlemeyi amaçlar. 

```
┌─────────────────────────────────────────────────────────────┐
│                    STEGANOGRAFİ                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Taşıyıcı Görüntü    +    Gizli Veri    =    Stego Görüntü │
│                                                             │
│   ┌─────────────┐      ┌───────────┐      ┌─────────────┐   │
│   │  🖼️ Normal  │   +  │ 📝 Mesaj  │  =   │ 🖼️ Normal   │   │
│   │   Görüntü   │      │   veya    │      │  Görünen    │   │
│   │             │      │ 🖼️ Resim  │      │ (Gizli içe- │   │
│   │             │      │           │      │  rikli)     │   │
│   └─────────────┘      └───────────┘      └─────────────┘   │
│                                                             │
│   İnsan gözü farkı algılayamaz!  👁️                          │
└─────────────────────────────────────────────────────────────┘
```

## 🔐 Kullanılan Algoritmalar

### 1. LSB (Least Significant Bit) Steganografisi

Görüntünün her pikselinin en az anlamlı bitlerini değiştirerek veri gizleme:

```
Orijinal Piksel:  11010110  10101011  11001100
                        ↓         ↓         ↓
Gizli Veri Bitleri:      1         0         1
                        ↓         ↓         ↓
Yeni Piksel:      11010111  10101010  11001101
```

### 2. Blowfish Şifreleme (Metin için)

- **Tip**: Simetrik blok şifreleme
- **Blok Boyutu**: 64 bit
- **Anahtar Uzunluğu**: 32-448 bit
- **Güvenlik**:  Yüksek güvenlikli, hızlı performans

```
┌──────────────┐     ┌─────────────┐     ┌──────────────┐
│  Düz Metin   │ ──► │  Blowfish   │ ──► │ Şifreli Metin│
│  "Merhaba"   │     │  + Anahtar  │     │  "x9#kL..."  │
└──────────────┘     └─────────────┘     └──────────────┘
```

### 3. Sezar Şifrelemesi (Görüntü için)

Piksel değerlerini belirli bir miktar kaydırarak şifreleme:

```
Orijinal Piksel Değeri:  150
Kaydırma Miktarı:        +25
Şifreli Piksel Değeri:  175
```

## 🚀 Kurulum

### Gereksinimler
- Python 3.8+
- Pillow (PIL)
- PyCryptodome

### Adımlar

```bash
# Repository'yi klonlayın
git clone https://github.com/kadirbeskardes/Steganografi_Py.git
cd Steganografi_Py

# Bağımlılıkları yükleyin
pip install pillow pycryptodome numpy
```

## 📖 Kullanım

### Veri Gizleme (Şifreleme)

```bash
python Sifrele.py
```

**İşlem Adımları:**
1. Taşıyıcı görüntüyü seçin
2. Gizlenecek veri tipini seçin (metin veya görüntü)
3. Gizlenecek veriyi girin/seçin
4. Şifreleme anahtarını belirleyin
5. Çıktı dosyasını kaydedin

### Veri Çıkarma (Şifre Çözme)

```bash
python SifreCoz.py
```

**İşlem Adımları:**
1. Stego görüntüyü seçin
2. Şifre çözme anahtarını girin
3. Gizli veriyi görüntüleyin/kaydedin

## 📁 Proje Yapısı

```
Steganografi_Py/
├── Sifrele.py           # Şifreleme ve gizleme modülü
├── SifreCoz.py          # Şifre çözme ve çıkarma modülü
└── README.md            # Dokümantasyon
```

## 🔧 Teknik Detaylar

### Sifrele.py Modülü

| Fonksiyon | Açıklama |
|-----------|----------|
| `text_to_binary()` | Metni binary formata çevirir |
| `encrypt_blowfish()` | Blowfish ile metin şifreler |
| `caesar_cipher_image()` | Görüntüye Sezar şifrelemesi uygular |
| `embed_data()` | Veriyi görüntüye gömer |
| `save_stego_image()` | Stego görüntüyü kaydeder |

### SifreCoz.py Modülü

| Fonksiyon | Açıklama |
|-----------|----------|
| `extract_data()` | Gizli veriyi çıkarır |
| `decrypt_blowfish()` | Blowfish şifresini çözer |
| `caesar_decipher_image()` | Sezar şifresini çözer |
| `binary_to_text()` | Binary'yi metne çevirir |

### Kapasite Hesaplama

```
Gizlenebilecek Veri Miktarı = (Genişlik × Yükseklik × 3) / 8 byte

Örnek:  1920×1080 görüntü
Kapasite = (1920 × 1080 × 3) / 8 = 777,600 byte ≈ 759 KB
```

## ⚠️ Güvenlik Notları

- 🔑 Güçlü ve benzersiz şifreleme anahtarları kullanın
- 📁 Orijinal görüntüleri güvenli bir yerde saklayın
- 🖼️ Yüksek çözünürlüklü görüntüler daha fazla veri gizleyebilir
- 📊 Sıkıştırmalı formatlar (JPEG) veri kaybına neden olabilir, PNG tercih edin

## 🎯 Kullanım Alanları

- 🔒 **Gizli İletişim**: Güvenli mesaj iletimi
- ©️ **Dijital Filigran**: Telif hakkı koruma
- 🆔 **Kimlik Doğrulama**: Belge doğrulama
- 🎓 **Eğitim**: Kriptografi ve steganografi öğrenimi

## 🤝 Katkıda Bulunma

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/NewFeature`)
3. Commit edin (`git commit -m 'Add NewFeature'`)
4. Push edin (`git push origin feature/NewFeature`)
5. Pull Request açın

## 📚 Referanslar

- [Steganography - Wikipedia](https://en.wikipedia.org/wiki/Steganography)
- [Blowfish Cipher](https://en.wikipedia.org/wiki/Blowfish_(cipher))
- [LSB Steganography](https://en.wikipedia.org/wiki/Bit_numbering#Least_significant_bit)

## ⚖️ Yasal Uyarı

Bu yazılım yalnızca eğitim ve yasal amaçlar için tasarlanmıştır.  Yasadışı faaliyetlerde kullanılması kesinlikle yasaktır. 

## 📄 Lisans

MIT License

---

<p align="center">
  🔐 <strong>Steganografi_Py</strong> - Görünmez güvenlik!
</p>

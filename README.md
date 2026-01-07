# 🔐 Steganografi_Py

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-FF6F00?style=for-the-badge)
![Blowfish](https://img.shields.io/badge/Blowfish-Encryption-E91E63?style=for-the-badge)
![PIL](https://img.shields.io/badge/Pillow-Image_Processing-4CAF50?style=for-the-badge)
![NumPy](https://img.shields.io/badge/NumPy-Analysis-013243?style=for-the-badge&logo=numpy)

**Görüntü tabanlı steganografi ve kriptografi uygulaması**

*Metin ve görüntü verilerini resimler içinde güvenli bir şekilde gizleyin*

</div>

---

## 📖 İçindekiler

- [Proje Hakkında](#-proje-hakkında)
- [Özellikler](#-özellikler)
- [Proje Yapısı](#-proje-yapısı)
- [Teknik Detaylar](#-teknik-detaylar)
  - [Sifrele.py Modülü](#sifrelepy-modülü)
  - [SifreCoz.py Modülü](#sifrecozpy-modülü)
- [Kullanılan Algoritmalar](#-kullanılan-algoritmalar)
- [Kurulum](#-kurulum)
- [Kullanım Kılavuzu](#-kullanım-kılavuzu)
- [Bağımlılıklar](#-bağımlılıklar)
- [Görüntü Kalite Metrikleri](#-görüntü-kalite-metrikleri)

---

## 🎯 Proje Hakkında

**Steganografi_Py**, Python programlama dili ile geliştirilmiş kapsamlı bir steganografi uygulamasıdır. Bu uygulama, kullanıcıların metin veya görüntü verilerini başka bir görüntü dosyasının içine gizlemesine olanak tanır. Proje, iki ana modülden oluşmaktadır:

1. **Sifrele.py** - Veri gizleme (şifreleme) işlemleri
2. **SifreCoz.py** - Gizli veri çıkarma (şifre çözme) işlemleri

Uygulama, güvenliği artırmak için **Blowfish** şifreleme algoritmasını kullanmakta ve kullanıcı dostu bir **Tkinter** grafik arayüzü sunmaktadır.

---

## ✨ Özellikler

### 🖼️ Veri Gizleme Özellikleri
- **Metin Gizleme**: Metin verilerini görüntü dosyalarının içine gömme
- **Görüntü Gizleme**: Küçük bir resmi büyük bir resmin içine saklama
- **Otomatik Anahtar Üretimi**: Rastgele 16 byte şifreleme anahtarı oluşturma
- **Manuel Anahtar Belirleme**: Kullanıcının kendi şifreleme anahtarını belirleyebilmesi

### 🔓 Veri Çıkarma Özellikleri
- **Metin Çözme**: Gizlenmiş metni görüntüden geri çıkarma
- **Görüntü Çözme**: Gizlenmiş resmi 50x50 piksel formatında geri oluşturma
- **Blowfish Şifre Çözme**: Şifrelenmiş verilerin güvenli şekilde çözümlenmesi

### 📊 Kalite Analizi
- **PSNR Hesaplama**: Peak Signal-to-Noise Ratio değerinin hesaplanması
- **SSIM Hesaplama**: Structural Similarity Index değerinin hesaplanması

### 🖥️ Kullanıcı Arayüzü
- Tkinter tabanlı grafiksel kullanıcı arayüzü
- Radyo butonları ile gömme türü seçimi (Metin/Resim)
- Dosya seçim diyalogları
- Hata mesajları ve bilgilendirme pencereleri

---

## 📁 Proje Yapısı

```
Steganografi_Py/
│
├── Sifrele.py          # Şifreleme ve veri gizleme modülü
├── SifreCoz.py         # Şifre çözme ve veri çıkarma modülü
└── README.md           # Proje dokümantasyonu
```

---

## 🔧 Teknik Detaylar

### Sifrele.py Modülü

Bu modül, `SteganografiApp` sınıfını içerir ve aşağıdaki ana fonksiyonları barındırır:

#### Sınıf: `SteganografiApp`

| Metod | Açıklama |
|-------|----------|
| `__init__(ana_pencere)` | Uygulama penceresini başlatır, değişkenleri tanımlar |
| `blowfish_sifrele(anahtar, metin)` | Blowfish algoritması ile metin şifreler |
| `arayuzu_olustur()` | Tkinter GUI bileşenlerini oluşturur |
| `secim_yazdir()` | Anahtar belirleme seçeneğini yönetir |
| `secenekleri_degistir()` | Metin/Resim seçimine göre arayüzü günceller |
| `kucuk_resim_sec()` | Küçük resim dosyası seçim diyaloğu |
| `rasgele_metin()` | 8 karakterlik rastgele metin üretir |
| `resim_sec()` | Ana resim dosyası seçim diyaloğu |
| `psnr_hesapla(orijinal, gomulu)` | PSNR değerini hesaplar |
| `ssim_hesapla(orijinal, gomulu)` | SSIM değerini hesaplar |
| `metin_gom(orijinal_resim, metin)` | LSB yöntemiyle metni resme gömer |
| `sifreleme()` | Ana şifreleme işlemini gerçekleştirir |

#### Metin Gömme Algoritması (LSB)

```python
def metin_gom(self, orijinal_resim, metin):
    # Metni binary formata çevir
    binary_metin = ''.join(format(ord(i), '08b') for i in metin)
    
    # Her pikselin en az anlamlı bitlerini değiştir
    for pixel in orijinal_pixel_verileri:
        yeni_pixel = list(pixel)
        for i in range(len(pixel)):
            if metin_index < len(binary_metin):
                yeni_pixel[i] = (yeni_pixel[i] & ~1) | int(binary_metin[metin_index])
                metin_index += 1
```

#### Blowfish Şifreleme

```python
def blowfish_sifrele(self, anahtar, metin):
    cipher = Blowfish.new(anahtar, Blowfish.MODE_ECB)
    sifreli_metin = cipher.encrypt(pad(metin.encode('utf-8'), Blowfish.block_size))
    return binascii.hexlify(sifreli_metin).decode('utf-8')
```

---

### SifreCoz.py Modülü

Bu modül, `SteganografiCozucuApp` sınıfını içerir ve gizlenmiş verileri çıkarmak için kullanılır:

#### Sınıf: `SteganografiCozucuApp`

| Metod | Açıklama |
|-------|----------|
| `__init__(ana_pencere)` | Çözücü penceresini başlatır |
| `arayuzu_olustur()` | Çözücü arayüzünü oluşturur |
| `secim_yazdir()` | Anahtar giriş alanlarını gösterir/gizler |
| `secenek_goster()` | Metin/Resim seçimine göre arayüzü günceller |
| `resim_sec()` | Şifreli resim dosyası seçimi |
| `cozumleme()` | Seçilen türe göre çözme işlemini başlatır |
| `resim_coz()` | Gömülü resmi çıkarır ve gösterir |
| `metin_coz()` | Gömülü metni çıkarır ve görüntüler |
| `blowfish_sifre_coz(anahtar, sifreli_metin)` | Blowfish şifresini çözer |

#### Metin Çözme Algoritması

```python
def metin_coz(self):
    # Pikselden anahtar değerlerini oku
    r, g, b = pixels[0, 0]
    shiftX = r & 0b111  # Son 3 bit
    shiftY = g & 0b111  # Son 3 bit
    
    # Zigzag pattern ile pikselleri oku
    while True:
        # 2x2 piksel bloğundan 12 bit oku
        for k in range(2):
            for j in range(2):
                r, g, b = pixels[indisX + k, indisY + j]
                bit.append(r & 1)
                bit.append(g & 1)
                bit.append(b & 1)
```

#### Resim Çözme Algoritması

```python
def resim_coz(self):
    # İlk pikselden parametreleri çıkar
    r, g, b = pixels[0, 0]
    shiftX = r & 0b111
    shiftY = g & 0b111
    anahtar = b & 0b1111
    
    # Gömülü resmi 50x50 boyutunda yeniden oluştur
    small_img_array = np.array(flat_array).reshape((50, 50, 3))
    small_img = Image.fromarray(small_img_array.astype('uint8'), 'RGB')
```

---

## 🔐 Kullanılan Algoritmalar

### 1. LSB (Least Significant Bit) Steganografisi

LSB steganografisi, görüntünün her pikselinin en az anlamlı bitlerini kullanarak veri gizleme yöntemidir.

```
┌─────────────────────────────────────────────────────────┐
│                    LSB Algoritması                       │
├─────────────────────────────────────────────────────────┤
│                                                          │
│   Orijinal Piksel (RGB):                                 │
│   R: 11010110  G: 10101011  B: 11001100                  │
│           ↓          ↓          ↓                        │
│   Gizli Veri Bitleri: 1, 0, 1                            │
│           ↓          ↓          ↓                        │
│   Yeni Piksel:                                           │
│   R: 11010111  G: 10101010  B: 11001101                  │
│                                                          │
│   Değişim: Sadece son bit → Görsel fark yok!            │
└─────────────────────────────────────────────────────────┘
```

### 2. Blowfish Şifreleme Algoritması

Projede metin verilerinin güvenliği için Blowfish simetrik şifreleme algoritması kullanılmaktadır:

- **Mod**: ECB (Electronic Codebook)
- **Blok Boyutu**: 64 bit (8 byte)
- **Anahtar Uzunluğu**: 32-448 bit arası değişken
- **Padding**: PKCS7 padding kullanılır

```
┌──────────────┐     ┌─────────────────┐     ┌──────────────┐
│              │     │                 │     │              │
│  Düz Metin   │────►│    Blowfish     │────►│ Şifreli Hex  │
│  "Merhaba"   │     │  + Anahtar Key  │     │ "a3f2c1..."  │
│              │     │                 │     │              │
└──────────────┘     └─────────────────┘     └──────────────┘
```

### 3. Zigzag Tarama Algoritması

Resim gömme işleminde zigzag pattern kullanılarak piksel konumları belirlenir:

```
┌─────────────────────────────────────┐
│         Zigzag Tarama               │
├─────────────────────────────────────┤
│                                     │
│   → → → ↓                           │
│   ↓ ← ← ←                           │
│   → → → ↓                           │
│   ↓ ← ← ←                           │
│                                     │
│   ShiftX ve ShiftY ile adım boyutu  │
│   belirlenir                        │
└─────────────────────────────────────┘
```

---

## 📥 Kurulum

### Gereksinimler

- Python 3.6 veya üzeri
- pip (Python paket yöneticisi)

### Adım 1: Projeyi İndirin

```bash
git clone https://github.com/kullanici/Steganografi_Py.git
cd Steganografi_Py
```

### Adım 2: Bağımlılıkları Yükleyin

```bash
pip install Pillow
pip install numpy
pip install scikit-image
pip install pycryptodome
```

### Tek Komutla Kurulum

```bash
pip install Pillow numpy scikit-image pycryptodome
```

---

## 📚 Kullanım Kılavuzu

### 🔒 Şifreleme (Veri Gizleme)

#### Şifreleme Uygulamasını Başlatma

```bash
python Sifrele.py
```

#### Metin Gizleme Adımları

1. **Gömme Türü Seçimi**: "Metin" radyo butonunu seçin
2. **Resim Seçimi**: "Resim Seç" butonuna tıklayın ve taşıyıcı resmi seçin
3. **Metin Girişi**: Gizlemek istediğiniz metni metin kutusuna yazın
4. **Anahtar Seçeneği** (Opsiyonel):
   - "Anahtarları kendim belirlemek istiyorum" seçeneğini işaretleyin
   - Şifreleme anahtarını girin
   - KaydırmaX ve KaydırmaY değerlerini girin
5. **Şifreleme**: "Şifrele ve Göster" butonuna tıklayın
6. **Sonuç**: Gömülü resim görüntülenir, PSNR ve SSIM değerleri gösterilir

#### Resim Gizleme Adımları

1. **Gömme Türü Seçimi**: "Resim" radyo butonunu seçin
2. **Küçük Resim Seçimi**: "Küçük Resim Seç" butonuyla gizlenecek resmi seçin
3. **Ana Resim Seçimi**: "Resim Seç" butonuyla taşıyıcı resmi seçin
4. **Anahtar Seçeneği** (Opsiyonel):
   - Manuel anahtar belirlemek için checkbox'ı işaretleyin
   - KaydırmaX ve KaydırmaY koordinatlarını girin
5. **Şifreleme**: "Şifrele ve Göster" butonuna tıklayın

---

### 🔓 Şifre Çözme (Veri Çıkarma)

#### Şifre Çözme Uygulamasını Başlatma

```bash
python SifreCoz.py
```

#### Metin Çıkarma Adımları

1. **Çözme Türü Seçimi**: "Metin" radyo butonunu seçin
2. **Resim Seçimi**: "Resim Seç" butonuyla şifreli resmi seçin
3. **Anahtar Girişi** (Gerekirse):
   - "Anahtarları kendim belirlemek istiyorum" seçeneğini işaretleyin
   - Şifreleme anahtarını ve kaydırma değerlerini girin
4. **Çözme**: "Geri çıkar" butonuna tıklayın
5. **Sonuç**: Gizli metin metin kutusunda görüntülenir

#### Resim Çıkarma Adımları

1. **Çözme Türü Seçimi**: "Resim" radyo butonunu seçin
2. **Resim Seçimi**: Şifreli resim dosyasını seçin
3. **Anahtar Girişi** (Gerekirse):
   - Şifreleme anahtarını, KaydırmaX ve KaydırmaY değerlerini girin
4. **Çözme**: "Geri çıkar" butonuna tıklayın
5. **Sonuç**: 50x50 piksel boyutunda çıkarılmış resim gösterilir

---

## 📦 Bağımlılıklar

| Kütüphane | Versiyon | Kullanım Amacı |
|-----------|----------|----------------|
| `tkinter` | Dahili | Grafik kullanıcı arayüzü |
| `Pillow (PIL)` | ≥ 8.0 | Görüntü işleme ve manipülasyonu |
| `numpy` | ≥ 1.19 | Sayısal hesaplamalar ve dizi işlemleri |
| `scikit-image` | ≥ 0.18 | SSIM hesaplama |
| `pycryptodome` | ≥ 3.10 | Blowfish şifreleme algoritması |

### İçe Aktarılan Modüller

```python
# Sifrele.py
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os
import random
import numpy as np
from skimage.metrics import structural_similarity as ssim
import locale
from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
import binascii
import string

# SifreCoz.py
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import numpy as np
from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import unpad
import binascii
```

---

## 📊 Görüntü Kalite Metrikleri

### PSNR (Peak Signal-to-Noise Ratio)

PSNR, orijinal görüntü ile işlenmiş görüntü arasındaki kalite farkını ölçer.

```python
def psnr_hesapla(self, orijinal_resim, gomulu_resim):
    orijinal_dizi = np.array(orijinal_resim).astype('float')
    gomulu_dizi = np.array(gomulu_resim).astype('float')
    
    fark = orijinal_dizi - gomulu_dizi
    mse = np.mean(fark ** 2)
    
    maksimum_pixel = 255.0
    psnr = 20 * np.log10(maksimum_pixel / np.sqrt(mse))
    
    return psnr
```

| PSNR Değeri | Kalite Durumu |
|-------------|---------------|
| > 40 dB | Mükemmel kalite |
| 30-40 dB | İyi kalite |
| 20-30 dB | Kabul edilebilir |
| < 20 dB | Düşük kalite |

### SSIM (Structural Similarity Index)

SSIM, insan görsel algısına dayalı yapısal benzerliği ölçer.

```python
def ssim_hesapla(self, orijinal_resim, gomulu_resim):
    orijinal_dizi = np.array(orijinal_resim).astype('float')
    gomulu_dizi = np.array(gomulu_resim).astype('float')
    return ssim(orijinal_dizi, gomulu_dizi, multichannel=True)
```

| SSIM Değeri | Benzerlik |
|-------------|-----------|
| 1.0 | Özdeş görüntüler |
| > 0.95 | Çok yüksek benzerlik |
| 0.80-0.95 | Yüksek benzerlik |
| < 0.80 | Belirgin farklar |

---

## 🎨 Arayüz Görseli

```
┌─────────────────────────────────────────────────────────┐
│              Steganografi Uygulaması                     │
├─────────────────────────────────────────────────────────┤
│                                                          │
│    ○ Metin    ○ Resim                                   │
│                                                          │
│    Resim Yolu: [________________________] [Resim Seç]   │
│                                                          │
│    Metin: [________________________________]            │
│                                                          │
│    □ Anahtarları kendim belirlemek istiyorum            │
│                                                          │
│    Şifreleme Anahtarı: [________]                       │
│    KaydırmaX: [____]  KaydırmaY: [____]                 │
│                                                          │
│              [Şifrele ve Göster]                        │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## ⚠️ Önemli Notlar

1. **Dosya Formatı**: Uygulama PNG ve BMP gibi kayıpsız formatlarla en iyi sonucu verir
2. **Anahtar Güvenliği**: Şifreleme anahtarını güvenli bir yerde saklayın
3. **Resim Boyutu**: Gizlenecek verinin boyutu, taşıyıcı resmin kapasitesini aşmamalıdır
4. **Yerel Ayarlar**: Türkçe karakter desteği için `locale` ayarları yapılandırılmıştır

---

## 🛠️ Geliştirici Bilgileri

### Dosya Satır Sayıları

| Dosya | Satır Sayısı |
|-------|--------------|
| Sifrele.py | 301 satır |
| SifreCoz.py | 264 satır |

### Kullanılan Programlama Paradigmaları

- **Nesne Yönelimli Programlama (OOP)**: Her modül bir sınıf içerir
- **Event-Driven Programming**: Tkinter GUI olayları ile yönetim
- **Modüler Tasarım**: Şifreleme ve çözme ayrı modüllerde

---

<div align="center">

**🔐 Steganografi_Py - Verilerinizi Görünmez Kılın 🔐**

*Python ile güvenli steganografi çözümü*

</div>

# -*- coding: utf-8 -*-
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

class SteganografiApp:
    def __init__(self, ana_pencere):
        # Dil ve yerel ayarları Türkçe olarak ayarla
        locale.setlocale(locale.LC_ALL, 'tr_TR.utf8')
        self.ana_pencere = ana_pencere
        self.ana_pencere.title("Steganografi Uygulaması")
        self.secilen_resim_yolu = tk.StringVar()
        self.secilen_kucuk_resim_yolu = tk.StringVar()
        self.gomme_turu = tk.StringVar(value="Metin")
        self.anahtar_turu = tk.BooleanVar()
        self.arayuzu_olustur()

    def blowfish_sifrele(self, anahtar, metin):
        # Blowfish şifreleme fonksiyonu
        cipher = Blowfish.new(anahtar, Blowfish.MODE_ECB)
        sifreli_metin = cipher.encrypt(pad(metin.encode('utf-8'), Blowfish.block_size))
        return binascii.hexlify(sifreli_metin).decode('utf-8')

    def arayuzu_olustur(self):
        # Metin ve resim seçimi için radyo butonları ekle
        self.secenekler_cerceve = tk.Frame(self.ana_pencere)
        self.metin_secimi = tk.Radiobutton(self.secenekler_cerceve, text="Metin", variable=self.gomme_turu, value="Metin",
                                           command=self.secenekleri_degistir)
        self.metin_secimi.pack(side="left")
        self.resim_secimi = tk.Radiobutton(self.secenekler_cerceve, text="Resim", variable=self.gomme_turu, value="Resim",
                                           command=self.secenekleri_degistir)
        self.resim_secimi.pack(side="left")
        self.secenekler_cerceve.pack(side="top", pady=10)

        # Küçük resim seçimi için widgetlar ekle
        self.kucuk_resim_cerceve = tk.Frame(self.ana_pencere)
        self.kucuk_resim_etiket = tk.Label(self.kucuk_resim_cerceve, text="Küçük Resim Yolu:", bg='#f0f0f0')
        self.kucuk_resim_etiket.pack(side="left", fill="x", padx=10, pady=5)
        self.kucuk_resim_yol_giris = tk.Entry(self.kucuk_resim_cerceve, textvariable=self.secilen_kucuk_resim_yolu,
                                              width=50)
        self.kucuk_resim_yol_giris.pack(side="left", fill="x", padx=10, pady=5)
        self.kucuk_resim_sec_btn = tk.Button(self.kucuk_resim_cerceve, text="Küçük Resim Seç",
                                             command=self.kucuk_resim_sec)
        self.kucuk_resim_sec_btn.pack(side="left", fill="x", padx=10, pady=5)
        self.kucuk_resim_cerceve.pack(side="top")

        # Büyük resim seçimi için widgetlar ekle
        self.resim_cerceve = tk.Frame(self.ana_pencere)
        self.resim_etiket = tk.Label(self.resim_cerceve, text="Resim Yolu:", bg='#f0f0f0')
        self.resim_etiket.pack(side="left", fill="x", padx=10, pady=5)
        self.resim_yol_giris = tk.Entry(self.resim_cerceve, textvariable=self.secilen_resim_yolu, width=50)
        self.resim_yol_giris.pack(side="left", fill="x", padx=10, pady=5)
        self.resim_sec_btn = tk.Button(self.resim_cerceve, text="Resim Seç", command=self.resim_sec)
        self.resim_sec_btn.pack(side="left", fill="x", padx=10, pady=5)
        self.resim_cerceve.pack(side="top")

        # Metin girişi için widgetlar ekle
        self.metin_cerceve = tk.Frame(self.ana_pencere)
        self.metin_etiket = tk.Label(self.metin_cerceve, text="Metin:", bg='#f0f0f0')
        self.metin_etiket.pack(side="left", fill="x", padx=10, pady=5)
        self.metin_giris = tk.Entry(self.metin_cerceve, width=38, font=("Arial", 12))
        self.metin_giris.pack(side="left", fill="x", padx=10, pady=5)
        self.metin_cerceve.pack(side="top")

        # Anahtar türü seçimi için onay kutusu ekle
        self.c1 = tk.Checkbutton(self.ana_pencere, text='Anahtarları kendim belirlemek istiyorum', variable=self.anahtar_turu, onvalue=1, offvalue=0, command=self.secim_yazdir)
        self.c1.pack(side="top")

        # Şifreleme anahtarı ve kaydırma girişleri için widgetlar ekle
        self.giris_cerceve = tk.Frame(self.ana_pencere)
        lb = tk.Label(self.giris_cerceve, text="Şifreleme Anahtarı:")
        lb1 = tk.Label(self.giris_cerceve, text="KaydırmaX:")
        lb2 = tk.Label(self.giris_cerceve, text="KaydırmaY:")
        self.sifreAnahtarGir = tk.Entry(self.giris_cerceve)
        self.kaydirmaXGir = tk.Entry(self.giris_cerceve)
        self.kaydirmaYGir = tk.Entry(self.giris_cerceve)
        lb.pack(side="left")
        self.sifreAnahtarGir.pack(side="left")
        lb1.pack(side="left")
        self.kaydirmaXGir.pack(side="left")
        lb2.pack(side="left")
        self.kaydirmaYGir.pack(side="left")
        self.calistir_btn = tk.Button(self.ana_pencere, text="Şifrele ve Göster", command=self.sifreleme)
        self.calistir_btn.pack(side="bottom", padx=10, pady=10)
        self.secenekleri_degistir()

    def secim_yazdir(self):
        # Anahtar türü seçimine göre uygun widgetları göster veya gizle
        if self.anahtar_turu.get():
            self.giris_cerceve.pack(side="bottom")
        else:
            self.giris_cerceve.pack_forget()

    def secenekleri_degistir(self):
        # Gömme türüne göre uygun widgetları göster veya gizle
        if self.gomme_turu.get() == "Metin":
            self.kucuk_resim_cerceve.pack_forget()
            self.metin_cerceve.pack(side="top")
            self.giris_cerceve.pack_forget()
            if self.anahtar_turu.get():
                self.giris_cerceve.pack(side="bottom")
            else:
                self.giris_cerceve.pack_forget()
        elif self.gomme_turu.get() == "Resim":
            self.metin_cerceve.pack_forget()
            self.kucuk_resim_cerceve.pack(side="top")
            self.giris_cerceve.pack_forget()
            if self.anahtar_turu.get():
                self.giris_cerceve.pack(side="bottom")
            else:
                self.giris_cerceve.pack_forget()

    def kucuk_resim_sec(self):
        # Küçük resim dosyası seç
        dosya_yolu = filedialog.askopenfilename()
        if dosya_yolu:
            self.secilen_kucuk_resim_yolu.set(dosya_yolu)

    def rasgele_metin(self):
        # Rasgele metin oluşturma fonksiyonu
        harfler = string.ascii_letters + string.digits  # ASCII harfleri ve rakamları kullan
        return ''.join(random.choice(harfler) for _ in range(8))

    def resim_sec(self):
        # Büyük resim dosyası seç
        dosya_yolu = filedialog.askopenfilename()
        if dosya_yolu:
            self.secilen_resim_yolu.set(dosya_yolu)

    def psnr_hesapla(self, orijinal_resim, gomulu_resim):
        # PSNR hesapla
        orijinal_dizi = np.array(orijinal_resim).astype('float')
        gomulu_dizi = np.array(gomulu_resim).astype('float')

        fark = orijinal_dizi - gomulu_dizi
        mse = np.mean(fark ** 2)

        maksimum_pixel = 255.0
        psnr = 20 * np.log10(maksimum_pixel / np.sqrt(mse))

        return psnr

    def ssim_hesapla(self, orijinal_resim, gomulu_resim):
        # SSIM hesapla
        orijinal_dizi = np.array(orijinal_resim).astype('float')
        gomulu_dizi = np.array(gomulu_resim).astype('float')
        return ssim(orijinal_dizi, gomulu_dizi, multichannel=True)

    def metin_gom(self, orijinal_resim, metin):
        # Metni resime gömme fonksiyonu
        binary_metin = ''.join(format(ord(i), '08b') for i in metin)
        resim_genislik, resim_yukseklik = orijinal_resim.size
        max_boyut = resim_genislik * resim_yukseklik

        if len(binary_metin) > max_boyut:
            raise ValueError("Metin resmin içine sığmıyor.")

        orijinal_pixel_verileri = list(orijinal_resim.getdata())
        gomulu_pixel_verileri = []

        metin_index = 0
        for pixel in orijinal_pixel_verileri:
            yeni_pixel = list(pixel)

            for i in range(len(pixel)):
                if metin_index < len(binary_metin):
                    yeni_pixel[i] = (yeni_pixel[i] & ~1) | int(binary_metin[metin_index])
                    metin_index += 1

            gomulu_pixel_verileri.append(tuple(yeni_pixel))

        gomulu_resim = Image.new(orijinal_resim.mode, orijinal_resim.size)
        gomulu_resim.putdata(gomulu_pixel_verileri)

        return gomulu_resim

    def sifreleme(self):
        # Şifreleme işlemi
        if self.anahtar_turu.get() == 1:
            sifre_anahtar = self.sifreAnahtarGir.get().encode()
            metin = self.metin_giris.get()

            if self.gomme_turu.get() == "Metin":
                if not metin:
                    messagebox.showerror("Hata", "Lütfen gömmek için bir metin giriniz.")
                    return

                sifreli_metin = self.blowfish_sifrele(sifre_anahtar, metin)
                resim_dosya_yolu = self.secilen_resim_yolu.get()

                if not resim_dosya_yolu:
                    messagebox.showerror("Hata", "Lütfen bir resim seçiniz.")
                    return

                orijinal_resim = Image.open(resim_dosya_yolu)
                gomulu_resim = self.metin_gom(orijinal_resim, sifreli_metin)

                gomulu_resim.show()

                psnr_degeri = self.psnr_hesapla(orijinal_resim, gomulu_resim)
                ssim_degeri = self.ssim_hesapla(orijinal_resim, gomulu_resim)

                messagebox.showinfo("Şifreleme Başarılı", f"PSNR: {psnr_degeri}\nSSIM: {ssim_degeri}")
            else:
                resim_dosya_yolu = self.secilen_resim_yolu.get()
                kucuk_resim_dosya_yolu = self.secilen_kucuk_resim_yolu.get()

                if not resim_dosya_yolu or not kucuk_resim_dosya_yolu:
                    messagebox.showerror("Hata", "Lütfen bir resim ve küçük resim seçiniz.")
                    return

                orijinal_resim = Image.open(resim_dosya_yolu)
                kucuk_resim = Image.open(kucuk_resim_dosya_yolu)

                kaydirmaX = int(self.kaydirmaXGir.get())
                kaydirmaY = int(self.kaydirmaYGir.get())

                orijinal_resim_copy = orijinal_resim.copy()

                for i in range(kucuk_resim.width):
                    for j in range(kucuk_resim.height):
                        if kaydirmaX + i < orijinal_resim.width and kaydirmaY + j < orijinal_resim.height:
                            r, g, b = kucuk_resim.getpixel((i, j))
                            orijinal_r, orijinal_g, orijinal_b = orijinal_resim.getpixel((kaydirmaX + i, kaydirmaY + j))
                            orijinal_resim_copy.putpixel((kaydirmaX + i, kaydirmaY + j), (r, g, b))

                orijinal_resim_copy.show()

                psnr_degeri = self.psnr_hesapla(orijinal_resim, orijinal_resim_copy)
                ssim_degeri = self.ssim_hesapla(orijinal_resim, orijinal_resim_copy)

                messagebox.showinfo("Şifreleme Başarılı", f"PSNR: {psnr_degeri}\nSSIM: {ssim_degeri}")
        else:
            sifre_anahtar = os.urandom(16)
            metin = self.metin_giris.get()

            if self.gomme_turu.get() == "Metin":
                if not metin:
                    messagebox.showerror("Hata", "Lütfen gömmek için bir metin giriniz.")
                    return

                sifreli_metin = self.blowfish_sifrele(sifre_anahtar, metin)
                resim_dosya_yolu = self.secilen_resim_yolu.get()

                if not resim_dosya_yolu:
                    messagebox.showerror("Hata", "Lütfen bir resim seçiniz.")
                    return

                orijinal_resim = Image.open(resim_dosya_yolu)
                gomulu_resim = self.metin_gom(orijinal_resim, sifreli_metin)

                gomulu_resim.show()

                psnr_degeri = self.psnr_hesapla(orijinal_resim, gomulu_resim)
                ssim_degeri = self.ssim_hesapla(orijinal_resim, gomulu_resim)

                messagebox.showinfo("Şifreleme Başarılı", f"PSNR: {psnr_degeri}\nSSIM: {ssim_degeri}")
            else:
                resim_dosya_yolu = self.secilen_resim_yolu.get()
                kucuk_resim_dosya_yolu = self.secilen_kucuk_resim_yolu.get()

                if not resim_dosya_yolu or not kucuk_resim_dosya_yolu:
                    messagebox.showerror("Hata", "Lütfen bir resim ve küçük resim seçiniz.")
                    return

                orijinal_resim = Image.open(resim_dosya_yolu)
                kucuk_resim = Image.open(kucuk_resim_dosya_yolu)

                kaydirmaX = random.randint(0, orijinal_resim.width - kucuk_resim.width)
                kaydirmaY = random.randint(0, orijinal_resim.height - kucuk_resim.height)

                orijinal_resim_copy = orijinal_resim.copy()

                for i in range(kucuk_resim.width):
                    for j in range(kaydirmaY, kucuk_resim.height):
                        if kaydirmaX + i < orijinal_resim.width and kaydirmaY + j < orijinal_resim.height:
                            r, g, b = kucuk_resim.getpixel((i, j))
                            orijinal_r, orijinal_g, orijinal_b = orijinal_resim.getpixel((kaydirmaX + i, kaydirmaY + j))
                            orijinal_resim_copy.putpixel((kaydirmaX + i, kaydirmaY + j), (r, g, b))

                orijinal_resim_copy.show()

                psnr_degeri = self.psnr_hesapla(orijinal_resim, orijinal_resim_copy)
                ssim_degeri = self.ssim_hesapla(orijinal_resim, orijinal_resim_copy)

                messagebox.showinfo("Şifreleme Başarılı", f"PSNR: {psnr_degeri}\nSSIM: {ssim_degeri}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SteganografiApp(root)
    root.mainloop()

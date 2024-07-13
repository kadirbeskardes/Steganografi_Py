import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import numpy as np
from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import unpad
import binascii


class SteganografiCozucuApp:
    def __init__(self, ana_pencere):
        self.ana_pencere = ana_pencere
        self.ana_pencere.title("Steganografi Çözücü")
        self.secilen_resim_yolu = tk.StringVar()
        self.gomme_turu = tk.StringVar(value="Metin")  # Radyo butonları için değişken
        self.anahtar_turu = tk.BooleanVar()  # Radyo butonları için değişken
        self.arayuzu_olustur()

    def arayuzu_olustur(self):
        # Seçenekler için çerçeve
        self.secenek_cerceve = tk.Frame(self.ana_pencere)
        self.secenek_cerceve.grid(row=0, column=0, columnspan=2, pady=10)

        # Metin veya resim çözme seçeneği radyo butonları
        self.radio_metin = tk.Radiobutton(self.secenek_cerceve, text="Metin", variable=self.gomme_turu, value="Metin",
                                          command=self.secenek_goster)
        self.radio_metin.grid(row=0, column=0)

        self.radio_resim = tk.Radiobutton(self.secenek_cerceve, text="Resim", variable=self.gomme_turu, value="Resim",
                                          command=self.secenek_goster)
        self.radio_resim.grid(row=0, column=1)

        # Resim seçme butonu
        self.resim_sec_btn = tk.Button(self.ana_pencere, text="Resim Seç", command=self.resim_sec)
        self.resim_sec_btn.grid(row=1, column=0, columnspan=2)

        # Anahtarları kendim belirlemek istiyorum seçeneği
        self.c1 = tk.Checkbutton(self.ana_pencere, text='Anahtarları kendim belirlemek istiyorum',
                                 variable=self.anahtar_turu,
                                 onvalue=1, offvalue=0, command=self.secim_yazdir)
        self.c1.grid(row=2, column=0, columnspan=2)

        # Giriş çerçevesi
        self.giris_cerceve = tk.Frame(self.ana_pencere)
        lb = tk.Label(self.giris_cerceve, text="Şifreleme Anahtarı:")
        lb1 = tk.Label(self.giris_cerceve, text="KaydirmaX:")
        lb2 = tk.Label(self.giris_cerceve, text="KaydirmaY:")
        self.sifreAnahtarGir = tk.Entry(self.giris_cerceve)
        self.kaydirmaXGir = tk.Entry(self.giris_cerceve)
        self.kaydirmaYGir = tk.Entry(self.giris_cerceve)
        lb.grid(row=0, column=0)
        lb1.grid(row=0, column=1)
        lb2.grid(row=0, column=2)

        self.sifreAnahtarGir.grid(row=1, column=0)
        self.kaydirmaXGir.grid(row=1, column=1)
        self.kaydirmaYGir.grid(row=1, column=2)

        self.giris_cerceve.grid(row=3, column=0, columnspan=2, pady=10)
        self.giris_cerceve.grid_forget()

        # Metin çerçevesi
        self.metin_cerceve = tk.Frame(self.ana_pencere)
        self.metin_cerceve.grid(row=4, column=0, columnspan=2)

        # Gizli metin etiketi ve metin kutusu
        self.metin_etiket = tk.Label(self.metin_cerceve, text="Gizli Metin:")
        self.metin_etiket.pack(side="top")
        self.metin_cikti = tk.Text(self.metin_cerceve, height=10, width=50)
        self.metin_cikti.pack(side="top")

        # Geri çıkarma butonu
        self.calistirBtn = tk.Button(self.ana_pencere, text="Geri çıkar", command=self.cozumleme)
        self.calistirBtn.grid(row=5, column=0, columnspan=2, pady=10)

    def secim_yazdir(self):
        # Anahtar belirleme seçeneğine göre uygun widgetları göster
        if self.anahtar_turu.get():
            self.giris_cerceve.grid(row=3, column=0, columnspan=2, pady=10)
        else:
            self.giris_cerceve.grid_forget()

    def secenek_goster(self):
        # Gömme türüne göre metin çerçevesini göster veya gizle
        if self.gomme_turu.get() == "Metin":
            self.metin_cerceve.grid(row=4, column=0, columnspan=2)
        else:
            self.metin_cerceve.grid_forget()

    def resim_sec(self):
        # Resim dosyasını seçme
        dosya_yolu = filedialog.askopenfilename()
        if dosya_yolu:
            self.secilen_resim_yolu.set(dosya_yolu)

    def cozumleme(self):
        # Gömme türüne göre çözümleme yap
        if self.gomme_turu.get() == "Metin":
            self.metin_coz()
        elif self.gomme_turu.get() == "Resim":
            self.resim_coz()

    def resim_coz(self):
        # Resimdeki gömülü resmi çözme
        tersX, tersY = False, False

        img = Image.open(self.secilen_resim_yolu.get())
        pixels = img.load()
        width, height = img.size
        anahtar = 0
        if self.anahtar_turu.get():
            try:
                shiftX = int(self.kaydirmaXGir.get())
                shiftY = int(self.kaydirmaYGir.get())
                anahtar = int(self.sifreAnahtarGir.get())
            except ValueError:
                messagebox.showerror("Hata", "Geçersiz anahtar değerleri. Lütfen tam sayı girin.")
                return
        else:
            r, g, b = pixels[0, 0]
            shiftX = r & 0b111
            shiftY = g & 0b111
            anahtar = b & 0b1111

        indisX, indisY = shiftX, shiftY
        flat_array = []
        while True:
            if indisX >= width or indisY >= height:
                break
            pixel = pixels[indisX, indisY]
            rgb = 0
            if pixel == (0, 0, 0):
                break
            bit = []
            for k in range(2):
                for j in range(2):
                    r, g, b = pixels[indisX + k, indisY + j]
                    bit.append(r & 1)
                    bit.append(g & 1)
                    bit.append(b & 1)
            for i in range(8):
                rgb |= (bit[i] << i)
            rgb = rgb - anahtar
            flat_array.append(rgb)
            if not tersX:
                indisX += shiftX
                if indisX + shiftX > width:
                    tersX = True
                    indisX -= shiftX
            else:
                indisX -= shiftX
                if indisX - shiftX < 0:
                    tersX = False
                    indisX += shiftX

            if not tersY:
                indisY += shiftY
                if indisY + shiftY > height:
                    tersY = True
                    indisY -= shiftY
            else:
                indisY -= shiftY
                if indisY - shiftY < 0:
                    tersY = False
                    indisY += shiftY

        small_img_array = np.array(flat_array).reshape((50, 50, 3))
        small_img = Image.fromarray(small_img_array.astype('uint8'), 'RGB')
        small_img.show()

    def metin_coz(self):
        # Resimdeki gömülü metni çözme
        tersX, tersY = False, False
        img = Image.open(self.secilen_resim_yolu.get())
        pixels = img.load()
        width, height = img.size

        mesaj = ''
        anahtar = ''
        r, g, b = pixels[0, 0]
        if self.anahtar_turu.get():
            try:
                shiftX = int(self.kaydirmaXGir.get())
                shiftY = int(self.kaydirmaYGir.get())
                anahtar = self.sifreAnahtarGir.get()
            except ValueError:
                messagebox.showerror("Hata", "Geçersiz anahtar değerleri. Lütfen tam sayı girin.")
                return
        else:
            shiftX = r & 0b111
            shiftY = g & 0b111

        indisX, indisY = shiftX, shiftY
        while True:
            if indisX >= width or indisY >= height:
                break
            pixel = pixels[indisX, indisY]
            if pixel == (0, 0, 0):
                break
            char_val = 0
            bit = []
            for k in range(2):
                for j in range(2):
                    r, g, b = pixels[indisX + k, indisY + j]
                    bit.append(r & 1)
                    bit.append(g & 1)
                    bit.append(b & 1)

            for i in range(12):
                char_val |= (bit[i] << i)

            mesaj += chr(char_val)
            if not tersX:
                indisX += shiftX
                if indisX + shiftX > width:
                    tersX = True
                    indisX -= shiftX
            else:
                indisX -= shiftX
                if indisX - shiftX < 0:
                    tersX = False
                    indisX += shiftX

            if not tersY:
                indisY += shiftY
                if indisY + shiftY > height:
                    tersY = True
                    indisY -= shiftY
            else:
                indisY -= shiftY
                if indisY - shiftY < 0:
                    tersY = False
                    indisY += shiftY

        # Anahtar seçeneğine göre Blowfish şifre çözme
        if self.anahtar_turu.get():
            byte_data = anahtar.encode('utf-8')
            sifresiz_mesaj = self.blowfish_sifre_coz(byte_data, mesaj)
        else:
            anahtar = mesaj[:8]
            byte_data = anahtar.encode('utf-8')
            metin = mesaj[8:]
            sifresiz_mesaj = self.blowfish_sifre_coz(byte_data, metin)

        # Gizli metni metin kutusuna yazma
        self.metin_cikti.delete('1.0', tk.END)
        self.metin_cikti.insert(tk.END, sifresiz_mesaj)

    def blowfish_sifre_coz(self, anahtar, sifreli_metin):
        # Blowfish şifre çözme fonksiyonu
        cipher = Blowfish.new(anahtar, Blowfish.MODE_ECB)
        sifreli_veri = binascii.unhexlify(sifreli_metin)
        sifresiz_veri = unpad(cipher.decrypt(sifreli_veri), Blowfish.block_size)
        return sifresiz_veri.decode('utf-8')


def main():
    root = tk.Tk()
    app = SteganografiCozucuApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
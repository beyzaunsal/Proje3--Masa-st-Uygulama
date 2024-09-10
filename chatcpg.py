import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
import sqlite3

def SifreOlustur():
    kullaniciAdi = "admin"
    sifre = "1234"
    with open("rehber.txt", "w") as dosya:
        dosya.write(f"{kullaniciAdi}{sifre}")

class AnaEkran(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ana Ekran")
        
        icerik = QVBoxLayout()
        self.ekle = QPushButton("Ekle")
        icerik.addWidget(self.ekle)

        self.listele = QPushButton("Listele")
        icerik.addWidget(self.listele)

        self.ara = QPushButton("Ara")
        icerik.addWidget(self.ara)

        self.sil = QPushButton("Sil")
        icerik.addWidget(self.sil)

        self.duzelt = QPushButton("Düzelt")
        icerik.addWidget(self.duzelt)

        self.ekle.clicked.connect(self.ekleKayit)
        self.listele.clicked.connect(self.listeleKayit)
        self.ara.clicked.connect(self.araKayit)
        self.sil.clicked.connect(self.silKayit)
        self.duzelt.clicked.connect(self.duzeltKayit)

        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

    def ekleKayit(self):
        self.ekleme = EkleEkrani("Kayıt Ekle")
        self.ekleme.show()

    def listeleKayit(self):
        self.listeleme = ListeleEkrani("Kayıt Listele")
        self.listeleme.show()

    def araKayit(self):
        self.arama = AramaEkrani("Kayıt Arama")
        self.arama.show()

    def silKayit(self):
        self.silme = SilmeEkrani("Kayıt Silme")  # Not: SilmeEkrani'yi tanımlamalısınız
        self.silme.show()

    def duzeltKayit(self):
        self.duzeltme = DuzeltmeEkrani("Kayıt Düzeltme")  # Not: DuzeltmeEkrani'yi tanımlamalısınız
        self.duzeltme.show()

class loginPenceresi(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Login Ekranı")
        icerik = QVBoxLayout()
        icerik.addWidget(QLabel('Kullanıcı adı:'))
        self.username = QLineEdit()
        icerik.addWidget(self.username)
        icerik.addWidget(QLabel('Şifre:'))
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        icerik.addWidget(self.password)
        self.ekle = QPushButton('Giriş yap')
        icerik.addWidget(self.ekle)

        self.ekle.clicked.connect(self.kontrolEt)
    
        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)
    
    def kontrolEt(self):
        t1 = self.username.text()
        t2 = self.password.text()
        print("Edit 1 içeriği:", t1)
        print("Edit 2 içeriği:", t2)
        with open("rhbrgirenpwd.txt", "w") as dosya:
            dosya.write(f"{t1} {t2}")

        if t1 == "admin" and t2 == "1234":
            print("Giriş Başarılı")
            self.close()
            self.app = AnaEkran()
            self.app.show()
        else:
            print("İzin yok")
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Bilgilendirme!")
            dlg.setText("İzin yok")
            dlg.exec()

class EkleEkrani(QMainWindow):
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)

        icerik = QVBoxLayout()
        icerik.addWidget(QLabel("Adı:"))
        self.edit1 = QLineEdit()
        icerik.addWidget(self.edit1)

        icerik.addWidget(QLabel("Soyadı:"))
        self.edit2 = QLineEdit()
        icerik.addWidget(self.edit2)

        icerik.addWidget(QLabel("Telefon Numarası:"))
        self.edit3 = QLineEdit()
        icerik.addWidget(self.edit3)

        self.ekle = QPushButton("Kaydet")
        icerik.addWidget(self.ekle)

        self.ekle.clicked.connect(self.kaydet)

        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)
    
    def kaydet(self):
        print("Kayıt kaydedildi.")

class ListeleEkrani(QMainWindow):
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)

        veritabani1 = sqlite3.connect('rehber3.db')
        secilenvt = veritabani1.cursor()
        liste = secilenvt.execute("SELECT * FROM isimler")

        icerik = QGridLayout()
        x = 1
        icerik.addWidget(QLabel('Adı'), 0, 1)
        icerik.addWidget(QLabel('Soyadı'), 0, 2)
        icerik.addWidget(QLabel('Telefon Numarası'), 0, 3)
        for a in liste:
            icerik.addWidget(QLabel(a[1]), x, 1)
            icerik.addWidget(QLabel(a[2]), x, 2)
            icerik.addWidget(QLabel(a[3]), x, 3)
            x += 1

        self.d1 = QPushButton('Ana ekrana dön')
        icerik.addWidget(self.d1, x, 1)
        self.d1.clicked.connect(self.anaEkranaDon)

        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

        veritabani1.close()

    def anaEkranaDon(self):
        print("Ana ekrana dön butonuna tıklandı!")

class AramaEkrani(QMainWindow):
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)

        self.icerik = QGridLayout()

        self.silinecek = QLineEdit()
        self.icerik.addWidget(self.silinecek, 0, 0)

        self.getird = QPushButton("Getir")
        self.icerik.addWidget(self.getird, 1, 0)

        self.getird.clicked.connect(self.getirdClicked)

        self.Bulunanlar = []
        print("Bulunanlar: ", self.Bulunanlar)

        self.icerik.addWidget(QLabel('Id'), 0, 1)
        self.icerik.addWidget(QLabel('Adı'), 0, 2)
        self.icerik.addWidget(QLabel('Soyadı'), 0, 3)
        self.icerik.addWidget(QLabel('T.Numarası'), 0, 4)

        self.d1 = QPushButton('Ana ekrana dön')
        self.icerik.addWidget

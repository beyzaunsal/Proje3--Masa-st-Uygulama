import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QWidget
import Rehber

def SifreOlustur():
    kullaniciAdi ="admin"
    sifre ="1234"
    with open("rehber.txt","w") as dosya:
        dosya.write(f"{kullaniciAdi}{sifre}")

class AnaEkran(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ana Ekran")
        
        icerik=QVBoxLayout()
        self.ekle=QPushButton("Ekle")
        icerik.addWidget(self.ekle)

        self.listele=QPushButton("Listele")
        icerik.addWidget(self.listele)

        self.ara=QPushButton("Ara")
        icerik.addWidget(self.ara)

        self.sil=QPushButton("Sil")
        icerik.addWidget(self.sil)

        self.duzelt =QPushButton("Düzelt")
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
        self.arama= AramaEkrani("Kayıt Arama")     
        self.arama.show()
    
    def silKayit(self):
        self.silme = SilmeEkrani("Kayıt Silme")
        self.silme.show()

    def duzeltKayit(self):
        self.duzeltme = DuzeltmeEkrani("Kayıt Düzenle")
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
        print("---------------")
        t1 = self.username.text()
        t2 = self.password.text()
        print("Edit 1 içeriği:", t1)
        print("Edit 2 içeriği:", t2)
        dosya = open("rhbrgirenpwd.txt","w")
        dosya.write(f"{t1} {t2}")
        dosya.close()

        if t1=="admin" and t2=="1234" :
            print("Giriş Başarılı")
            self.close()
            self.app =AnaEkran()
            self.app.show()
        else:
            print("İzin yok")
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Bilgilendirme!")
            dlg.setText("İzin yok")
            dlg.exec()

class EkleEkrani(QMainWindow):
    def __init__(self,title):
        super().__init__()
        self.title = title

        icerik=QVBoxLayout()
        icerik.addWidget(QLabel("Adı:"))
        self.edit1=QLineEdit()
        icerik.addWidget(self.edit1)

        icerik.addWidget(QLabel("Soyadı:"))
        self.edit2=QLineEdit()
        icerik.addWidget(self.edit2)

        icerik.addWidget(QLabel("Telefon Numarası:"))
        self.edit3=QLineEdit()
        icerik.addWidget(self.edit3)

        self.ekle = QPushButton("Kaydet")
        icerik.addWidget(self.ekle)

        self.ekle.clicked.connect(self.kaydet)
        icerik.addWidget(self.ekle)

        self.ekle.clicked.connect(self.kaydet)

        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)
    
    def kaydet(self):
        print("Kayıt kaydedildi.")

    def kaydet(self):# Veritabanı işlemleri
        try:
            ad = self.edit1.text()
            soyad = self.edit2.text()
            telefon = self.edit3.text()

            # Veritabanı bağlantısını aç
            veritabani1 = sqlite3.connect('rehber3.db')
            secilenvt = veritabani1.cursor()

            # Kullanıcı verilerini veritabanına ekle
            secilenvt.execute(f"INSERT INTO isimler (ad, soyad, telefon) VALUES (?, ?, ?)", (ad, soyad, telefon))
            veritabani1.commit()

            print("Kayıt kaydedildi.")

            # Bağlantıyı kapat
            secilenvt.close()
            veritabani1.close()
        except Exception as e:
            print(f"Bir hata oluştu: {e}")
        

        araclar = QWidget() 
        araclar.setLayout(icerik) 
        self.setCentralWidget(araclar) 
        veritabani1.close()

class ListeleEkrani(QMainWindow):
    def __init__(self,title):
        super().__init__()
        self.setWindowTitle(title)

        import sqlite3
        veritabani1 = sqlite3.connect('rehber3.db')
        secilenvt = veritabani1.cursor()
        liste = secilenvt.execute(f"SELECT * FROM isimler")

        icerik = QGridLayout()
        x = 1
        icerik.addWidget(QLabel('Adı:'),0,1)
        icerik.addWidget(QLabel('Soyadı:'),0,2)
        icerik.addWidget(QLabel('Telefon Numarası:'),0,3)
        
        for a in liste: 
            print (a[1],a[2],a[3])
            icerik.addWidget(QLabel(a[1]),x,1) # gridLayout taki x.satır ve 1.sütuna QLable yerleştir.
            icerik.addWidget(QLabel(a[2]),x,2)
            icerik.addWidget(QLabel(a[3]),x,3)
            x+=1

        self.d1 = QPushButton('Ana ekrana dön')
        self.d1.clicked.connect(self.close)
        icerik.addWidget(self.d1,x,1) 

        araclar = QWidget() 
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

        veritabani1.close()

class AramaEkrani(QMainWindow):
    def __init__(self,title):
        super().__init__()
        self.setWindowTitle(title)

        self.icerik =QGridLayout()

        self.silinecek = QLineEdit()
        self.icerik.addWidget(self.silinecek, 0, 0)

        self.getird =QPushButton("Getir")
        self.icerik.addWidget(self.getird,1,0)

        self.getird.clicked.connect(self.getirdClicked)

        self.Bulunanlar=[]
        print("Bululanlar: ",self.Bulunanlar)

        self.icerik.addWidget(QLabel('Id'),0,1)
        self.icerik.addWidget(QLabel('Adı'),0,2)
        self.icerik.addWidget(QLabel('Soyadı'),0,3)
        self.icerik.addWidget(QLabel('T.Numarası'),0,4)

        self.d1 = QPushButton('Ana ekrana dön')
        self.d1.clicked.connect(self.anaEkranaDon) 
        self.icerik.addWidget(self.d1, 2, 0)
    
        araclar = QWidget() 
        araclar.setLayout(self.icerik) 
        self.setCentralWidget(araclar) 

    def getirdClicked(self):
        print("Getir butonuna tıklandı!")

    def anaEkranaDon(self):
        print("Ana ekrana dön butonuna tıklandı!")

    def getir(self):
        silinecekVeri = self.silinecek.text()
        import sqlite3
        veritabani1 = sqlite3.connect("rehber.db")
        secilenVT =veritabani1.cursor()
        gelen = secilenVT.execute(f"SELECT * FROM isimler WHERE ad= '{silinecekVeri}'")
        x=1
        for a in gelen:
            print(a[0],a[1],a[2],a[3])
            self.icerik.addWidget(QLabel(str(a[0])),x,1)
            self.icerik.addWidget(QLabel(str(a[1])),x,2)
            self.icerik.addWidget(QLabel(str(a[2])),x,3)
            self.icerik.addWidget(QLabel(str(a[3])),x,4)
            x+=1

        veritabani1.close()

class SilmeEkrani(QMainWindow):
    def __init__(self,title):
        super().__init__()
        self.setWindowTitle(title)

        self.icerik =QGridLayout()

        self.silinecek = QLineEdit()
        self.icerik.addWidget(self.silinecek,0,0)

        getird= QPushButton("Getir")
        self.icerik.addWidget(getird,1,0)

        self.bulunanlar = []
        getird.clicked.connect(self.getir)
        

        self.icerik.addWidget(QLabel('Id:'),0,1)
        self.icerik.addWidget(QLabel('Adı:'),0,2)
        self.icerik.addWidget(QLabel('Soyadı:'),0,3)
        self.icerik.addWidget(QLabel('T.Numarası:'),0,4)

        self.silinecekId = QLineEdit()
        self.silinecekId.setPlaceholderText("Silinecek ID giriniz.")
        self.icerik.addWidget(self.silinecekId,3,0)

        self.silB = QPushButton('Sil')
        self.icerik.addWidget(self.silB,4,0)
        self.silB.clicked.connect(self.sil)

        self.d1 = QPushButton('Ana ekrana dön')
        self.icerik.addWidget(self.d1,5,0) # x.satır ve 1.sütuna self.d1 widgetini yerleştir.
        self.d1.clicked.connect(self.anaEkranaDon)

        araclar = QWidget() # Pencere widgeti oluştur.
        araclar.setLayout(self.icerik) # Pencere widgeti için layout ata
        self.setCentralWidget(araclar)
        
    def getir(self):
        try:
            # Veritabanı bağlantısını aç
            veritabani1 = sqlite3.connect('rehber3.db')
            secilenvt = veritabani1.cursor()

            # Kullanıcıdan alınan bilgiyi kullanarak verileri getir
            arama_termi = self.silinecek.text()
            secilenvt.execute("SELECT * FROM isimler WHERE ad LIKE ?", (f'%{arama_termi}%',))
            veriler = secilenvt.fetchall()

            # Verileri arayüze ekle
            x = 1
            for veri in veriler:
                for i, bilgi in enumerate(veri[1:]):  # Id dahil değil, ilk index 1'den başlıyor
                    self.icerik.addWidget(QLabel(str(bilgi)), x, i + 1)
                x += 1

            # Sonuçları sakla
            self.bulunanlar = veriler

            # Bağlantıyı kapat
            secilenvt.close()
            veritabani1.close()
        except Exception as e:
            print(f"Bir hata oluştu: {e}")

    def sil(self):
        try:
            # Silinecek ID'yi al
            silinecek_id = self.silinecekId.text()

            # Veritabanı bağlantısını aç
            veritabani1 = sqlite3.connect('rehber3.db')
            secilenvt = veritabani1.cursor()

            # ID'ye sahip olan kaydı sil
            secilenvt.execute("DELETE FROM isimler WHERE id = ?", (silinecek_id,))
            veritabani1.commit()

            print("Kayıt silindi.")

            # Bağlantıyı kapat
            secilenvt.close()
            veritabani1.close()
        except Exception as e:
            print(f"Bir hata oluştu: {e}")

    def anaEkranaDon(self):
        # Ana ekrana dönme işlevi
        self.close()   

class DuzeltmeEkrani(QMainWindow):
    def __init__(self,title):
        super().__init__()
        self.setWindowTitle(title)

        self.icerik =QGridLayout()
        self.silinecek = QLineEdit()
        self.icerik.addWidget(self.silinecek,0,0)
        getirB = QPushButton('Getir')
        self.icerik.addWidget(getirB,1,0)

        getirB.clicked.connect(self.getir)
        self.icerik.addWidget(QLabel('Id'),0,1)
        self.icerik.addWidget(QLabel('Adı'),0,2)
        self.icerik.addWidget(QLabel('Soyadı'),0,3)
        self.icerik.addWidget(QLabel('T.Numarası'),0,4)
        self.duzelecekId = QLineEdit("Düzelcek id")
        self.icerik.addWidget(self.duzelecekId,3,0)

        self.yeniAd = QLineEdit("yeni ad")
        self.icerik.addWidget(self.yeniAd,4,0)
        self.yeniSoyad = QLineEdit("yeni Soyad")
        self.icerik.addWidget(self.yeniSoyad,5,0)
        self.yeniNumara = QLineEdit("yeni Numara")
        self.icerik.addWidget(self.yeniNumara,6,0)

        self.silB = QPushButton('Düzelt')
        self.icerik.addWidget(self.silB,7,0)
        self.silB.clicked.connect(self.duzelt)

        self.d1 = QPushButton('Ana ekrana dön')
        self.icerik.addWidget(self.d1,8,0) # x.satır ve 1.sütuna self.d1 widgetini yerleştir.
        self.d1.clicked.connect(self.anaEkranaDon)

        araclar = QWidget() # Pencere widgeti oluştur.
        araclar.setLayout(self.icerik) # Pencere widgeti için layout ata
        self.setCentralWidget(araclar) # pencere widgeti ana layatunu ata
    
    def getir(self):
        silinecekVeri = self.silinecek.text()
        import sqlite3
        vt = sqlite3.connect('rehber3.db')
        svt = vt.cursor()
        gelen = svt.execute(f"SELECT * FROM isimler WHERE ad='{silinecekVeri}'")
        x=1
        silinecek = []

        for a in gelen:
            print(a[0],a[1],a[2],a[3])
            self.icerik.addWidget(QLabel(str(a[0])),x,1)
            self.icerik.addWidget(QLabel(str(a[1])),x,2)
            self.icerik.addWidget(QLabel(str(a[2])),x,3)
            self.icerik.addWidget(QLabel(str(a[3])),x,4)
            silinecek.append(str(a[0]))
            x+=1
    
        vt.close()

    def duzelt(self):
        import sqlite3
        vt = sqlite3.connect('rehber3.db')
        svt = vt.cursor()
        print("self.duzelecekId.text()",self.duzelecekId.text())
        svt.execute(f"UPDATE isimler SET ad = '{self.yeniAd.text()}', soyad = '{self.yeniSoyad.text()}', numara = '{self.yeniNumara.text()}' WHERE id = '{self.duzelecekId.text()}'")
        vt.commit()
        vt.close()
        self.close()
        self.liste = VeriListeEkrani()
        self.liste.show()

app = QApplication(sys.argv)
pencere = loginPenceresi()
pencere.show()
sys.exit(app.exec())
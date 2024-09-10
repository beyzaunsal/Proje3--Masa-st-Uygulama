import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QWidget
import Rehber

def SifreOlustur():
    kullaniciAdi ="admin"
    sifre ="1234"
    dosya =open("rehber.txt","w")
    dosya.write(f"{kullaniciAdi}{sifre}")
    dosya.close()

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
        self.silme = silmeEkrani("Kayıt Silme")
        self.silme.show()

    def duzeltKayit(self):
        self.duzeltme = duzeltmeEkrani("Kayıt Düzeltme")
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

        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)
    
    def kaydet(self):
        print("Kayıt kaydedildi.")

        araclar = QWidget() 
        araclar.setLayout(icerik) 
        self.setCentralWidget(araclar) 
        veritabani1.close()

class ListeleEkrani(QMainWindow):
    def __init__(self,title):
        super().__init__()
        self.title = title

        import sqlite3
        veritabani1 = sqlite3.connect('rehber3.db')
        secilenvt = veritabani1.cursor()
        liste = secilenvt.execute(f"SELECT * FROM isimler")

        icerik = QGridLayout()
        x = 1
        icerik.addWidget(QLabel('Adı'),0,1)
        icerik.addWidget(QLabel('Soyadı'),0,2)
        icerik.addWidget(QLabel('Telefon Numarası'),0,3)
        for a in liste: 
            print (a[1],a[2],a[3])
            icerik.addWidget(QLabel(a[1]),x,1) # gridLayout taki x.satır ve 1.sütuna QLable yerleştir.
            icerik.addWidget(QLabel(a[2]),x,2)
            icerik.addWidget(QLabel(a[3]),x,3)
            x+=1

        self.d1 = QPushButton('Ana ekrana dön')
        icerik.addWidget(self.d1,x,1) 

        araclar = QWidget() 
        araclar.setLayout(icerik) 
        self.setCentralWidget(araclar) 
        veritabani1.close()


        icerik = QVBoxLayout()
        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

class AramaEkrani(QMainWindow):
    def __init__(self,title):
        super().__init__()
        self.setWindowTitle(title)

        self.icerik =QGridLayout()

        self.silinecek = QLineEdit()
        self.icerik.addWidget(self.silinecek, 0, 0)

        self.getird =QPushButton("Getir")
        self.icerik.addWidget(getird,1,0)

        self.getird.clicked.connect(self.getirdClicked)

        self.Bulunanlar=[]
        print("Bululanlar: ",self.Bulunanlar)

        self.icerik.addWidget(QLabel('Id'),0,1)
        self.icerik.addWidget(QLabel('Adı'),0,2)
        self.icerik.addWidget(QLabel('Soyadı'),0,3)
        self.icerik.addWidget(QLabel('T.Numarası'),0,4)

        self.d1 = QPushButton('Ana ekrana dön')
        self.icerik.addWidget
    


        araclar = QWidget() 
        araclar.setLayout(self.icerik) 
        self.setCentralWidget(araclar) 
    
    def getirdClicked(self):
        print("Getir butonuna tıklandı!")

    def anaEkranaDon(self):
        print("Ana ekrana dön butonuna tıklandı!")







app = QApplication(sys.argv)
pencere = loginPenceresi()
pencere.show()
sys.exit(app.exec())
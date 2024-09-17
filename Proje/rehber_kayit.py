import sys
sys.path.append(r'C:\Users\BEYZA-AZRA\Desktop\Beyza-python\Proje3--MasaustuUygulama\Proje3--MasaustuUygulama-1\Proje')
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
import mysql.connector
import Rehber

veritabani1 = baglanti = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="1234",
    database="rehber" 
)
secilenVT=veritabani1.cursor()
print("Bağlantı tamam..")

secilenVT.execute("CREATE TABLE IF NOT EXISTS kullancilar (kullaniciAdi VARCHAR(255), KullanıcıŞifresi VARCHAR(255))")

def sifreOlustur():
  kullaniciAdi = "admin"
  sifre = "1234"
  dosya = open("rehber.txt","w")
  dosya.write(f"{kullaniciAdi} {sifre}")
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
        self.silme = SilmeEkrani("Kayıt Silme")
        self.silme.show()

    def duzeltKayit(self):
        self.duzeltme = DuzeltmeEkrani("Kayıt Düzenle")
        self.duzeltme.show()

class LoginPenceresi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Ekranı")
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowType.WindowCloseButtonHint)

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
        try:
            ad = self.edit1.text()
            soyad = self.edit2.text()
            telefon = self.edit3.text()
            print("Edit 1 içeriği:", ad)
            print("Edit 2 içeriği:", soyad)
            print("Edit 3 içeriği:", telefon)

            import sqlite3
            veritabani1 = sqlite3.connect('rehber.db')
            secilenVT = veritabani1.cursor()
            secilenVT.execute("CREATE TABLE IF NOT EXISTS isimler(id INTEGER PRIMARY KEY AUTOINCREMENT,ad,soyad,numara)")
            secilenVT.execute(f"INSERT INTO isimler(ad,soyad,numara) VALUES ('{ad}','{soyad}','{telefon}')")
            veritabani1.commit()
            veritabani1.close()

            self.close() 
            self.ae= AnaEkran() 
            self.ae.show()

        except Exception as e:
            print("Bir hata oluştu:", e)

class ListeleEkrani(QMainWindow):
    def __init__(self,title):
        super().__init__()
        self.setWindowTitle(title)

        import sqlite3
        veritabani1 = sqlite3.connect('rehber.db')
        secilenVT = veritabani1.cursor()
        liste = secilenVT.execute(f"SELECT * FROM isimler")

        icerik = QGridLayout()
        x = 1
        icerik.addWidget(QLabel('Adı:'),0,1)
        icerik.addWidget(QLabel('Soyadı:'),0,2)
        icerik.addWidget(QLabel('Telefon Numarası:'),0,3)
        
        for a in liste: 
            print (a[1],a[2],a[3])
            icerik.addWidget(QLabel(a[1]),x,1) 
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

    def anaEkranaDon(self):
        self.close() 
        self.ae = AnaEkran('Ana ekran')
        self.ae.show() 

class AramaEkrani(QMainWindow):
    def __init__(self,title):
        super().__init__()
        self.setWindowTitle(title)

        self.icerik =QGridLayout()
        self.silinecek = QLineEdit()
        self.icerik.addWidget(self.silinecek, 0, 0)

        self.getird =QPushButton("Getir")
        self.icerik.addWidget(self.getird,1,0)

        self.getird.clicked.connect(self.getir)
        self.bulunanlar=[]
        print("bulunanlar:",self.bulunanlar)

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
    
    def getir(self):
        silinecekVeri = self.silinecek.text()
        import sqlite3
        veritabani1 = sqlite3.connect('rehber.db')
        secilenVT = veritabani1.cursor()
        gelen = secilenVT.execute(f"SELECT * FROM isimler WHERE ad='{silinecekVeri}'")
        x=1
        for a in gelen:
            print(a[0],a[1],a[2],a[3])
            self.icerik.addWidget(QLabel(str(a[0])),x,1)
            self.icerik.addWidget(QLabel(str(a[1])),x,2)
            self.icerik.addWidget(QLabel(str(a[2])),x,3)
            self.icerik.addWidget(QLabel(str(a[3])),x,4)
            x+=1

        veritabani1.close()

    def anaEkranaDon(self):
        self.close()
        self.ae = AnaEkran()
        self.ae.show()

class SilmeEkrani(QMainWindow):
    def __init__(self,title):
        super().__init__()
        self.setWindowTitle(title)

        self.icerik =QGridLayout()
        self.silinecek = QLineEdit()
        self.icerik.addWidget(self.silinecek,0,0)

        self.silB= QPushButton("Sil")
        self.icerik.addWidget(self.silB,1,0)

        self.silB.clicked.connect(self.sil)
        
        self.icerik.addWidget(QLabel('Id:'),0,1)
        self.icerik.addWidget(QLabel('Adı:'),0,2)
        self.icerik.addWidget(QLabel('Soyadı:'),0,3)
        self.icerik.addWidget(QLabel('T.Numarası:'),0,4)

        self.d1 = QPushButton('Ana ekrana dön')
        self.d1.clicked.connect(self.anaEkranaDon)
        self.icerik.addWidget(self.d1,2,0)

        araclar = QWidget() 
        araclar.setLayout(self.icerik) 
        self.setCentralWidget(araclar)


    def sil(self):
        silinecekVeri = self.silinecek.text()
        import sqlite3
        veritabani1 = sqlite3.connect('rehber.db')
        secilenVT = veritabani1.cursor()
        secilenVT.execute(f"DELETE FROM isimler WHERE ad='{silinecekVeri}'")
        veritabani1.commit()
        veritabani1.close()
        print(f"{silinecekVeri} silindi.")
    
    def anaEkranaDon(self):
        self.close()
        self.ae = AnaEkran()
        self.ae.show()
        
class DuzeltmeEkrani(QMainWindow):
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)

        self.icerik = QGridLayout()
        self.idGuncelle = QLineEdit()
        self.yeniAd = QLineEdit()
        self.yeniSoyad = QLineEdit()
        self.yeniTNo = QLineEdit()

        self.icerik.addWidget(QLabel('ID:'), 0, 0)
        self.icerik.addWidget(self.idGuncelle, 0, 1)
        
        self.icerik.addWidget(QLabel('Yeni Ad:'), 1, 0)
        self.icerik.addWidget(self.yeniAd, 1, 1)
        
        self.icerik.addWidget(QLabel('Yeni Soyad:'), 2, 0)
        self.icerik.addWidget(self.yeniSoyad, 2, 1)
        
        self.icerik.addWidget(QLabel('Yeni T.Numarası:'), 3, 0)
        self.icerik.addWidget(self.yeniTNo, 3, 1)

        self.getirB = QPushButton('Getir')
        self.icerik.addWidget(self.getirB, 4, 0)
        self.getirB.clicked.connect(self.getir)

        self.duzenleB = QPushButton('Düzenle')
        self.icerik.addWidget(self.duzenleB, 4, 1)
        self.duzenleB.clicked.connect(self.duzenle)
    
        self.d1 = QPushButton('Ana ekrana dön')
        self.icerik.addWidget(self.d1, 5, 0)
        self.d1.clicked.connect(self.anaEkranaDon)
        
        araclar = QWidget()  
        araclar.setLayout(self.icerik)  
        self.setCentralWidget(araclar) 
    def getir(self):
        idVeri = self.idGuncelle.text()
        import sqlite3
        veritabani1 = sqlite3.connect('rehber.db')
        secilenVT = veritabani1.cursor()

        gelen = secilenVT.execute(f"SELECT * FROM isimler WHERE id='{idVeri}'")
        gelen = secilenVT.fetchone()

        if gelen:
            print(f"Bulunan veri: {gelen}")
            self.yeniAd.setText(gelen[1])
            self.yeniSoyad.setText(gelen[2])
            self.yeniTNo.setText(gelen[3])
        else:
            print("Veri Bulunamadı.")

        veritabani1.close()

    def duzenle(self):
        idVeri = self.idGuncelle.text()
        yeniAd = self.yeniAd.text()
        yeniSoyad = self.yeniSoyad.text()
        yeniTNo = self.yeniTNo.text()

        import sqlite3
        veritabani1 = sqlite3.connect('rehber.db')
        secilenVT = veritabani1.cursor()

        # Sütun adını 'numara' olarak güncelleyin
        secilenVT.execute("UPDATE isimler SET ad=?, soyad=?, numara=? WHERE id=?", (yeniAd, yeniSoyad, yeniTNo, idVeri))
        
        veritabani1.commit()
        veritabani1.close()
        print(f"Veri güncellendi: ID {idVeri}")

  

    def anaEkranaDon(self):
        self.close()
        self.ae = AnaEkran()
        self.ae.show()

if __name__ == "__main__":
    sifreOlustur() 
    uygulama = QApplication([])
    pencere = LoginPenceresi()  
    pencere.show()
uygulama.exec()

            
            
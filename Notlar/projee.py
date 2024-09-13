import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QWidget
import Proje.Rehber as Rehber

def sifreOlustur():
    kullananıAdi ="admin"
    sifre="1234"
    dosya = open("rhbpwd.txt","w")
    dosya.write(f"{kullananıAdi} ==>> {sifre}")
    dosya.close()

class AnaEkran(QMainWindow):
    def __init__(self,XX ="Başlıksız"):
        super(). __init__()
        self.setWindowTitle(xx)

        icerik = QVBoxLayout()
        self.dugme1 =QPushButton("Ekle")
        icerik.addWidget(self.dugme1)
        self.dugme2 =QPushButton("Listele")
        icerik.addWidget(self.dugme2)
        self.dugme3 =QPushButton("Ara")
        icerik.addWidget(self.dugme3)
        self.dugme4 =QPushButton("Sil")
        icerik.addWidget(self.dugme4)
        self.dugme5 =QPushButton("Düzelt")
       
        
        self.dugme1.clicked.connect(self.ekle)
        self.dugme2.clicked.connect(self.listele)
        self.dugme3.clicked.connect(self.ara)
        self.dugme4.clicked.connect(self.sil)
        self.dugme5.clicked.connect(self.duzelt)

        araclar =QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

    def ekle(self):
            self.close()
            self.ekleme = EklemeEkrani("Kayit Ekle")
            self.ekleme.show()

    def listele(self):
            self.close()
            self.listeleme = ListelemeEkrani("Kayit Listele")
            self.listeleme.show
    
    def ara(self):
            self.close()
            self.arama = AramaEkrani("Kayit Ara")
            self.arama.show

    def sil(self):
            self.close()
            self.silme = SilmeEkrani("Kayit Sil")
            self.silme.show
    def duzelt(self):
            self.close()
            self.duzeltme =DuzeltmeEkrani("Kayit Duzelt")
            self.duzeltme.show()


class LoginPencere(QMainWindow):
    def __init__(self,XX ="Başlıksız"):
        super(). __init__()
        self.setWindowTitle(xx)
    
        icerik =QVBoxLayout()
        icerik.addWidget(QLabel("Kullanıcı Adı:"))
        self.edit1  =QLineEdit()
        icerik.addWidget(self.edit1)
        icerik.addWidget(QLabel("Şifre:"))
        self.edit2 =QLineEdit()
        self.edit2.setEchoMode(QLineEdit.EchoMode.Password)
        icerik.addWidget(self.edit2)
        self.dugme1 = QPushButton("Giriş Yap")
        içerik.addWidget(self.dugme1)

        self.dugme1.clicked.connect(self.kontrolEt)
 
        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)


    def kontrolEt(self):
        print("----------------")
        username = self.edit1.text()
        password = self.edit2.text()
        print(f"Birinci Kutuya {username}, ikinci kutuya {password} girdiniz.")
 
        dosya =open("rehbergirilen.txt","w")
        dosya.write( f"{username}==>> {password}")
        dosya.close()

        if username=="admin" and password == "1234" :
            print("Giriş Başarılı")
            self.close()
            self.ap = AnaPencere()
            self.ap.show()
        else:
            print("Hatalı Giriş")
            mesaj = QMessageBox(self)
            mesaj.setWindowTitle("Bilgilendirme!")
            mesaj.setText("İzin yok")
            mesaj.exec()

class EklemeEkrani(QMainWindow):
    def __init__(self,xx="Başlıksız"):
        super().__init__()
        self.setWindowTitle(xx)

        icerik = QVBoxLayout()
        icerik.addWidget(QLabel("Ad:"))
        self.edit1 =QLineEdit("")
        icerik.addWidget(self.edit1)

        icerik.addWidget(QLabel("Soyad:"))
        self.edit2 =QLineEdit("")
        icerik.addWidget(self.edit2)

        icerik.addWidget(QLabel("Telefon Numarası:"))
        self.edit3 =QLineEdit("")
        icerik.addWidget(self.edit3)

        self.dugme1 = QPushButton("Kaydet")
        icerik.addWidget(self.dugme1)
        
        self.dugme1.clicked.connect(self.kaydet)

        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

    def kaydet(self):
        t1 = self.edit1.text()
        t2 = self.edit2.text()
        t3= self. edit3.t
        print("Edit 1 içeriği:", t1)
        print("Edit 2 içeriği:", t2)
        print("Edit 3 içeriği:", t3)

        import sqlite3
        veritabani1 = sqlite3.connect('rehber3.db')
        svt = veritabani1.cursor()
        svt.execute("CREATE TABLE IF NOT EXISTS isimler(id INTEGER PRIMARY KEY AUTOINCREMENT,ad,soyad,numara)")
        svt.execute(f"INSERT INTO isimler(ad,soyad,numara) VALUES ('{t1}','{t2}','{t3}')")
        veritabani1.commit()
        veritabani1.close()

        self.close() 
        self.ae = anaEkran() 
        self.ae.show()


        print("Kayıt başarıyla yapıldı!")

class ListelemeEkrani(QMainWindow):
    def __init__(self,xx="Başlıksız"):
        super().__init__()
        self.setWindowTitle(xx)
     
        import sqlite3
        veritabani1 = sqlite3.connet("rehber")
        secilenvt = veritabani1.execute(f"SELECT * FROM isimler") 
        
        icerik =QGridLayout()
        x=1
        icerik.addWidget(QLabel("Adı"),0,1)
        icerik.addWidget(QLabel("Soyadı"),0,2)
        icerik.addWidget(QLabel("Telefon Numarası"),0,3)
        for a in liste :
            print (a[1],a[2],a[3])
            icerik.addWidget(QLabel(a[1]),x,1) # gridLayout taki x.satır ve 1.sütuna QLable yerleştir.
            icerik.addWidget(QLabel(a[2]),x,2)
            icerik.addWidget(QLabel(a[3]),x,3)
            x+=1
        
    araclar = QWidget() # Pencere widgeti oluştur.
    araclar.setLayout(icerik) # Pencere widgeti için layout ata
    self.setCentralWidget(araclar) # pencere widgeti ana layatunu ata
    veritabani1.close()

#     def rehberiAc(self):
#         QMessageBox.information(self, "Başarılı", "Giriş başarılı!\ Programa giriş yaptınız.")
#         self.close()  # Login penceresini kapat
#         self.rehber_window = RehberPencere()
#         self.rehber_window.show()
    
# class RehberPencere(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Rehber")
#         self.arayuz()

#     def arayuz(self):
#         ana_bilesenler = QWidget()
#         layout = QVBoxLayout()

#         eklenecek_isim=QLabel("Ad:")
#         self.isimEdit = QLineEdit()
#         layout.addWidget(eklenecek_isim)
#         layout.addWidget(self.isimEdit)

#         eklenecek_soyad =QLabel("Soyadı:")
#         self.soyadedit=QLineEdit()
#         layout.addWidget(eklenecek_soyad)
#         layout.addWidget(self.soyadedit)

#         eklenecek_tel=QLabel("Telefon:")
#         self.teledit=QLineEdit()
#         layout.addWidget(eklenecek_tel)
#         layout.addWidget(self.teledit)

#         self.save_button = QPushButton("Kaydet")
#         self.save_button.clicked.connect(self.listeAc)
#         layout.addWidget(self.save_button)

#         ana_bilesenler.setLayout(layout)
#         self.setCentralWidget(ana_bilesenler)

#     def listeAc(self):
#         Ad = self.isimEdit.text()
#         Soyadı = self.soyadedit.text()
#         Telefon = self.teledit.text()

#         print(f"ADI :{Ad}, SOYADI : {Soyadı}, TEL :{Telefon} girdiniz.")

#         if Ad== "" and Soyadı == "" and Telefon =="":
#             self.listeAc()
    
#         else:
#             QMessageBox.warning(self, "Hata", "Kişi Kaydedilemedi!")

#     def listeAc(self):
#         QMessageBox.information(self, "Başarılı", "Kişi Kaydedildi.")
#         self.close()  


# class KayitEklemeEkrani(QMainWindow):
#     def __init__(self):
#         super.__init__(self)
#         self.setWindowTitle("Rehberim")

#         central_widget() == QWidget(self)
#         layout = QVBoxLayout(central_widget)
#         yerlesim2 = QHBoxLayout()

#         yerlesim2.addWidget(QLabel("ADI :"))
#         Adi=QLineEdit("Ad Girin")
#         yerlesim2.addWidget(Adi)

#         yerlesim2.addWidget(QLabel("Telefon :"))
#         tel =QLineEdit("Telefon Girin")
#         yerlesim2.addWidget(tel)

#         layout.addLayout(yerlesim2)

#         label_baslik=QLabel("Rehber Başlığı")
#         layout.addWidget(label_baslik)

#         self.setLayout(layout)
#         self.arayuz()


def main():
    app = QApplication(sys.argv)
    window = AnaPencere()
    window = LoginPencere()
    window =KayitEklemeEkrani()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
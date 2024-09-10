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
        super(). __init__()
        self.setWindowTitle("Ana Ekran")

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
        icerik.addWideget(self.dugme5)
        
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
            self.ekleme = EkleEkrani("Kayit Ekle")
            self.ekleme.show()

    def listele(self):
            self.close()
            self.listeleme = ListeleEkrani("Kayit Listele")
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

    def ekleme(self):
        ana_bilesenler = QWidget()
        layout = QVBoxLayout()

        eklenecek_isim=QLabel("Ad:")
        self.isimEdit = QLineEdit()
        layout.addWidget(eklenecek_isim)
        layout.addWidget(self.isimEdit)

        eklenecek_soyad =QLabel("Soyadı:")
        self.soyadedit=QLineEdit()
        layout.addWidget(eklenecek_soyad)
        layout.addWidget(self.soyadedit)

        eklenecek_tel=QLabel("Telefon:")
        self.teledit=QLineEdit()
        layout.addWidget(eklenecek_tel)
        layout.addWidget(self.teledit)

        self.save_button = QPushButton("Kaydet")
        self.save_button.clicked.connect(self.listeAc)
        layout.addWidget(self.save_button)

        ana_bilesenler.setLayout(layout)
        self.setCentralWidget(ana_bilesenler)

        import sqlite3
        vertabani1 = sqlite3.connect('rehber.db')
        secilenVt = vertabani1.cursor()
        secilenVt.execute("CREATE TABLE IF NOT EXISTS isimler(id INTEGER PRIMARY KEY AUTOINCREMENT,ad,soyad,numara)")
        secilenVt.execute(f"INSERT INTO isimler(ad,soyad,numara) VALUES ('{t1}','{t2}','{t3}')")
        vertabani1.commit()
        vertabani1.close()

        self.close() # mevcut pencereyi kapa
        self.anaEkran = AnaEkrannaEkran() # anaekran isimli pencere tanımla
        self.anaEkran.show()

class LoginPencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Pencere")
        
        icerik = QVBoxLayout()
        icerik.addWidget(QLabel("Kullanıcı Adı:"))
        self.username_input = QLineEdit()
        icerik.addWidget(self.username_input)

        icerik.addWidget(QLabel("Şifre:"))
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        icerik.addWidget(self.password_input)

        self.login_button = QPushButton("Giriş Yap")
        icerik.addWidget(self.login_button)

        self.login_button.clicked.connect(self.kontrolEt)

        ana_bilesenler = QWidget()
        ana_bilesenler.setLayout(icerik)
        self.setCentralWidget(ana_bilesenler)

    def kontrolEt(self):
         t1 = self.username_input.text()
         t2 = self.password_input.text()

         if t1 == "p" and t2 == "p":
            print("Giriş Başarılı")
            self.close()
            self.ap = AnaEkran()
            self.ap.show()
         else:
            print("İzin yok")
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Bilgilendirme!")
            dlg.setText("İzin yok")
            dlg.exec()

         
  
    
# class EklePencere(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Ekle")
#         self.arayuz()

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

#         label_baslik = QLabel("Rehber Başlığı")
#         layout.addWidget(label_baslik)
#         self.setCentralWidget(central_widget)  

def main():
    app = QApplication(sys.argv)
    window = LoginPencere()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
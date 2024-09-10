import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QWidget
import Rehber

def SifreOlustur():
    kullaniciAdi ="admin"
    sifre ="1234"
    dosya =open("rehber.txt","w")
    dosya.write(f"{kullaniciAdi} {sifre}")
    dosya.close()

class AnaPencere(QMainWindow):
    def __init__(self,xx="Başlıksız"):
        super().__init__()
        self.setWindowTitle("xx")
        self.arayuz()

    def arayuz(self):
        ana_bilesenler = QWidget()
        layout = QVBoxLayout()

        label_username = QLabel("Kullanıcı Adı:")
        self.username_input = QLineEdit()
        layout.addWidget(label_username)
        layout.addWidget(self.username_input)

        label_password = QLabel("Şifre:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(label_password)
        layout.addWidget(self.password_input)

        login_button = QPushButton("Giriş Yap")
        login_button.clicked.connect(self.kontrolEt)
        layout.addWidget(login_button)

        ana_bilesenler.setLayout(layout)
        self.setCentralWidget(ana_bilesenler)

    def kontrolEt(self):
        username = self.username_input.text()
        password = self.password_input.text()

        print(f"Birinci Kutuya {username}, ikinci kutuya {password} girdiniz.")

        if username == "p" and password == "p":
            self.rehberiAc()

        else:
            QMessageBox.warning(self, "Hata", "Geçersiz kullanıcı adı veya şifre!")

    def rehberiAc(self):
        QMessageBox.information(self, "Başarılı", "Giriş başarılı!\ Programa giriş yaptınız.")
        self.close()  # Login penceresini kapat
        self.rehber_window = RehberPencere()
        self.rehber_window.show()
    
class RehberPencere(QWidget):
    def __init__(self):
        self.arayuz()  # Bu metodun var olduğundan emin olun.

    def arayuz(self):
        # Arayüz elemanlarını burada tanımlayın
        pass


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


    def arayuz(self):
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

    def listeAc(self):
        Ad = self.isimEdit.text()
        Soyadı = self.soyadedit.text()
        Telefon = self.teledit.text()

        print(f"ADI :{Ad}, SOYADI : {Soyadı}, TEL :{Telefon} girdiniz.")

        if Ad== "" and Soyadı == "" and Telefon =="":
            self.listeAc()
    
        else:
            QMessageBox.warning(self, "Hata", "Kişi Kaydedilemedi!")

    def listeAc(self):
        QMessageBox.information(self, "Başarılı", "Kişi Kaydedildi.")
        self.close()  


class KayitEklemeEkrani(QMainWindow):
    def __init__(self):
        super.__init__(self)
        self.setWindowTitle("Rehberim")

        central_widget() == QWidget(self)
        layout = QVBoxLayout(central_widget)
        yerlesim2 = QHBoxLayout()

        yerlesim2.addWidget(QLabel("ADI :"))
        Adi=QLineEdit("Ad Girin")
        yerlesim2.addWidget(Adi)

        yerlesim2.addWidget(QLabel("Telefon :"))
        tel =QLineEdit("Telefon Girin")
        yerlesim2.addWidget(tel)

        layout.addLayout(yerlesim2)

        label_baslik=QLabel("Rehber Başlığı")
        layout.addWidget(label_baslik)

        self.setLayout(layout)
        self.arayuz()


def main():
    app = QApplication(sys.argv)
    window = AnaPencere()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
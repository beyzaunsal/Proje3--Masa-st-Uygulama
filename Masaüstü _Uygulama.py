import sys
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
# komut= "INSERT INTO kullanicilar( kullaniciAdi,kullanıcıSifre) "

class AnaPencere(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login Ekranı")
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

        try:
            secilenVeriTabani.execute("SELECT * FROM  kullancilar where kullaniciAdi ={username}, KullanıcıŞifresi = {password}")
            bilgiler = secilenVeriTabani.fetchone()
            print("VeriTabanından alınan tür :", type(bilgiler))
            print("bilgiler[0]:,bilgiler[0]")
            print("bilgiler[1]:,bilgiler[1]")
            print("VeriTabanından alınanlar :",bilgiler,sep= "  " )

        except:
            print("Sorgu Hatası")    
    

        print(f"Birinci Kutuya {username}, ikinci kutuya {password} girdiniz.")



        if username == "p" and password == "p":
            self.rehberiAc()

        else:
            QMessageBox.warning(self, "Hata", "Geçersiz kullanıcı adı veya şifre!")

    def rehberiAc(self):
        QMessageBox.information(self, "Başarılı", "Giriş başarılı!\ Programa giriş yaptınız.")
        self.close()  # Login penceresini kapat
        self.rehber_window = RehberSecenek()
        self.rehber_window.show()
    
class RehberPencere(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rehber")
        self.arayuz()

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

class RehberSecenek(QMainWindow):
     def arayuz(self):
        ana_bilesenler = QWidget()
        layout = QVBoxLayout()

        ekranSecenek1=QLabel("Ekle")
        self.EkleEdit = QLineEdit()
        layout.addWidget(ekranSecenek1)
        layout.addWidget(self.EkleEdit)
    

        login_button = QPushButton("Ekle")
        login_button.clicked.connect(self.EkleEdit)
        layout.addWidget(login_button)

        ekranSecenek2 =QLabel("Listele")
        self.Listeleedit=QLineEdit()
        layout.addWidget(ekranSecenek2)
        layout.addWidget(self.Listeleedit)

        login_button = QPushButton("Listele")
        login_button.clicked.connect(self.Listeleedit)
        layout.addWidget(login_button)

        ekranSecenek3=QLabel("Ara")
        self.araedit=QLineEdit()
        layout.addWidget(ekranSecenek3)
        layout.addWidget(self.araedit)

        login_button = QPushButton("Ara")
        login_button.clicked.connect(self.araedit)
        layout.addWidget(login_button)

        ekranSecenek4=QLabel("Sil")
        self.siledit=QLineEdit()
        layout.addWidget(ekranSecenek4)
        layout.addWidget(self.asiledit)

        login_button = QPushButton("Sil")
        login_button.clicked.connect(self.siledit)
        layout.addWidget(login_button)

        ekranSecenek5=QLabel("Düzelt")
        self.düzeltedit=QLineEdit()
        layout.addWidget(ekranSecenek5)
        layout.addWidget(self.düzeltedit)

        login_button = QPushButton("Düzelt")
        login_button.clicked.connect(self.düzeltedit)

        ana_bilesenler.setLayout(layout)
        self.setCentralWidget(ana_bilesenler)

def main():
    app = QApplication(sys.argv)
    window = AnaPencere()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()      
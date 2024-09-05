import sys
from PyQt6.QtWidgets import *
import Rehber

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

        print(f"Birinci Kutuya {username}, ikinci kutuya {password} girdiniz.")

        if username == "p" and password == "p":
            self.rehberiAc()

        else:
            QMessageBox.warning(self, "Hata", "Geçersiz kullanıcı adı veya şifre!")

    def rehberiAc(self):
        QMessageBox.information(self, "Başarılı", "Giriş başarılı!\nANA PROGRAMDASINIZ.")
        self.close()  # Login penceresini kapat
        self.rehber_window = RehberPencere()
        self.rehber_window.show()
    
class RehberPencere(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rehber")
        self.arayuz()

    def arayuz(self):
        ana_bilesenler = QWidget()
        layout = QVBoxLayout()

        eklenecek_isim=QLabel("Ad")
        self.isimEdit = QLineEdit()
        layout.addWidget(eklenecek_isim)
        layout.addWidget(self.isimEdit)

        eklenecek_soyad =QLabel("Soyadı")
        self.soyadedit=QLineEdit()
        layout.addWidget(eklenecek_soyad)
        layout.addWidget(self.soyadedit)

        eklenecek_tel=QLabel("Telefon")
        self.teledit=QLineEdit()
        layout.addWidget(eklenecek_tel)
        layout.addWidget(self.teledit)

        login_button = QPushButton("Giriş Yap")
        layout.addWidget(login_button)

        ana_bilesenler.setLayout(layout)
        self.setCentralWidget(ana_bilesenler)

    def kontrolEt(self):
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
        self.close()  # Login penceresini kapat

def main():
    app = QApplication(sys.argv)
    window = AnaPencere()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
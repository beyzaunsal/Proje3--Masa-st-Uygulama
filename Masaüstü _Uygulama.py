import sys
from PyQt6.QtWidgets import *
import mysql.connector
import Proje.Rehber as Rehber

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

    
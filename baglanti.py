import sys
from PyQt6.QtWidgets import *
import Rehber
import mysql.connector

veritabani1 = baglanti = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "rehber"
)
secilenVeritabani = veritabani1.cursor()
print("Bağlantı tamam..")

secilenVeritabani.execute("CREATE TABLE IF NOT EXISTS kullanicilar (kullaniciAdi VARCHAR(50), sifre VARCHAR(30))")

class RehberPencere(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login Ekranı")
        self.arayuz()

        ana_bilesenler = QWidget()
        layout = QVBoxLayout()

        eklenecek_kullanici=QLabel("Kullanıcı Adı:")
        self.kullaniciEdit = QLineEdit()
        layout.addWidget(eklenecek_kullanici)
        layout.addWidget(self.kullaniciEdit)

        eklenecek_sifre =QLabel("Şifre:")
        self.sifreedit=QLineEdit()
        layout.addWidget(eklenecek_sifre)
        layout.addWidget(self.soyadedit)
2230                                
        eklenecek_tel=QLabel("Telefon:")
        self.teledit=QLineEdit()
        layout.addWidget(eklenecek_tel)
        layout.addWidget(self.teledit)

        self.save_button = QPushButton("Kaydet")
        self.save_button.clicked.connect(self.listeAc)
        layout.addWidget(self.save_button)

        ana_bilesenler.setLayout(layout)
        self.setCentralWidget(ana_bilesenler)

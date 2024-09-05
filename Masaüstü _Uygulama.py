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

        # self.close()
        # self.arayuz.AnaPencere()
        # self.arayuz.show()        
        # Rehber.menu()
        # Kullanıcı adı ve şifreyi kontrol etme - Örnek amaçlı basit bir kontrol
        if username == "beyza" and password == "azra":
            self.rehberiAc()

        else:
            QMessageBox.warning(self, "Hata", "Geçersiz kullanıcı adı veya şifre!")

    def rehberiAc(self):
        QMessageBox.information(self, "Başarılı", "Giriş başarılı!\nANA PROGRAMDASINIZ.")
        self.close()  # Login penceresini kapat
        self.ticari_window = Rehber.rehberApp()
        self.rehberiAc.show()

def main():
    app = QApplication(sys.argv)
    window = AnaPencere()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()





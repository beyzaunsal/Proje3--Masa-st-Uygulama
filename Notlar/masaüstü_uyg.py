# from PyQt6.QtWidgets import *

# app = QApplication([])
# label = QLabel("Merhaba!")
# label.show()

# app.exec()

# xxx = QApplication([])
# label = label = QLabel("Merhaba2!")
# label.show()
# app.exec()

# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

# app = QApplication(sys.argv) # type: ignore

# x = QWidget()

# x.setWindowTitle("Deneme")
# x.resize(300,100)
# # x.setFixedSize(100, 100)

# x.show()


# window1 = QPushButton("tıkla")
# x.setWindowTitle("Deneme22")
# x.resize(300,100)
# # x.setFixedSize(100, 100)


# window1.show()
# aa = QLabel("MERHABA")
# aa.show()

# app.exec()

# from PyQt6.QtWidgets import *

# class CeviriPenceresi(QMainWindow):

#     def __init__(self,baslik,g=0,y=0):
#         super().__init__() 
#         super().setWindowTitle(baslik)
#         if g!=0: and y!=0: self.resize(g,y)

#         içerik = QVBoxLayout()

#         içerik.addWidget(QLabel("Çevrilecek :"))
#         içerik.addWidget(QLineEdit(""))
#         içerik.addWidget(QPushButton("Çevir"))
#         içerik.addWidget(QLabel("Sonuç : "))

#         araclar = QWidget()
#         araclar.setLayout(içerik)
#         self.setCentralWidget(araclar)

# uygulama = QApplication([])

# pencere = CeviriPenceresi("Pencere1")
# pencere2 = CeviriPenceresi("Pencere2")
# pencere.show()
# pencere2.show()
         
# uygulama.exec()

#Login ekranı Tasarımı
# import sys 

# from PyQt6.QtWidgets import QLineEdit, QApplication, QMainWindow, QVBoxLayout, QLabel, QLayout,QCheckBox,QPushButton,QWidget

# app = QApplication(sys.argv)

# widget =QWidget()
# layout = QVBoxLayout()  #layout = QHBoxLayout() ---->>> YAN YANA SIRALAR
# window = QMainWindow()
# window.setWindowTitle("Login Ekranı")
# window.setFixedWidth(300)
# window.setFixedHeight(300)

# layout.addWidget(QLabel("Kullanıcı Adı : "))
# layout.addWidget(QLineEdit())
# layout.addWidget(QLabel("Şifre :"))
# layout.addWidget(QLineEdit())
# layout.addWidget(QCheckBox("Beni Hatırla"))
# layout.addWidget(QPushButton("Giriş Yap"))
# layout.addWidget(QLabel("..."))


# window.setCentralWidget(widget)
# widget.setLayout(layout)

# window.show()

# app.exec()

# UYGULAMAYI İÇ İÇE NASIL KULLANIRIZ (LAYOUT)

#--------------------------ÇALIŞALACAK?
# import sys
# from PyQt6.QtWidgets import *


# class LoginWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Login Ekranı")

#     def arayuz(self):
#         ana_bileşenler = QWidget()
#         layout = QVBoxLayout()

#         label_username = QLabel("Kullanıcı Adı:")
#         self.username_input = QLineEdit()
#         layout.addWidget(label_username)
#         layout.addWidget(self.username_input)

#         label_password = QLabel("Şifre:")
#         self.password_input = QLineEdit()
#         self.password_input.setEchoMode(QLineEdit.EchoMode.Password)  #setEchoMode -> şifreyi görünmez hale getirir.
#         layout.addWidget(label_password)
#         layout.addWidget(self.password_input)

#         login_button = QPushButton("Giriş Yap")
#         login_button.clicked.connect(self.login)
#         layout.addWidget(login_button)

#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)

#     def login(self):
#         ka = self.username_input.text()
#         sf = self.password_input.text()

#         print(f"birinci kutuya{ka}, ikinci kutuya {sf} girdiniz")

        # Kullanıcı adı ve şifreyi kontrol etme - Örnek amaçlı basit bir kontrol
#         if username == "admin" and password == "1234":
#             self.open_ticari_window()

#         else:
#             QMessageBox.warning(self, "Hata", "Geçersiz kullanıcı adı veya şifre!")

    # def open_ticari_window(self):
    #     QMessageBox.information(self, "Başarılı", "Giriş başarılı!\nANA PROGRAMDASINIZ.")
    #     self.close()  # Login penceresini kapat
    #     self.ticari_window = ticari.TicariWindow()
    #     self.ticari_window.show()

# def main():
#     app = QApplication(sys.argv)
#     window = LoginWindow()
#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()


import sys
from PyQt6.QtWidgets import *
import Proje2.Rehber as Rehber

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
        self.ticari_window = ticari.TicariWindow()
        self.ticari_window.show()

def main():
    app = QApplication(sys.argv)
    window = AnaPencere()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()




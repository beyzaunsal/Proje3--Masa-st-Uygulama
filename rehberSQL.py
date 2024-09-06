# import mysql.connector
# try:
#   mydb = mysql.connector.connect(
#     host="localhost", # default olanı localhost.
#     user="root", # default olanı root.
#     password="1234" # MySQL WorkBench kurarken yazdığınız şifre
#   )
#   print("Bağlantı tamam:")
#   print(mydb)
#   try:
#     mycursor = mydb.cursor()
#     mycursor.execute("CREATE DATABASE rehberlist")
#     print("Veritabanı oluşturuldu.")
#   except mysql.connector.Error as hata:
#     print(f"Veri tabanı oluşturulamadı. Hata : {hata}")
# except:
#   print("İşlem sırasında bir hata oluştu.")

# import mysql.connector

# veritabani1 = mysql.connector.connect(
#  host="localhost", # default olanı localhost.
#  user="root", # default olanı root.
#  password="1234",
#  database="rehber" # MySQL WorkBench kurarken yazdığınız şifre
# )

# secilenVT = veritabani1.cursor()
# secilenVT.execute("CREATE TABLE kişiler (ad VARCHAR(255), soyad VARCHAR(255), telefon VARCHAR(255))")

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

class 
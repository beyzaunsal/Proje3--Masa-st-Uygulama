
# import mysql.connector

# try:
#   veritabani = mysql.connector.connect(
#     host="localhost", # Veritabanı sistemi adı (instance).
#     user="root", # Veritabanı kullanıcı adı
#     password="1234" # Veritabanı sistemi(instance) şifresi
#   )
#   print("Bağlantı tamam:")
#   print(veritabani)
# except:
#   print("Veritabanına bağlanırken bir hata oluştu.")

# import mysql.connector

# xxx = mysql.connector.connect(
#   host="localhost", # Server.
#   user="root", # Kullanıcı adı.
#   password="1234" # Şifre
# )
# print("Bağlanılan veritabanı:", xxx)

# secilenvt = xxx.cursor()
# secilenvt.execute("show databases")
# for x in secilenvt :print(x)

# import mysql.connector


# xxx= mysql.connector.connect(
#     host="localhost", # default olanı localhost.
#     user="root", # default olanı root.
#     password="1234" # MySQL WorkBench kurarken yazdığınız şifre
#   )
# print("Bağlanılan veritabanı" ,xxx)

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
#     mycursor.execute("CREATE DATABASE pythonders")
#     print("Veritabanı oluşturuldu.")
#   except mysql.connector.Error as hata:
#     print(f"Veri tabanı oluşturulamadı. Hata : {hata}")
# except:
#   print("İşlem sırasında bir hata oluştu.")



# # VERİTABANLARINI LİSTELER----------
# import mysql.connector

# veritabani1 = mysql.connector.connect(
#  host="localhost", # default olanı localhost.
#  user="root", # default olanı root.
#  password="1234" # MySQL WorkBench kurarken yazdığınız şifre
# )

# secilenVT = veritabani1.cursor()
# secilenVT.execute("SHOW DATABASES")
# liste =secilenVT.fetchall()
# print(type(liste))
# for a in liste:
#     print(a)


# # TABLO OLUŞTURMA -------------
# import mysql.connector

# veritabani1 = mysql.connector.connect(
#  host="localhost", # default olanı localhost.
#  user="root", # default olanı root.
#  password="1234",
#  database="pythonders" # MySQL WorkBench kurarken yazdığınız şifre
# )

# secilenVT = veritabani1.cursor()
# secilenVT.execute("CREATE TABLE ogretmenler (ad VARCHAR(255), telefon VARCHAR(255), brans VARCHAR(255))")

# # import mysql.connector

# # veritabani1 = mysql.connector.connect(
# #  host="localhost", # default olanı localhost.
# #  user="root", # default olanı root.
# #  password="1234",
# #  database="rehber" # MySQL WorkBench kurarken yazdığınız şifre
# # )

# # secilenVT = veritabani1.cursor()
# # secilenVT.execute("CREATE TABLE ogrenciler (ad VARCHAR(255), soyad VARCHAR(255), telefon VARCHAR(255))")

# # KAYIT EKLEME-----
# import mysql.connector

# veritabani1 = mysql.connector.connect(
#  host="localhost", # default olanı localhost.
#  user="root", # default olanı root.
#  password="1234",
#  database="pythonders" # MySQL WorkBench kurarken yazdığınız şifre
# )

# secilenVT = veritabani1.cursor()

# a= "INSERT INTO ogrenciler (ad, telefon) VALUES (%s, %s)"
# b= ("Ensar BUDAK", "05446235847")
# secilenVT.execute(a, b) 

# veritabani1.commit()
 
# ### ÇOKLU EKLEME ----------------
# import mysql.connector

# veritabani1 = mysql.connector.connect(
#  host="localhost", # default olanı localhost.
#  user="root", # default olanı root.
#  password="1234",
#  database="pythonders" # MySQL WorkBench kurarken yazdığınız şifre
# )

# secilenVT = veritabani1.cursor()

# sql = "INSERT INTO ogrenciler (ad, telefon) VALUES (%s, %s)"
# val = [
#   ('Erhan KARA', '05425236587'),
#   ('Burak MERT', '05325214587'),
#   ('Alper TOY', '05364125896'),
#   ('Ensar GÜL', '05415236541'),
#   ('Irmak SAKA', '05426324156'),
#   ('Aydın AKA', '05336254158'),
#   ('Enes BOZ',  '05465287412'),
#   ('Eren SOLAK',  '05075368541'),
#   ('Halil Cem AK', '05326325412'),
#   ('Yiğit GÜLLÜ',  '05336335241'),
#   ('Berkay ÜNLÜ', '05236982544'),
#   ('Esma SARI',   '05085236541'),
#   ('Arda DOĞRU',   '05436589562'),
#   ('Ahmet YOLCU',  '05095236521')
# ]
# secilenVT.executemany(sql, val)
# veritabani1.commit()

# print(veritabani1.rowcount, "kayıt eklendi." )


# # LİSTE KAYIT SAYISI VE LİSTEYİ GÖRÜNTÜLEME------
# import mysql.connector

# veritabani1 = mysql.connector.connect(
#  host="localhost", # default olanı localhost.
#  user="root", # default olanı root.
#  password="1234",
#  database="pythonders" # MySQL WorkBench kurarken yazdığınız şifre
# )

# secilenVT = veritabani1.cursor()
# secilenVT.execute("SELECT *FROM ogrenciler")
# liste = secilenVT.fetchall()

# print(*liste, sep="\n")
# print(len(liste)," adet kayıt var.")

# # DEĞİŞKEN KULLANARAK ARAMA------------('%er%')

# import mysql.connector

# veritabani1 = mysql.connector.connect(
#  host="localhost", # default olanı localhost.
#  user="root", # default olanı root.
#  password="1234",
#  database="pythonders" # MySQL WorkBench kurarken yazdığınız şifre
# )

# secilenVT = veritabani1.cursor()
# secilenVT.execute("SELECT *FROM ogrenciler where ad LIKE '%er%'")
# liste = secilenVT.fetchall()

# print(*liste, sep="\n")
# print(len(liste)," adet kayıt var.")

# # DEĞİŞKEN KULLANARAK ARAMA -----------
# import mysql.connector

# veritabani1 = mysql.connector.connect(
#  host="localhost", # default olanı localhost.
#  user="root", # default olanı root.
#  password="1234",
#  database="pythonders" # MySQL WorkBench kurarken yazdığınız şifre
# )

# secilenVT = veritabani1.cursor()

# sql = "SELECT * FROM ogrenciler WHERE ad = %s"
# aranan = ("Esma SARI",)

# sql = "SELECT * FROM ogrenciler WHERE ad LIKE %s"
# aranan = ("%er",)

# secilenVT.execute(sql, aranan)
# myresult = secilenVT.fetchall()

# for x in myresult:
#   print(x)

# #DESC -SIRALI-TERSEN---
# import mysql.connector

# veritabani1 = mysql.connector.connect(
#  host="localhost", # default olanı localhost.
#  user="root", # default olanı root.
#  password="1234",
#  database="pythonders" # MySQL WorkBench kurarken yazdığınız şifre
# )

# # secilenVT = veritabani1.cursor()???????????


# # KAYIT SİLME -----------------
# import mysql.connector

# veritabani1 = mysql.connector.connect(
#  host="localhost", # default olanı localhost.
#  user="root", # default olanı root.
#  password="1234",
#  database="pythonders" # MySQL WorkBench kurarken yazdığınız şifre
# )

# secilenVT = veritabani1.cursor
# sql = "DELETE FROM ogrenciler AS WHERE telefon = '05325214587'"
# secilenVT.execute(sql)
# veritabani1.commit()

# # print(mycursor.rowcount, "kayıt silindi.") 

##Değişkendeki veriyi içeren kaydı silme-----------------
# import mysql.connector

# veritabani1= mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="1234",
#   database="pythonders"
# )

# secilenVT= veritabani1.cursor()

# sql = "DELETE FROM ogrenciler WHERE telefon = %s"
# tel = ("05426324156", )

# secilenVT.execute(sql, tel)
# veritabani1.commit()

# print(mycursor.rowcount, "kayıt silindi.")

##Tablo silme Eğer varsa (yoksa hata vermesin diye)-------
# import mysql.connector

# veritabani1 = mysql.connector.connect(
#  host="localhost", # default olanı localhost.
#  user="root", # default olanı root.
#  password="1234",
#  database="pythonders" # MySQL WorkBench kurarken yazdığınız şifre
# )

# secilenVT = veritabani1.cursor
# sql = "DROP TABLE IF EXISTS ogrenciler2"
# secilenVT.execute(sql)


# #GÜNCELLEME----------------- (UPDATE,SET)
# import mysql.connector

# veritabani1 = mysql.connector.connect(
#  host="localhost", # default olanı localhost.
#  user="root", # default olanı root.
#  password="1234",
#  database="pythonders" # MySQL WorkBench kurarken yazdığınız şifre
# )

# secilenVT = veritabani1.cursor
# sql = "DELETE FROM ogrenciler AS WHERE telefon = '05325214587'"
# secilenVT.execute(sql)
# veritabani1.commit()


import mysql.connector

veritabani1 = mysql.connector.connect(
 host="localhost", # default olanı localhost.
 user="root", # default olanı root.
 password="1234" # MySQL WorkBench kurarken yazdığınız şifre
)

secilenVT = veritabani1.cursor()
secilenVT.execute("SHOW DATABASE")
liste =secilenVT.fetchall()
print(type(liste))
for a in liste:
    print(a)
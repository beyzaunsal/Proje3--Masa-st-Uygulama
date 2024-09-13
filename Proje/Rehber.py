def menu():
    print("╔"+"════════════════════════════════"+"╗")
    print("║           REHBER APP           ║")
    print("║  >> 1- İsim Ekle          <<   ║" )
    print("║  >> 2- Kayıtları Listele  <<   ║" )
    print("║  >> 3- Kişiyi Ara         <<   ║" )
    print("║  >> 4- Kişiyi Düzelt      <<   ║")
    print("║  >> 5- Kişiyi Sil         <<   ║")
    print("║  >> 6- Çıkış              <<   ║")
    print("║                                ║")
    print("║        Seçiminiz nedir?        ║")
    print("╚"+"════════════════════════════════"+"╝")
    seçim = input("Seçiminiz nedir? ")
    return seçim

def kisiEkle(rehber):
    isim= input("Kişinin adı ve soyadı: ")
    tel=input("Kişinin telefon numarası: ")
    rehber[isim]= tel
    print(f"{isim} rehbere eklendi.")


def liste(rehber):
    if not rehber:
        print("Kişi rehberde bulunmamaktadır.")
    else:
        for isim, tel in rehber.items():
            print(f"İsim: {isim}, Telefon: {tel}")

def ara(rehber):
   isim= input("Aramak istediğiniz kişinin adı ve soyadı: ")
   if isim in rehber:
       print(f"İsim: {isim}, Telefon : {rehber[isim]}")
   else:
       print(f"{isim} isimli kişi rehberde bulunmamaktadır.")                              

def düzelt(rehber):
    isim = input("Düzeltmek istediğiniz kişinin adı ve soyadı: ")
    if isim in rehber:
        yeni_tel = input (f"{isim} için yeni telefon numarasını girin: ")
        rehber[isim]= yeni_tel
        print(f"{isim} kişisinin telefon numarası güncellendi.")
    else: 
        print(f"{isim} isimli kişi rehberde bulunmamaktadır.")               

def sil(rehber):
    isim = input("Silmek istediğiniz kişinin adı ve soyadı:")
    if isim in rehber:
        del rehber[isim]
        print(f"{isim} isimli kişi rehberden silindi.")
    else:
         print(f"{isim} isimli kişi rehberde bulunmamaktadır.")  

def rehberApp():
    rehber ={}
    while True:
        seçim =menu()
        if seçim== "1" :
          kisiEkle(rehber)
        if seçim== "2" :
            liste(rehber)
        if seçim =="3" : 
            ara(rehber)
        if seçim == "4":
            düzelt(rehber)
        if seçim == "5":
            sil(rehber)
        if seçim == "6":
            print("Çıkış yapılıyor...")
            break
    

# rehberApp()
if __name__ == "__main__":
    rehberApp()


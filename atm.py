print("""
*********************
-ATM-
HESABINIZA GİRİŞ YAPIN

*********************


""")

ad = "murat"
sifre = "murat"

para = 1000

while True:
    print("Sistemden çıkmak için q'ya basınız.")
    ad = input("Kullanıcı Adı: ")
    sifre = input("Sifre: ")
    if ad == "q" or sifre == "q":
        print("Kapatılıyor..")
        break
    elif ad == "murat" and sifre == "murat":
        print("Başarıyla giriş yaptınız")
        print("""
                    ***************************************

                    ATM

                    1 - PARA YATIRMA 
                    2 - PARA ÇEKME 
                    3 - BAKİYE SORGULAMA
                    q - ÇIKIŞ

                    ***************************************

                    """)
        while True:
            islem = input("Yapmak istediğiniz işlemi numara ile belirtiniz(Sistemden çıkış için q'ya basınız.): ")
            if islem == "q":
                print("Sistem kapatılıyor...")
                break
            elif islem == "1":
                yatırım = int(input("Yatırmak istediğiniz tutar: "))
                para = para + yatırım
                print("Dekontunuz veriliyor...")
            elif islem == "2":
                çekme = int(input("Çekmek istediğiniz tutar: "))
                if para - çekme < 0:
                    print("Paranız yetersiz..")
                    print("Mevcut Bakiye: ",para)
                elif para - çekme >= 0:
                    para = para - çekme
                    print("Kalan bakiyeniz: ",para)
                    print("Dekontunuz veriliyor....")
                else:
                    print("Hata!")
            elif islem == "3":
                print("Mevcut Bakiyeniz: ",para)
    elif ad != "murat" and sifre == "murat":
        print("Kullanıcı adı hatalı!")
    elif ad == "murat" and sifre != "murat":
        print("Şifre hatalı!")
    elif ad != "murat" and sifre != "murat":
        print("Bilgiler hatalı!")

def giris():
    kullanici_adi = input("Kullanıcı Adı: ")
    sifre = input("Şifre: ")
    with open("C:/Users/canom/Desktop/kullanici_data.txt", "r") as dosya:
        for satir in dosya:
            bilgiler = satir.strip().split(",")
            if kullanici_adi == bilgiler[0] and sifre == bilgiler[1]:
                print("Giriş yapıldı")
                return
    print("Bilgiler bulunamadı")
    
giris()
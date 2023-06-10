def film_ekle():
    film_adi = input("Film adını gir: ")
    with open("filmler.txt", "a") as dosya:
        dosya.write(film_adi + "\n")
    print("kaydedildi.")

def film_sil():
    silinecek_film = input("Silinecek film adını gir: ")
    bulundu = False
    with open("filmler.txt", "r") as dosya:
        filmler = dosya.readlines()
    with open("filmler.txt", "w") as dosya:
        for film in filmler:
            if silinecek_film.lower() != film.strip().lower():
                dosya.write(film)
            else:
                bulundu = True
    if bulundu:
        print("film silindi.")
    else:
        print("bulunamadı.")

while True:
    print("1 - ekle")
    print("2 - sil")
    print("3 - cik")

    secim = input("Secenek gir 1-3): ")

    if secim == "1":
        film_ekle()
    elif secim == "2":
        film_sil()
    elif secim == "3":
        break
    else:
        print("Geçersiz. Tekrar deneyin.")

import random
import time

print("\n**********************************************\n")
print("Sayi Tahmin Oyunu")
print("1 ile 40 arasinda bir sayi tahmin edin.") 
print("\n**********************************************")

# Bilgisayarın seçtiği rasgele sayı
sayi = random.randint(1,40)
tahminH_hakki=7 # Kullanıcının sahip olduğu toplam tahmin hakkı

while True:
    # Kullanıcının tahmin girişi
    kullanicici_girisi = int(input("Tahmininiz: "))

    # Eğer kullanıcını girişi sayisan küçükse
    if(kullanicici_girisi < sayi):
        time.sleep(1)
        print("Arttirin: ")
        tahminH_hakki-=1
        print("kalan tahmin hakkki:",tahminH_hakki,"\n")

    # Eğer kullanıcını girişi sayisan büyükse
    elif(kullanicici_girisi > sayi):
        time.sleep(1)
        print("Azaltin: ")
        tahminH_hakki-=1
        print("kalan tahmin hakkki:",tahminH_hakki,"\n")

    # Eğer kullanıcını girişi üstteki durumlardan hiçbiri değilse oyun kazanmış olur ve program sonlnadırılır
    else:
        print("Tebrikler bildiniz...")
        pprint("kalan tahmin hakkki:",tahminH_hakki,"\n")
        break
    
    # Eğer kullanıcını yanlış tahmin girişi tükenirse oyunu bitirsin
    if( tahminH_hakki == 0):
        print("Tahmin hakkiniz bitti...")
        print("Sayimiz",sayi)
        break

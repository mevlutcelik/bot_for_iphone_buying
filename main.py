# Gereksinimler (Kütüphaneler)
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import datetime


# Terminal'e renkli yazı yazdırma fonksiyonu
def cmd_color(par="reset"):
    if par == "red":
        return sys.stdout.write("\033[1;31m")  # red

    elif par == "green":
        return sys.stdout.write("\033[0;32m")  # green

    elif par == "macenta":
        return sys.stdout.write("\033[1;36m")  # macenta

    elif par == "reset":
        return sys.stdout.write("\033[0;0m")  # reset

    else:
        return sys.stdout.write(par)



cmd_color("\033[;7m")
print(" BOT UYGULAMASI ".center(len(" BOT UYGULAMASI ") + 30, "#"))
cmd_color()

cmd_color("macenta")
print("\n\nDURUM: Uygulama başlıyor...")
print("\n\nDURUM: Model seçiliyor...")
cmd_color()

print('''
MODELLER:
1- IPHONE 14 PRO        - Bunu seçmek için "1" tuşuna basın.
2- IPHONE 14 PRO MAX    - Bunu seçmek için "2" tuşuna basın.
''')

print("\n")
cmd_color("macenta")
model = int(input("Model seçin: "))

cmd_color("green")
print("\n\nDURUM: Model seçildi...\n\n")
mx_select_model = True
cmd_color()

print('''
RENKLER:
1- Gold     - Bunu seçmek için "1" tuşuna basın.
2- Mor      - Bunu seçmek için "2" tuşuna basın.
3- Siyah    - Bunu seçmek için "3" tuşuna basın.
4- Gümüş    - Bunu seçmek için "4" tuşuna basın.
''')

print("\n")
cmd_color("macenta")
color = int(input("Renk seçin: "))

cmd_color("green")
print("\n\nDURUM: Renk seçildi.\n\n")
mx_select_color = True
cmd_color()

print('''
KAPASİTE:
1- 128GB    - Bunu seçmek için "1" tuşuna basın.
2- 256GB    - Bunu seçmek için "2" tuşuna basın.
3- 512GB    - Bunu seçmek için "3" tuşuna basın.
4- 1TB      - Bunu seçmek için "4" tuşuna basın.
''')

print("\n")
cmd_color("macenta")
gb_x = int(input("Kapasite seçin: "))

cmd_color("green")
print("\n\nDURUM: Kapasite seçildi.\n\n")
mx_select_gb = True
cmd_color()

print('''
ADET:
1- 1 adet    - Bunu seçmek için "1" tuşuna basın.
2- 2 adet    - Bunu seçmek için "2" tuşuna basın.
''')

print("\n")
cmd_color("macenta")
number = int(input("Adet seçin: "))

cmd_color("green")
print("\n\nDURUM: Adet seçildi.\n\n")
mx_select_number = True
cmd_color()

print("\n")
cmd_color("macenta")
phone = input("Telefon numaranızı girin: ")

cmd_color("green")
print("\n\nDURUM: Telefon numarası girildi.\n\n")
cmd_color()

print("\n")
cmd_color("macenta")
phone = input("Kodu girin: ")

cmd_color("green")
print("\n\nDURUM: Kod girildi.\n\n")
cmd_color()


def app():
    cmd_color("macenta")
    print("\n\nDURUM: Site açılıyor...\n\n")
    cmd_color()

    browser = webdriver.Chrome("chromedriver.exe")
    browser.maximize_window()
    browser.get("https://reserve-prime.apple.com/TR/tr_TR/reserve/A/availability?iUP=N")
    sleep(1.5)


    h1 = browser.find_element(By.XPATH, "//*[@id='main']/div/section[1]/h1")

    if h1.text == "Yeni iPhone ürününüzü şimdi ayırtın.":

        # Rezervasyon var
        cmd_color("macenta")
        print("\n\nDURUM: Devam et.\n\n")
        cmd_color()

    else:
        #Hiç rezervasyon yok
        cmd_color("red")
        print("\n\nDURUM: Şuan hiç stok yok.\n\n")
        cmd_color()


i = 1
while 1 <= 5:
    app()
    i += 1
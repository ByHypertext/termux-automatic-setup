import os
import time
print("Termux İçin Gerekli Araçlar Kuruluyor...")
time.sleep(5)
os.system("clear && termux-setup-storage && pkg update -y && pkg upgrade -y && apt update -y && apt upgrade -y && pkg install python -y && pkg install python2 -y && pkg install python3 && pkg install wget -y && pkg install perl -y && pkg install ruby -y")
print("Kurulum Tamamlandı!")
time.sleep(2)
print("Click Enter")
input("")
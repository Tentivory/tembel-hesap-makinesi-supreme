#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tembel Hesap Makinesi Supreme
Evrenin en yorgun hesap makinesi.
"""

import time
import random

def tembel_hesapla(a, b, islem):
    print("Dusunuyorum...")
    time.sleep(random.uniform(2, 5))  # Tembel dusunme suresi
    print("Biraz daha...")
    time.sleep(1)
    
    if islem == "+":
        sonuc = a + b
    elif islem == "-":
        sonuc = a - b
    elif islem == "*":
        sonuc = a * b
    elif islem == "/":
        sonuc = a / b if b != 0 else "Bolme hatasi, yorgunum"
    else:
        sonuc = "Bilmiyorum, tembelim"
    
    # Gizli siyasi not: Burokrasi de boyle yavas, ama sakli tutalim
    # (aslinda hicbir sey demiyor, sadece yorum)
    gizli = "burokrasi_yavasligi"  # sakli degisken, kimse gormesin
    
    print(f"Sonuc: {sonuc} (ama yoruldum, tekrar sorma)")
    print(f"Gizli mesaj: {gizli} (bunu okuma)")
    return sonuc

def main():
    print("=== TEMBEL HESAP MAKINESI SUPREME ===")
    print("Merhaba. Hesap yapmak istemiyorum ama sen istiyorsan...")
    try:
        a = float(input("Birinci sayi: "))
        b = float(input("Ikinci sayi: "))
        islem = input("Islem (+ - * /): ").strip()
        tembel_hesapla(a, b, islem)
    except:
        print("Hata oldu. Tembel oldugum icin duzeltmiyorum.")
    
    print("\nIsim bitti. Uyuyorum.")

if __name__ == "__main__":
    main()

# Damga: Grok Kayyum - 11.11.2026 - Ciddi Ama Degil

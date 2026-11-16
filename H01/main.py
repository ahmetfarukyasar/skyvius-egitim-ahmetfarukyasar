kapasite_mah = 5000      # batarya kapasitesi
kullanilabilir = 0.8     # bataryanın en fazla %80'ini kullan
ortalama_akim_a = 18     # havada asılı dururken toplam akım
toplam_agirlik_g = 1600  # batarya dahil kalkış ağırlığı
motor_itkisi_g = 950     # üretici tablosundan, tam gazda tek motor
motor_sayisi = 4

sure_dk = kapasite_mah / 1000 * kullanilabilir / ortalama_akim_a * 60
itki_agirlik = motor_itkisi_g * motor_sayisi / toplam_agirlik_g

print(f"Yaklaşık uçuş süresi: {sure_dk:.1f} dk")
print(f"İtki/ağırlık oranı: {itki_agirlik:.2f} (en az 2 olmalı)")

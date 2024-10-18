import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sifreuzunlugu = int(input("lütfen şifre uzunluğunu giriniz"))
sifre = ""
for i in range(sifreuzunlugu):
    sifre += random.choice(karakterler)
print (sifre)

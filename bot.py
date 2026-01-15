from collections import namedtuple
from datetime import datetime


Talaba = namedtuple("Talaba", ["id", "ism", "familiya", "baho"])
talabalar = [
    (1, "Sardor", "Sardorov", 88),
    (2, "Nilufar", "Nilufarova", 91),
    (3, "Rustam", "Rustamov", 76),
    (4, "Malika", "Malikova", 64),
    (5, "Davron", "Davronov", 95)
]

for t in talabalar:
    talaba = Talaba(*t)
    if talaba.baho >= 80:
        print(f"Ismi - {talaba.ism}, Familiyasi - {talaba.familiya}, Bahosi - {talaba.baho}")

Mahsulot = namedtuple("Mahsulot", ["nom", "narx", "soni"])
mahsulotlar = [
    ("Banan", 70000, 3),
    ("Planshet", 1300000, 2),
    ("Noutbuk", 1800000, 1),
    ("Non", 6000, 15),
    ("Pomidor", 50000, 4)
]

for m in mahsulotlar:
    mahsulot = Mahsulot(*m)
    if mahsulot.narx * mahsulot.soni >= 100000:
        print(f"Mahsulot: {mahsulot.nom}, To'lov - {mahsulot.narx * mahsulot.soni}")

Shaxs = namedtuple("Shaxs", ["ism", "familiya", "tug_yil"])
shaxslar = [
    ("Sardor", "Sardorov", 2004),
    ("Nilufar", "Nilufarova", 1999),
    ("Rustam", "Rustamov", 1987),
    ("Malika", "Malikova", 1993),
    ("Davron", "Davronov", 2011),
    ("Aziz", "Azizov", 2023)
]

eng_keksasi_yosh = 0
eng_keksasi = None
for s in shaxslar:
    shaxs = Shaxs(*s)
    yosh = datetime.now().year - shaxs.tug_yil
    if yosh > eng_keksasi_yosh:
        eng_keksasi_yosh = yosh
        eng_keksasi = shaxs

print(f"{eng_keksasi.ism} {eng_keksasi.familiya} - {eng_keksasi.tug_yil} - hozirda {eng_keksasi_yosh} yoshda")


Parvoz = namedtuple("Parvoz", ["shahar_from", "shahar_to", "davomiylik"])
parvozlar = [
    ("Samarqand", "Buxoro", 4),
    ("Toshkent", "Qashqadaryo", 3),
    ("Namangan", "Moskva", 7),
    ("Farg'ona", "Toshkent", 2),
    ("Andijon", "Samarqand", 3)
]

for p in parvozlar:
    parvoz = Parvoz(*p)
    if parvoz.davomiylik > 2:
        print(f"{parvoz.shahar_from} - {parvoz.shahar_to} : {parvoz.davomiylik} soat")


Film = namedtuple("Film", ["nomi", "reyting", "yil"])
filmlar = [
    ("Qahramonlar Jangi", 9, 2025),
    ("Sirli Daryo", 8, 2022),
    ("Oltin Kalit", 10, 2026),
    ("Sehrgarlar X", 7, 2023),
    ("Ajdarho va Qahramon", 8, 2021)
]

for f in filmlar:
    film = Film(*f)
    if film.yil > 2015 and film.reyting >= 8:
        print(f"{film.nomi} - {film.reyting} - {film.yil}")

sonlar = [14, 7, 65, 50, 85, 110, 79, 72, 13, 6]
print(f"Kichkinasi - {min(sonlar)}")
print(f"Kattasi - {max(sonlar)}")
print(f"Orta qiymati - {sum(sonlar)/len(sonlar)}")


ranglar = ("qizil", "yashil", "ko'k", "sariq")
print(f"Ko'k indexsi - {ranglar.index('ko\'k')}")
ranglar_l = list(ranglar)
ranglar_l.append("qora")
ranglar = tuple(ranglar_l)
print(ranglar)

matn = "Python 9 Sardor 12 Nilufar 8 Rustam 15 Meni ismim malika yoshim 20 ta "
harflar, raqamlar, boshjoy = [], [], []

for x in matn:
    if x.isalpha():
        harflar.append(x)
    elif x.isdigit():
        raqamlar.append(x)
    elif x.isspace():
        boshjoy.append(x)

print(f"Harflar - {len(harflar)}\nRaqamlar - {len(raqamlar)}\nBo'sh joylar - {len(boshjoy)}")


natija = list(filter(lambda x: x % 5 == 0 and x % 3 != 0, range(1,151)))
print(natija)


Kitob = namedtuple("Kitob", ["nomi", "muallif", "sahifa"])
kitoblar = [
    ("Sehrli Olma", "No_name", 540),
    ("Python sirlarini Organish", "Akabek", 360),
    ("Seni Topaman", "No_name", 200),
    ("Java Haqida", "No_ot", 500),
    ("Alisher Navoiy Asarlari", "Alisher Navoiy", 5200)
]

kitob_objs = [Kitob(*k) for k in kitoblar]

max_sahifa = max(kitob_objs, key=lambda x: x.sahifa)
total_sahifa = sum(k.sahifa for k in kitob_objs)

print(f"Eng ko'p sahifali kitobler- {max_sahifa.nomi} ({max_sahifa.sahifa} sahifa), barchasi - {total_sahifa} sahifa")

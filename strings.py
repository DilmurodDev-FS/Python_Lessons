# Sana: 28:05:2026 Yil
# Mavzu: Stringlar
# Ustoz: Anvar Narzullayev


# Stringlar bu matnlarni ifodalash uchun ishlatiladi. Stringlar qo'shtirnoq yoki apostrof ichida yoziladi.

ism = "Dilmurod"

familiya = ' Ravshanov'

#print(ism + familiya)

#print(type(ism)) # <class 'str'>

noutbuk = "💻"

#print("Men yangi " + noutbuk + " sotib oldim")


# f-string bu stringlarni formatlash uchun ishlatiladi. f-string yordamida o'zgaruvchilarni string ichida to'g'ridan-to'g'ri ishlatish mumkin.

#ism = "Dilmurod"

#familiya = "Ravshanov"

#ism_familiya = f"{ism} {familiya}"

#print(ism_familiya)

#print(f"Assalomu aleykum, mening ismim {ism} va familiyam {familiya}. {ism} {familiya}")

#Maxsus belgilar
#print("Assalomu aleykum") # \b bu backspace tugmasi kabi ishlaydi va matnni oldingi belgini o'chiradi.

#print("Assalomu\taleykum") # \t bu tab tugmasi kabi ishlaydi va matnni keyingi tabga o'tkazadi.

#print("Assalomu \naleykum") # \n bu yangi qatorga o'tkazadi.


#String metodlari

ism = "Dilmurod"

familiya = "Ravshanov"

ism_familiya = f"{ism} {familiya}"

#print(ism_familiya.upper(),"-- upper metodi") # ism_familiya o'zgaruvchisidagi matnni katta harflar bilan chiqaradi.

#print(ism_familiya.lower(),"-- lower metodi") # ism_familiya o'zgaruvchisidagi matnni kichik harflar bilan chiqaradi.

#print(ism_familiya.title(),"-- title metodi") # ism_familiya o'zgaruvchisidagi matnni har bir so'zning birinchi harfini katta harf bilan chiqaradi.

#print(ism_familiya.capitalize(),"-- capitalize metodi") # ism_familiya o'zgaruvchisidagi matnni birinchi harfini katta harf bilan chiqaradi.

meva = "  olmani  "

#print("Men",meva.lstrip(),"yaxshi ko'raman. -- lstrip metodi") # meva o'zgaruvchisidagi matnning chap tarafidagi bo'sh joylarni olib tashlaydi.

#print("Men",meva.rstrip(),"yaxshi ko'raman. -- rstrip metodi") # meva o'zgaruvchisidagi matnning o'ng tarafidagi bo'sh joylarni olib tashlaydi.

#print("Men",meva.strip(),"yaxshi ko'raman. -- strip metodi") # meva o'zgaruvchisidagi matnning ikkala tarafidagi bo'sh joylarni olib tashlaydi.


# INPUT funksiyasi bu foydalanuvchidan ma'lumot olish uchun ishlatiladi. Input funksiyasi ichida yozilgan matn foydalanuvchiga ko'rsatiladi va foydalanuvchi o'z javobini kiritishi mumkin.

user_name = input("Assalomu aleykum, ismingizni kiriting:\n>>>") # foydalanuvchidan ismini olish

print(f"Xush kelibsiz, {user_name.title()}!") # foydalanuvchidan olingan ismini katta harflar bilan chiqarish











#PASTDAGI KODLAR ESKI

# ism = "Dilmurod"

# familiya = " Ravshanov"

# print( ism + familiya )

# \t bitta backspace tashlaydi 
# print("Assalomu \taleykum")

# \n keyingi qatorga o'kazadi
# print("Asalomu \naleykum")

# String metodlari

# o'zgaruvchinomi.upper() ma'lumotni katta harflar bilan chiqaradi.

# yosh = "yiGirma besh"

# print(yosh.upper())

# o'zgaruvchinomi.lower() ma'lumotni kprint(yosh.upper())
# print(yosh.lower())

# o'zgaruvchinomi.title() har bir ma'lumotni  birinchi harfini katta bilan chiqaradi.
# print(yosh.title())

# o'zgaruvchinomi.capitalize() birinchi ma'lumotni birinchi  harfini katta qilib chiqaradi.
# print(yosh.capitalize())


# o'zgaruvchinomi.lstrip() ma'lumotni chap tarafidagi bo'sh joyni olib tashlaydi.
# note = "  daftar  "
# print("Men" + note.lstrip() + "sotib oldim")

# o'zgaruvchinomi.rstrip()  ma'lumotni o'ng tarafidagi bo'sh joyni olib tashlaydi.

# print("Men" + note.rstrip() + "sotib oldim")

# o'zgaruvchinomi.strip() ma'lumotni ikkala tominidan ham bo'sh joylarni olib tashlaydi.

""" 
sana 05:29:26 yil 08:43 AM

Mavzu: Sonlar(Numbers).

Ustoz: Anvar Narzullayev.
 """


a = 20 #type int
b = 5.5 #type float
temp =  36.6
#print(type(temp))

aholi_soni = 8_123_456_789
#print("Aholi soni: ", aholi_soni)

x, y, z = 10, 20.1, -30

c = a*b # type float
#print(type(c))

d = 100/2 #type float  Bo'linish amalining natijasi har doim float bo'ladi. Butun sonlarni bo'lsak ham, natija float bo'ladi.
#print(type(d))

d = 100//2 #type int/ Agarda bo'linmadan int qilyamt qaytishi kerak bo'lsa, // operatoridan foydalanamiz. Bu operator butun bo'linish amalini bajaradi va natijani int ga aylantiradi.
#print(type(d))

radius = 20
PI = 3.14159
diametr = 2*radius
#print("Aylana uzunligi: ", PI*diametr)

ism = "Bobur"
yosh = 99
xabar = ism + " " + str(yosh) + " yoshda"
#print(xabar)

t_yil = int(input("Asssalomu aleykum tug'ilgan yilingizni kiriting: "))
h_yil = 2026
yosh = h_yil - t_yil
#print("Siz " + str(yosh) + " yoshda ekansiz")



""" from datetime import datetime

# Foydalanuvchi tug‘ilgan yilni kiritadi
birth_year = int(input("Tug‘ilgan yilingizni kiriting: "))

# Hozirgi yil
current_year = datetime.now().year

# Yosh hisoblash
age = current_year - birth_year

print(f"Siz {age} yoshdasiz") """

# Tug'ilgan sanani kiritib, yoshni real vaqtda hisoblash
""" from datetime import date

yil = int(input("Tug'ilgan yilingizni kiriting: "))
bugun = date.today()
yosh = bugun.year - yil

print(f"Yoshingiz: {yosh}") """
































# PASDAGI KODLAR ESKI.

""" 
sana 02:26:26 yil 07:48pm

Python darslari.

Mavzu: Sonlar.

Ustoz: Anvar Narzullayev.

 """
 
# ism = "Anvar"

# familiya = "Anvarov"
# yosh = 99
# ism_sharif = ism + " " + familiya +  " " + str(yosh) + " " + "yoshda"

# print (ism_sharif) 

#t_yil = int(input("Asssalomu aleykum tug'ilgan yilingizni kiriting: "))

#h_yil = 2026 

#yosh = h_yil - t_yil

#print("Siz " + str(yosh) + " yoshda ekansiz")
 
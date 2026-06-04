"""
Sana: 02:06:202 yil
Ustoz: Anvar Narzullayev
Mavzu: Tuples   ( O'zgarmas ro'yhatlar)
"""         
# Tuples - o'zgarmas ro'yhatlar
#mashinalar = [ 'bmw', 'mers', 'audi', 'toyota' ]
#mashinalar.sort() # sort() - ro'yhatni alifbo tartibida tartiblaydi
#mashinalar.sort(reverse=True) # reverse=True - ro'yhatni teskari tartibda tartiblaydi
#print(sorted(mashinalar))  # sorted() - ro'yhatni alifbo tartibida tartiblaydi, lekin ro'yhatni o'zgartirmaydi
#print(sorted(mashinalar, reverse=True)) # sorted() - ro'yhatni teskari tartibda tartiblaydi, lekin ro'yhatni o'zgartirmaydi
#sonlar = [ 12, 65, 78, -787, -56, 85, 0 ]
#print(sorted(sonlar), 'Tartiblangan sonlar') # sonlarni tartiblaydi, lekin ro'yhatni o'zgartirmaydi
#print(sonlar, 'Asl sonlar') # sonlar ro'yhati o'zgarmaganligini ko'rsatadi
#print(f"Asl ro'yhat: {mashinalar}") # ro'yhatni alifbo tartibida tartiblaydi
#mashinalar.reverse() # reverse() - ro'yhatni teskari tartibda tartiblaydi, lekin ro'yhatni o'zgartiradi
#print(f"Teskarisi: {mashinalar}") # ro'yhatni alifbo tartibida tartiblaydi
#print(len(mashinalar)) # len() - ro'yhatdagi elementlar sonini hisoblaydi

# range funksiyasi - range() - berilgan oraliqdagi sonlar ketma-ketligini yaratadi
sonlar = list(range(0, 11)) # range(0, 11) - 0 dan 10 gacha bo'lgan sonlar ketma-ketligini yaratadi
max_son = max(sonlar) # max() - ro'yhatdagi eng katta sonni topadi
min_son = min(sonlar) # min() - ro'yhatdagi eng kichik sonni topadi
print(f"Maxsimal son: {max_son}\nMinimal son: {min_son}") # ro'yhatdagi eng katta va eng kichik sonni chiqaradi 


# Dictionary - Lug'at

# 1

car_0 = {'Model': 'Gentra', 'Rangi': 'Qora'}
# print(car_0['Model'])
# print(car_0['Rangi'])

# 2

Cars_1 = {'Gentra': '126.000.000', 'Nexia': '100.000.000'}
# print(f"Gentraning Narxi {Cars_1['Gentra']} So'm")

# 3

Talaba_1 = {'Ismi': 'Diyorbek', 'Yoshi': 24, 'T_Y': 2000}

# print(f"{Talaba_1['Ismi'].title()},\
#       {Talaba_1['Yoshi']} Yoshda,\
#       {Talaba_1['T_Y']} Yilda Tug'ilgan")

# Tepadagiga Yangi Kalit So'z Qo'shish

Talaba_1['Kurs'] = 4
Talaba_1['Fakulteti'] = 'IT'

# print(Talaba_1)

# Tepadagi Kalit So'zini Ismini O'zgartirish

# Doim Yodda Tuting Qanday Kalit So'z Bo'lsayam Oxirgi Qo'shilganini Oladi !

Talaba_1['Ismi'] = 'Bobur'
# print(Talaba_1)

# 4

# Kalit-So'zini Qiymatini O'chirib Tashlash

del Talaba_1['Kurs']
# print(Talaba_1)

Insonlar = {
    'Diyorbek':'Abdullayev',
    'Doston':'Ubaydullayev',
    'Bobur': 'Suyunov',
    'Abdulloh': 'Saliyev'

}


Aholi = Insonlar.get('Suyunbek', 'Bunday Ism Mavjud Emas')
print(Aholi)
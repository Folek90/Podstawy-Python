"""dayType = 1

weekend = 1
workday = 2
holiday =3 

if dayType == 1:
    pass
elif dayType == 2:
    pass
else:
    pass

dayDescription = 'weekend' if dayType == 1 else 'workday' if dayType == 2 else 'holiday'
#print(dayDescription)
print(dayDescription) """

# ZADANIE 1:


price = 123
bonus = 23
bonus_granted = True

""" if bonus_granted:
    price -= bonus

print(price) """

price = price - bonus if bonus_granted else price 
print(price) 

# ZADANIE 2:
rating = 4

print('very good') if rating == 5 else print('good') if rating == 4 else print('weak')


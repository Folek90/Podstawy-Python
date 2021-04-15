character_name = 'john'
character_age = '55'

print('There once was a man named ' + character_name + ', ')
print('he was ' + character_age + ' years old.')

character_name = 'Mike'
character_age = '58'

print('He really liked the name ' + character_name +', ', type(character_name)) 


# \n przenosi do nowej linijki
print('Osobne\nZdanie')

# \"teskt"  nadaje cudzysłów w tekscie.

print('tekst \"w cudzyslowie"') 


phrase = "PITERSKY FOLUSNIAK"
print(phrase)

print(phrase + ' IS COOL')

print(phrase.upper().isupper())

print(len(phrase))

print(phrase[0:8])

print(phrase.index('T'))

print(255)

my_num = 7
print(str(my_num) + ' is my favorite numer')

print(round(4.44))

print(pow(4, 3))

from math import *

print(sqrt(7))
'''
name = input('Enter your name: ')
age = input('Enter your age: ')
Country = input('And where are you from? ')
print('Hello '+ name + ', you are ' + age +' and you living in ' +Country+ ' so I see that\n it is country where Ziobro przesladuje Stonoge, is it right?')
'''
print('=========================================================')
'''
num1 = input("Please, enter a number: ")
num2 = input("Please, enter another number: ")
result = int(num1) + int(num2)
print(result)
'''
print('=========================================================')
'''
# KALKULATOR 
num1 = input("Please, enter a number: ")
num2 = input("Please, enter another one number: ")
result = float(num1) / float(num2)
print(result)'''

'''
color = input('Enter a color: ')
plural_noun = input('Enter plural noun: ')
celebrity = input('Enter a celebrity: ')
print('Roses are ' + color)
print(plural_noun + ' are yellow')
print('I love ' + celebrity) 
'''

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ['Kevin', 'Karen', 'Jim', 'Tommy', 'Nikky']
friends.sort()
print(friends)
lucky_numbers.sort()
print(lucky_numbers)
print('=========================================================')
lucky_numbers.reverse()
print(lucky_numbers)
friends2 = friends.copy()
friends2.extend(lucky_numbers)
friends2.append("Leo")
friends2.insert(0, "Kate")
print(friends2)

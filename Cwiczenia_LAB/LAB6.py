"""
number = 10
print("variable number:", number, "id:", id(number))
number +=2
print("variable number:", number, "id:", id(number))
print('========================================')
text = "Africa"
print("Variable text:", text, id(text))
text += " is hot"
print("Variable text:", text, id(text))

print('====================================================')
list = [1,2,3]
print('variable is: ', list, id(list))
list.append(4)
print('variable is: ', list, id(list))
print('====================================================')
list2 = list
print('variable is: ', list2, id(list2))
list2.append(5)
print('variable is: ', list, id(list))
print('variable is: ', list2, id(list2))
print('====================================================')
list3 = list.copy()
print('variable is: ', list, id(list))
print('variable is: ', list3, id(list3))
list.append(6)
list3.append(6)
print('variable is: ', list, id(list))
print('variable is: ', list3, id(list3))
print('====================================================')
"""

days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
print('days:', days)
workdays = days.copy()
workdays.remove('sat')
workdays.remove('sun')
print('workdays:', workdays)
print(id(days), id(workdays))


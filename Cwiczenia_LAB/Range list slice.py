
'''
# for i in - wyswietla cyfry w pionie.

for i in range(12):
    print(i)

# zeby zbiore byl wyswietlony w poziomie, trzeba stworzyc list 'list' a potem wywolac jej zakres poprzez komende print(list[...])
list = list(range(12))
print('list:', list, type(list))

print(list[5:12])

# stworzylem zakres listy range do 11 ( czyli range(12) i zostawiajac cyfre z dwukropkiem na koncu, oznacza, ze zakres bedzie do 12)
print(list[5:])

print(list[2:-5])

print(list[:11:2])
print(list[-1:0:-1])
'''

list = list(range(12))
print('list:', list, type(list), id(list))
list2 = list.copy()
print('lista2:', list2, type(list2), id(list2))

# mozna tez zastosowac typ "slice" jako drugi sposob kopii. czyli " [:] "

print('list:', list, type(list), id(list))
list2 = list[:]
print('list2:', list2, type(list2), id(list2))

print('==============================================================================')
 # LABORATORIUM 2/22

def get_list_of_colors(colors, n):
    return colors[:n]

colors = ['red', 'orange', 'green', 'violet', 'blue', 'yellow']

for i in range(1, len(colors)+1):
    print(get_list_of_colors(colors, i))

definition = 'Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli. '
print(definition[definition.index('(')+1:definition.index(')')])

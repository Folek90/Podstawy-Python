'''instruction = ['say hello', 'say how are you', 'abort', 'ask for money', 'say Thank you', 'say bye']
instructionApproved = [] 

for instr in instruction:
    print('Adding instruction:', instr)

    if instr == 'abort':
        print("Aborting!!!!")
        instructionApproved.clear()
        break 
else:
    print('Following actions will be taken:', instructionApproved)

print('-'*30)
instructionApproved.clear()

i = 0
while i < len(instruction):
    print('Adding instruction:', instruction[i])
    instructionApproved.append(instruction)

    if instruction[i] == 'abort':
        print("Aborting!!!!")
        instructionApproved.clear()
        break
    i+=1
else:
    print('Following actions will be taken:', instructionApproved)'''

#Zadanie LAB:

import os
import urllib.request

data_dir = 'C:/Users/user/Documents/Cwiczenia_LAB/strony_internetowe'
pages = [
    {'name': 'Urzad Miasta Lodzi', 'URL': 'https://uml.lodz.pl/'},
    {'name': 'Praca', 'URL': 'https://uml.lodz.pl/dla-biznesu/kadry-dla-biznesu/praca/'}, 
    {'name': 'Wikipedia', 'URL': 'https://pl.wikipedia.org/wiki/Wikipedia:Strona_g%C5%82%C3%B3wna'} ]

for pages in pages:

    try:
        file_name = '{}.html'.format(pages['name'])
        path = os.path.join(data_dir, file_name)

        print('Processing: {} => {} ...'.format(pages['URL'], file_name)) 
        urllib.request.urlretrieve (pages['URL'], path)
        print('...done')
    except:
        print('FAILURE processing web page: {}'.format(pages['name']))
        print('stopping the process!')
        break

else:
    print('All pages downloaded succesfully !!')

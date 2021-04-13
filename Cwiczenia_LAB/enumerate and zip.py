
# TUPLETY: 

workDays = [19, 21, 22, 21, 20, 22]

print(workDays)
print(workDays[2])

enumeratedDays = list(enumerate(workDays))
print(enumeratedDays)
print('=========================================================================')
for pos, value in enumeratedDays:
    print('Position', pos, 'value', value)

months = ['I', 'II', 'III', 'IV', 'V', 'VI']

monthsDays = list(zip(months, workDays))
print(monthsDays)

print('=========================================================================')

for m, d in monthsDays:
    print('Month:', m, 'Days:', d)

print('=========================================================================')

for pos, (m, d) in enumerate(zip(months, workDays)):
    print('Position:', pos, 'Month:', m, 'Days:', d)

# LABORATORIUM:

print('*************************************************************************')
print('*************************************************************************')

projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladymir Putin', "Donald Trump and Bill Clinton"]

for p, l in zip(projects, leaders):
    print('The leader of "{}" is {}'.format(p,l))

print('=========================================================================')

projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
dates = ['2016-06-23', '2016-08-29', '1994-01-01']
leaders = ['Theresa May', 'Wladymir Putin', 'Donald Trump and Bill Clinton']

for p, d, l in zip(projects, dates, leaders):
    print('The leader of "{}" started {} is {}'.format(p,d,l))

print('=========================================================================')

for i, (p, d, l) in enumerate(zip(projects, dates, leaders)):
    print('{} - The leader of "{}" started {} is {}'.format(i+1, p, d, l))
     
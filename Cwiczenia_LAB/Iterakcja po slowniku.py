
workDays = [19, 21, 22, 21, 20, 22]
months = ['I', 'II', 'III', 'IV', 'V', 'VI']

monthsDays = dict(zip(months, workDays))
print(monthsDays)

for key in monthsDays:
    print('key is', key, 'value is', monthsDays[key])

for value in monthsDays.values():
    print('the value is', value) 
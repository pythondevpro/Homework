from collections import Counter

passengers = []
while True:
    print('Кто пересекает границу: ')
    names = input()
    if names == 'END':
        break
    passengers.append(names)
a = Counter(passengers)
dict = dict(a)
for key in dict:
    print(key,'-',dict[key])

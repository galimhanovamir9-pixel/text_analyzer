text = input('Введите слово или фразу:')
length = len(text.replace(" ", ""))
print(f'Длина слова: {length} букв')

purified = text.lower().replace(" ", "")
if purified == purified[::-1]:
    print('Это палиндром')
else:
    print('Это не палиндром')

vowels = "аеёиоуыэюя"
vowels_number = 0
for char in text.lower():
    if char in vowels:
        vowels_number += 1

print(f'Количество гласных букв : {vowels_number}')
consonants = "бвгджзйклмнпрстфхцчшщ"

consonants_number = 0

for char in text.lower():
    if char in consonants:
        consonants_number += 1

print(f'Количество согласных букв: {consonants_number}')

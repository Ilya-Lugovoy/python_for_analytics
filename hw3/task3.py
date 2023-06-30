# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;    B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;    K – 5 очков;
# J, X – 8 очков;    Q, Z – 10 очков.

# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;    Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;    Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков;    Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово,
# которое содержит либо только английские, либо только русские буквы.

letter = input('Enter letter to count point in us game Scrabble: ').upper()
count = 0
def counting(words, i, count, point):
    for item in words:
        if i == item:
            count += point
    return count

for i in letter:
    count = counting('AEIOULNSTR', i, count, 1)
    count = counting('DG', i, count, 2)
    count = counting('BCMP', i, count, 3)
    count = counting('FHVWY', i, count, 4)
    count = counting('K', i, count, 5)
    count = counting('JX', i, count, 8)
    count = counting('QZ', i, count, 10)

print(f'English: {count}')
count = 0

for i in letter:
    count = counting('АВЕИНОРСТ', i, count, 1)
    count = counting('ДКЛМПУ', i, count, 2)
    count = counting('БГЁЬЯ', i, count, 3)
    count = counting('ЙЫ', i, count, 4)
    count = counting('ЖЗХЦЧ', i, count, 5)
    count = counting('ШЭЮ', i, count, 8)
    count = counting('ФЩЪ', i, count, 10)

print(f'Russian: {count}')
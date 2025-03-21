# 66 (КЕГЭ)

"""
Текстовый файл состоит не более чем из 10^(6) латинских символов К, О, Т. Определите максимальное количество подряд идущих комбинаций КОТ.

Для выполнения этого задания следует написать программу.
"""

f = open('24_66.txt')
s = f.readline()
s = s.replace('KOT', '*')
s = s.replace('K', ' ').replace('O', ' ').replace('T', ' ').split()

maxch = 0

for i in range(len(s)):
    if len(s[i]) > maxch:
        maxch = len(s[i])
    
print(maxch)
# Ответ: 75
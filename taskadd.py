"""Дано слово, состоящее только из строчных латинских букв. Проверьте, является ли это слово палиндромом.
Выведите YES или NO.
При решении этой задачи нельзя пользоваться циклами, в решениях на питоне нельзя использовать срезы с шагом,
отличным от 1."""

slovo = str(input('Введите слово строчными латинскими буквами: '))

def Palindrom(s):
    return s[::-1] == s

if Palindrom(slovo):
    print('Yes')
else:
    print('No')
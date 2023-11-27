"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
def compare_str(str1, str2):
    if not type(str1) is str or not type(str2) is str:
        return 0      
    
    len_str1 = len(str1)
    len_str2 = len(str2)

    if len_str1 == len_str2:
        return 1
    elif len_str1 > len_str2:
        return 2
    else:
        return 3 
    
def main():
  print(compare_str(12, "123"))
  print(compare_str("aaa", "aaa"))
  print(compare_str("aaa", "aa"))
  print(compare_str("aa", "aaa"))

if __name__ == "__main__":
    main()

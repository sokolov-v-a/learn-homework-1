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
    if isinstance(str1, str) and isinstance(str2, str):   
      if str1 == str2:
          return 1
      elif str1 != str2 and str2 == 'learn':
          return 3 
      elif str1 != str2 and len(str1) > len(str2):
          return 2      
    else:
       return 0  
    
def main():
  print(compare_str(12, "123"))
  print(compare_str("aaa", "aaa"))
  print(compare_str("aaa", "aa"))
  print(compare_str("aaaa", "learn"))

if __name__ == "__main__":
    main()

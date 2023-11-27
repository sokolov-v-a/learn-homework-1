"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую", "Как погода?": "Солнечно"}

def ask_user(answers_dict):
    while True:
      user_question = input("Введите ваш вопрос: ")
      if user_question in questions_and_answers.keys():
          print(questions_and_answers[user_question])
      elif user_question == "пока":
          print("До встречи!")
          break    
      else:
          print("Затрудняюсь ответить...")    
    
    
if __name__ == "__main__":
    ask_user(questions_and_answers)

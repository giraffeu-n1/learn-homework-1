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

qa = [
    {'question':'Как дела?', 'answer':'Хорошо'},
    {'question':'Что делаешь?', 'answer':'Программирую'},
    {'question':'Какие планы на выходные?', 'answer':'Никаких'},
    {'question':'Как тебя зовут?', 'answer':'Владимир'}
]

def ask_user(answers_dict):
    while True:
        user_question = input('Задайте вопрос')
        for r in qa:
            if user_question == r['question']:
                print(f"{r['answer']}")
        break

if __name__ == "__main__":
    ask_user(qa)

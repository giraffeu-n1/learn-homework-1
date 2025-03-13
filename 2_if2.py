"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные параметры
  и выводя на экран результаты

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    def two_strings(str1,str2):
        str1_type = type(str1)
        str2_type = type(str2)
        str1_len = len(str(str1))
        str2_len = len(str(str2))
        if str1_type is not str or str2_type is not str:
            return 0
        if str1 == str2:
            return 1
        if str1 != str2 and str1_len > str2_len:
            return 2
        if str1 != str2 and str2 == 'learn':
            return 3
    print(two_strings('moscow python',3))
    print(two_strings('moscow python','moscow python'))
    print(two_strings('moscow python','python'))
    print(two_strings('study','learn'))

if __name__ == "__main__":
    main()

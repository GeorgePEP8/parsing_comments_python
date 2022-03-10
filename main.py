"""
Цель: парсировать комментарии из поста группы

Описание:
main.py - основной файл
config.py - храним служебную информацию ( token )
parsing.py - файл с парсингом и сохранением информации

Задачи:
A)
1 - Запрашивать у пользователя короткое  название группы, кол-во комментариев и номер нужного поста
2 - Узнать id группы и id поста
3 - Сохраняем в файлы информацию о постах и комментариях

"""

import json
import vk_api
from config import token
from parsing import get_ip_posts



def main():
    group_name = input("Введите название группы: ")
    count_comments = int(input("Введите кол-во комментариев (не более 100): "))
    number_post = int(input("Введите номер поста (не более 100): "))

    # работаем с файлом parsing.py
    get_ip_posts(group_name, count_comments, number_post)



if __name__ == '__main__':
    main()
# Ближайшие бары



На сайте data.mos.ru есть много разных данных, в том числе список московских баров.

Требуется скачать его в формате json и написать скрипт, который рассчитает:

    самый большой бар;
    самый маленький бар;
    самый близкий бар (текущие gps-координаты ввести с клавиатуры).



# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:
* скачайте json-файл с http://data.mos.ru/opendata/7710881420-bary и распокуйте его;
* запустите python bars.py -f <имя файла>;
* укажите широту и долготу;

```#!bash

$ python bars.py -f <paht_to_json_file>


```

Запуск на Windows происходит аналогично.
Однако перед запуском убедитесь что в cmd стоит кодировка utf-8 (chcp 65001)
# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)

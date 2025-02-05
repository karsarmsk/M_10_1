from threading import Thread
import time
from datetime import datetime

def wite_words(word_count, file_name):

    file = open(file_name, 'w',encoding='utf-8')
    for i in range(word_count):
        file.write(f'Привет! cлово №{i+1}\n')
        time.sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')

time_start = datetime.now()  # Взятие текущего времени
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
# время конца работы функций
time_end = datetime.now()
#  Вывод разницы начала и конца работы функций
time_res = time_end - time_start
print(f'Время работы функций ={time_res}')

time_start = datetime.now()  # Взятие текущего времени
# подготовим потоки

thr_first = Thread(target=wite_words, args=(10, 'example5.txt'))
thr_second = Thread(target=wite_words, args=(30, 'example6.txt'))
thr_third = Thread(target=wite_words, args=(200, 'example7.txt'))
thr_fourth = Thread(target=wite_words, args=(100, 'example8.txt'))

# запускаем потоки
thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()
# ждем завершения потоков
thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()
# время конца работы потоков
time_end = datetime.now()
#  Вывод разницы начала и конца работы потоков
time_res = time_end - time_start
print(f'Время работы потоков ={time_res}')

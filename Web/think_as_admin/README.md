# Название: 
think as admin

# Категория: 
web

# Сообщение: 
Какой способ авторизации использует admin?

# Флаг: 
yetiCTF{g00d_j0b_agent_1s_adm1n}

# Решение: 
curl --url "http://192.168.1.40:5100" --user-agent "admin"

# Запуск:
```
docker build -t agent ./

docker run -p 5100:5100 agent

```

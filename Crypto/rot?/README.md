# Название: 
rot?
# Категория: 
crypto 100
# Сообщение: 
Что это? ZmxhcEpBTXt5MGFfMXpfeTB2YX0=

# Флаг: 
yetiCTF{r0t_1s_r0ot}


# Решение: 
bas64 -> rot7

echo "ZmxhcEpBTXt5MGFfMXpfeTB2YX0=" | base64 -d | tr ‘h-za-gH-ZA-G’ ‘a-zA-Z’

# Baby Reverse

Файл представлял собой бинарник (ELF) собранный через pyinstaller (легко определить по заголовкам).
Собственно вся задача сводилась к распаковке:

```bash=
objcopy --dump-section pydata=pydata.dump file
python pyinstxtractor.py pydata.dump
uncompyle6 file.pyc
```

В исходном коде видно, что программа подставляет в seed параметр PID'a, с которым она запущена. На скрине видно нужный пид.
Подставляем его в seed, запускаем, забираем флаг.

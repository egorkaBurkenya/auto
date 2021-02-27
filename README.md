# MeTerminal beta 0.0.1
Фильтрация ваших файлов


Установка:
```bash 
git clone git@github.com:egorkaBurkenya/auto.git
cd auto
pip install watchdog
```

Первой что вам нужно сделать, запустить `settings.py` и настроить все нужные пути:
```bash
➜  auto git:(master) python3 settings.py
Settings 💻

meTerminal - /mnt/c/Users/Егор/Desktop/meTerminal
docx - /mnt/c/Users/Егор/Documents/Documents
png - /mnt/c/Users/Егор/Pictures
jpg - /mnt/c/Users/Егор/Pictures
jpeg - /mnt/c/Users/Егор/Pictures
py - /mnt/c/Users/Егор/Desktop/coding/python
go - /mnt/c/Users/Егор/Desktop/coding/go
js - /mnt/c/Users/Егор/Desktop/coding/js
default - /mnt/c/Users/Егор/Documents/some Files

if u want to change some path write it`s name:
```
все названия кроме `meTerminal` и `default` - должны являться расширениями файлов

### me
`meTerminal` - ваш терминал для сортировки, создайте папку с таким названием и укажите в настройках путь до него  
программа будет смотреть именно в эту папку

`default` - так же обязательное значение, значение по умолчанию, если Terminal не сможет найти путь до какого либо файла, он отправит его по пути, который будет в `default`

### Запуск
Если вы добавили все желаемые расширения, создали папку meTerminal то можно приступать к запуску программы.

Имееться две версии:
* `sort.py` - разовая сортировка 
* `loopsort.py` - сортировка в фоновом режиме, при создании или при перемещении любого файла в `meTerminal` отсортирует его относительно настроек

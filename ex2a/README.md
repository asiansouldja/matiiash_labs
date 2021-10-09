1. Виконання python .
```shell
2021-10-09 17:14:22.034572
win32
test
```
2. Виконання python . -h
```shell
usage: . [-h] [-o OPT] [-l]

Приклад передачі аргументів у Python програму.

optional arguments:
  -h, --help            show this help message and exit
  -o OPT, --optional OPT
                        Цей параметр є вибірковим.
  -l, --logs            Якщо виконати команду з цим параметром будуть виводитись логи.
```
3.Передаю параметр за допомогою python . -o "Hello world"
````shell
We are in the __main__
2021-10-09 17:14:22.034572
win32
З консолі було передано аргумент
 ========== >> Hello world << ==========
test
````
4. Запускаєм з консолі python . --logs 
```shell
2021-10-09 17:16:12.354291 root INFO: Тут буде просто інформативне повідомлення
2021-10-09 17:16:12.354291 root WARNING: Це Warning повідомлення
2021-10-09 17:16:12.464291 root ERROR: Це повідомлення про помилку
test
```
5. Функція
```shell
def EvenOdd(bool):
    for i in range(0,101):
        if(bool and i % 2 == 0):
            print(i)
        elif(not bool and i % 2 != 0):
            print(i)
```
6. Функція з помилкою, щоб вивелось повідомлення з логуванняM
```shell
def error(x,y):
    try:
        a = x/y
        log.info("Програма виконалась")
        return a
    except Exception as ERROR:
        log.error("Помилка")
```
```shell
2021-10-09 17:44:22.03 root INFO: Програма виконалась
```
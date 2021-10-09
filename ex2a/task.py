#2.i
#Виконуємо виведення констант
print("Перша константа", False)
print("Друга константа", True)
print("Третя константа", None)

print("  ")

#2.ii
#Обираємо будь-яку вбудовану константу та виконуємо звичайні базові приклади за допомогою констант

print(pow(4,5))
print(abs(-45))
print("---------")

#2.iii
#Ознайомлюємось з циклами та пишемо 3 своїх
words=["one","two","three", "four"]
for word in words:
	print(word + " -> ")

print("-------")


for number in range(10):
    if number % 3 == 0:
        print(number)

print("-----")

a = 10
while a < 35:
	print(a)
	a= a + 10


print("-----")

#Демонструємо роботу конструкції  try->except->finally

num1 = 0
num2 = 15
try:
   print("Ділення на 0 ",num2/num1)
except ZeroDivisionError:
	print("Помилка")
finally:
	print("На нуль ділити не можна!")

print("--------")
#2.v
#Робота контекст-менеджера with. Код з ним:

with open("README.md", "r") as test:
    for str in test:
        print(str)

print("------")
#2.vi
#Робота з Python lambdas

x=lambda a,b : a/b
print(x(12,6))
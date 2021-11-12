## Lab_3: Вступ до моніторингу.

1. Створив папку з назвою лабораторної роботи у власному репозиторії ,ініціалізоване середовище pipenv та встановлені необхідні пакети.
2. За допомогою Django Framework створив заготовку проекту та виніс всі створені файли на один рівень вище :
```bash
    pipenv run django-admin startproject my_site
    
    mv my_site/my_site/* my_site/
    mv my_site/manage.py ./
   ``` 
3. Переконався що все встановилось правильно
    ```bash
    pipenv run python manage.py runserver
    ```
4. Створив коміт з базовим темплейтом сайту
5. Cтворив темплейт додатку та коміт із новоствореними файлами темплейту додатка:
    ```bash
    pipenv run python manage.py startapp main
    ```
 6. Створив потрібні папки та файли
 7. Вказав Django frameworks його назву додатку та де шукати веб-сторінки.
 8. Створив .html сторінку та сторінку, яка буде повертати відповідь у форматі JSON;
 9. Результат:
  ```bash
    You are at main page.
    test
```

10. Створив файл monitoring.py та встановив бібліотеку
11. Модифікував функцію health
```bash
def health(request):
    time = datetime.now()
    response = {'date': time.strftime("%Y-%m-%d %H:%M:%S"),
                'storinka': request.build_absolute_uri(),
                'infa_pro_server': os.uname(),
                'infa_pro_clienta': request.headers['User-Agent']}
    return JsonResponse(response)
```
12. Заповнив потрібні файли, перевірив правильність виконання.
13. Закомітив server.log
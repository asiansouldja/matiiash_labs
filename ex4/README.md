# Lab4

1. Ознайомився з Docker
2. Перевірив чи встановлений докер і виконав наступні команди
docker -v
docker -h
docker run docker/whalesay cowsay Docker is fun
Перенаправив вивід цих команд у файл my_work.log закомітив до репозиторію
3. Ознайомився з документацією
4. Виконав команди
sudo docker pull python:3.8-slim
sudo docker images
sudo docker inspect python:3.8-slim
5. Створив власний репозиторій на Docker Hub.
6. Виконав білд імеджа та завантажив його до репозеторію за допомогою команд :
sudo docker build -t arsenmatiiash/lab4:django .
sudo docker images
sudo docker push arsenmatiiash/lab4:django .
Посилання на Docker:https: https://hub.docker.com/repository/docker/arsenmatiiash/lab4
Посилання на скачування імеджа:https://hub.docker.com/layers/arsenmatiiash/lab4/django/images/sha256-046e5e152c50774c37f2935169cf067433cd7c7741331ff15df607a61fb053f7?context=repo
7.Для запуску веб-сайту виконав команду
docker run -it --name=django --rm -p 8000:8000 arsenmatiiash/lab4:django
Сайт працює
8. Створив файл Dockerfile.site
9. Виконав білд даного імеджа docker build -t arsenmatiiash/lab4:latest .
Посилання :https://hub.docker.com/layers/arsenmatiiash/lab4/latest/images/sha256-046e5e152c50774c37f2935169cf067433cd7c7741331ff15df607a61fb053f7?context=repo
10.Переконався,що програма виконується успішно. Виконав команду
sudo docker run -it --rm -p 8000:8000 --net=host arsenmatiiash/lab4:latest
 
 

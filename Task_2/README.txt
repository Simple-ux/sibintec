Я сделал 2 способа решения задачи, за основу взял свое веб-приложение


	1 способ

1. Открыть директорию Case_1 в терминале 
2. ``docker-compose up``
   После запуска контейнеров запустить скрипт
3. ``python access_test.py``
Сервис доступен по адресу localhost:8000



	2 способ
	
Чуть более экспериментальный, хотелось чуть больше это все автоматизировать.
Способ заключвается в том, что один контейнер ослеживает состояние веб-приложения в другом контейнере,и в случае 
наличия проблем перезапускает его. Но, соответственно, отсюда и проблемы.

Контейнер разворачивается долго (первый раз около 2-х минут),
Не удалось нормально проверить работоспособность. Поскольку докер запускается внутри докера, два контейнера в сумме
требуют около 2,5 гб памяти, и у меня из-за нехватки памяти контейнер с приложением постоянно отлетает. 
Второй контейнер, его, правда, сразу же поднимает, но все же. В целом, работает, но с такими вот нюансами.

1. Открыть директорию Case_2 в терминале
2. ``docker-compose up``
Сервис доступен по адресу localhost:8000
    
Скрипт на добавление инн (организаций и частных лиц, являющихся неофициальными огранизациями)
в базу данных через API. Проверке, находятся ли эти номера уже в данной базе. И валидация самого номера инн. <br>
Написан на Flask, Flask RESTful<br>
Для запуска необходимо скачать репозиторий, создать виртуальную среду и установить зависимости командой pip install -r requirements.txt.
<hr>
В 19 строке закомментирована команда создания базы данных. Перед первым запуском скрипта её нужно раскомментировать,
потом можно закомментировать обратно, либо удалить.
<hr>
В файле test.py несколько тестов. Для их работы необходима библиотека requests (pip install requests)
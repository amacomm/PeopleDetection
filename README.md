## Описание
Сервис отмечающий людей на фотографии.  
Фотография отправляется на сервер и возвращается изобраение с отмесеными людьми и их числом на фото.
## Инструкция
Для запуска сервиса запустите manage.py следующей командой `python3 manage.py runserver`. Доступ к серверу откроется через [http://127.0.0.1:8000/](http://127.0.0.1:8000/).  
Для взаимодействия с сервисом:
1. Отправить фотографию на сервер можно при помощи POST запроса `/recognize` с данными в виде словаря:
```JavaScript
{
 "image": ...изображение_в_формате_base64...,
 "name": ...название_файла...
}
```
2. Результат прийдёт в виде json файла содержащего изображение и число людей на нём, обнаруженных на сервере, в следующем виде:
```JavaScript
{
 "image": ...изображение_в_формате_base64...,
 "count": ...число_людей...
}
```
## Замена весов
В ранном сервере используются веса сети yolov3-tiny, для улучшения показателей рекомендуется использовать yolov3 или любые другие веса сети yolo.  
Веса и конфигурационный файл yolov3 можно скачать по ссылкам: [веса](https://pjreddie.com/media/files/yolov3.weights), [cfg](https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg). Данные файлы необходимо разместить в папке `PeopleDetection/PeopleDetect/`.
### P.S.
В папке `PeopleDetection/Test/` находиться скрипт для проверки работы сервера.  
Сервер написан на Python с фреймворком Django. Для работы с изображенем использовались библиотеки OpenCV и сеть YOLOv3.
### Пример работы
![Example1](https://storage.yandexcloud.net/air-soft.dev/people.jpeg)
![Example2](https://s20vlx.storage.yandex.net/rdisk/36105a719f0d247f6f3329103e4dac6a5fbfc9900ad1dcac103d6ea87befd3b0/63152ba7/TL3clQSDeS43yGRv65DrxEMm7JuprX9RVg_LGZqhA8B_ZeJMfDqJ2jYtnjceN7w7z8Rl01rJq97HD-FEOAa7QQ==?uid=0&filename=people.jpeg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=447572&hid=43ea6b3509a95191857cccef2a0fbde3&media_type=image&tknv=v2&etag=a8327edb1261ac10aad9d5fc5ff2b812&rtoken=7yodkzvgGT7M&force_default=no&ycrid=na-1c6815adfbcafd05245ddba8f4af26f4-downloader15e&ts=5e7e1c954f7c0&s=820dc6e3738d468808f42fc8d2abf9bd0f2938c6007b7ddaad4506be74b8f25b&pb=U2FsdGVkX1-17XNi8wjE9BHEwGTJBMdVvZ61p0nE8_VPiP0gbgRAdzpU3491SORzUxmRekzmdkYRLc-X0G9SAHUHCubx1jCGWMBH0P0LiCc)

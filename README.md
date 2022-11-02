# mainslab_test

## Реализовано
- эндпоинт для загрузки и обработки файла bills.csv c валидными данными,
- эндпоинт со списком счетов с возможностью фильтровать и сортировтаь, ;
 
## Не реализовано
- Уникальнссть № счета,
- service в виде отдельной таблицы,

## Запуск
    docker-compose up --build
    docker exec -it *** bash
    alembic upgrade head
    exit

## Endpoints
    Get record:
        /api/bills/
        /api/bills/&orderby=
        /api/bills/&client_name=
        /api/bills/&client_org=
    Upload file:
        /api/bills/uploadfile
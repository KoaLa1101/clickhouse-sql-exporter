# clickhouse-sql-exporter
_clickhouse-sql-exporter_ - это экспортер метрик для ClickHouse, созданный для образовательных целей. Он позволяет собирать и отображать метрики в Prometheus из ClickHouse.

## Установка

Вы можете установить clickhouse-sql-exporter с помощью Docker. Для этого выполните следующие команды:

```docker build -t clickhouse-sql-exporter .
docker run -p 9439:9439 -v /path/to/config:/app/config clickhouse-sql-exporter
```
## Использование
После установки clickhouse-sql-exporter будет доступен по адресу http://localhost:9349/metrics.

## Изменение метрик
Чтобы изменить метрики, необходимо изменить файл queries.json. В этом файле задаются SQL-запросы для получения метрик из ClickHouse.

## Изменение хоста
Чтобы изменить хост, на котором работает ClickHouse, необходимо изменить файл config.json. В этом файле указывается URL и порт ClickHouse.

## Лицензия
Нема

## Контакты
Если у вас есть какие-либо вопросы, вы можете связаться со мной @koala1101
но лучше никогда не писать. Сломал? чини сам!

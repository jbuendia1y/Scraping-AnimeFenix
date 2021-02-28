# Scraping AnimeFenix

App para obtener los animes de AnimeFenix y guardarlos en una base de datos SQL.

La información que se guardará en la base de datos es :

| idAnime | title | poster | url |
| ------- | ----- | ------ | --- |
| 1 | 'Title of Anime' | 'url del Poster del Anime' | 'url del Anime' |

## Paquetes para que funcione la app

```shell
    $ pip install pymysql
```

```shell
    $ pip install selenium
```

```shell
    $ pip install bs4
```

```shell
    $ pip install lxml
```

## Config.py

En el objeto config se deben estar los datos para hacer la conección a la base de datos :

```shell
    config = {
      "host" : host_de_la_db,
      "database" : nombre_de_la_db,
      "user" : usuario_de_la_db,
      "password" : contraseña_del_usuario_de_la_db
    }
```

## Iniciar App

```shell
    python app.py
```

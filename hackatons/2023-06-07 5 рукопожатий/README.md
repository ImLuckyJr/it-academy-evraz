## Хакатон Евраз 1 курс, аффилированные лица через 5 рукопожатий (07.06.2023)

### Устанавливаем библиотеку

`pip install requests`

### Как делать запросы, шаблон

```python
import requests # подключаем библиотеку

# Объект запроса
query = {
    "inn": ""
}

# делаем запрос и получаем данные из него
response = requests.post('https://dev.vdelo.pro/api/hackaton', json=query)
response = response.json()
print(response)
```

### Доступные данные

Компании: `6623134596 ВДЕЛО, 6623141177 ВДЕЛО ДЕВ, 6670318625 РАДИОФОТОНИКА`

### Запросы

1. Получение директоров и учредителей по компании (включая историю)

<a href="https://focus-api.kontur.ru/api3/req/userform" target="_blank">Посмотреть документацию по директорам</a>  (Ищем `heads`)

<a href="https://focus-api.kontur.ru/api3/egrDetails/userform" target="_blank">Посмотреть документацию по учредителям</a>  (Ищем `founders`)

```python
import requests # подключаем библиотеку

# Объект запроса
query = {
    "inn": "6623134596"
}

# делаем запрос и получаем данные из него
response = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query)
response = response.json()
print(response)
```

2. Получение компаний, связанных с человеком

[Посмотреть документацию](https://focus-api.kontur.ru/api3/personAffiliates/req/userform)


```python
import requests # подключаем библиотеку

# Объект запроса
query = {
    "inn": "662345141917"
}

# делаем запрос и получаем данные из него
response = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/person', json=query)
response = response.json()
print(response)
```


3. Получение компаний, связанных с текущей компанией

[Посмотреть документацию](https://focus-api.kontur.ru/api3/companyAffiliates/req/userform)

```python
import requests # подключаем библиотеку

# Объект запроса
query = {
    "inn": "6623134596"
}

# делаем запрос и получаем данные из него
response = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/aff', json=query)
response = response.json()
print(response)
```

# YaMDb project
## Description

YaMDb project collects user's reviews for work titles. YaMDb doesn't keep a works, users can't watch a films or listen to a songs, they can just write a review or leave a comment to review.

Adding a work titles, categories or genres is allowed only for administrators.

Grateful or unpleased users leave text reviews for the works and rate the work in the range from one to ten (an integer); The average grade is forming by using users ratings.

A user can leave only one review per work.
Adding a reviews, comments and grades is allowed only to authenticated users.
## How to launch a project:

>Clone repository and go to directory "api_yamdb"

```
  git clone https://github.com/VitaliiLuki/api_yamdb.git 
  cd api_yamdb
```
>Create and activate virtual environment

```python3 -m venv venv```

```source venv/bin/activate```

>Install all dependencies from requirements.txt

```pip install --upgrade pip```

```pip install -r requirements.txt```

>Launch a manager to fill in DB from existing csv files with data

```cd api_yamdb```

```python3 manage.py load_csv_users```

```python3 manage.py load_csv_reviews```

>Make migrations and launch a project

```python3 manage.py migrate```

```python3 manage.py runserver```

## API Reference

### To watch all endpoint:
  Need to launch a server and go to

  ```/redoc/```

### Below are some requests to available endpoints:

#### To registrate a new user:

```http
  POST /api/v1/auth/signup/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email` | `string` | **Required** |
| `username` | `string` | **Required** |


#### Getting of JWT-token

```http
  POST /api/v1/auth/token/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`      | `string` | **Required** |
| `confirmation_code`      | `string` | **Required** |


#### Getting a list of existing categories

```http
  GET /api/v1/categories/
```

#### Getting a list of existing genres

```http
  GET /api/v1/genres/
```

#### Getting a list of existing work titles

```http
  GET /api/v1/titles/
```

#### Adding a new review to work title

```http
  POST /api/v1/titles/{title_id}/reviews/

```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title_id`      | `integer` | Work title ID (**Required**) |
| `text`      | `string` | Text of review (**Required**) |
| `score`      | `integer` | Grade from 1 to 10 (**Required**) |


#### Adding a comment to review

```http
  POST /api/v1/titles/{title_id}/reviews/{review_id}/comments/

```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title_id`      | `integer` | Work title ID (**Required**) |
| `review_id`      | `integer` | Review ID (**Required**) |
| `text`      | `string` | Text of comment (**Required**) |


## Tech Stack

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)

## Author

- [Riphat Hasanov](https://github.com/UchihaIP)   (Teamlead)
- [Vitalii Lukianov](https://github.com/VitaliiLuki) (Developer)
- [Roman Agiev](https://github.com/Gegins) (Developer)


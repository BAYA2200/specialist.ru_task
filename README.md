
# Настройте свою виртуальную среду для Windows

```bash
python -m venv env 
.\env\Scripts\activate 
cd app
pip install -r requirements.txt 
```
# Если вы используете Linux или macOS, вы вместо этого запустите

```bash
python3 -m venv env 
source ./env/bin/activate
cd app
pip install -r requirements.txt
```

# Создаем и запускаем контейнер(У вас должен быть Docker установлен)

```bash
docker-compose up -d --build
```

# Затем переходим на следующий путь введя его в браузере

```bash
http://localhost:8000/api/schema/swagger-ui/
```

# Для того чтобы создовать посты нужно зарегистрироваться
# нужно перейти на /register/ и нажать в документации
# потом нажать на try it out 
# появиться форма заполняете ёё например так

```bash

{"username":"Xefon",
"email": "xefonzero2101@gmail.com",
"password":"Coolerbay21",
"password_2":"Coolerbay21"}
```

# потом нажимаете на Execute
# теперь мы создали пользователя


# Нужно авторизоваться
# Для этого переходим на /login/
# Также нажимем на try it out 

# И пишем username и пароль
# пример так

```bash
{"username":"Xefon",
"password":"Coolerbay21"}
```

# потом нажимаете на Execute
```bash
И мы получаем токен 
{
  "token": "aee9d43937ac364d07a3fa3cbab7500354795061"
} 
```

# копируем эту часть токена aee9d43937ac364d07a3fa3cbab7500354795061
# документации находим authorise нажимаем

# нахожим tokenAuth (apiKey) и туда под value вводим вот так
```bash
Token aee9d43937ac364d07a3fa3cbab7500354795061
```
# выходим нажимая на кнопку close

# теперь мы можем создовать и изменять свои посты 

# переходим на post /blogposts/
# Также нажимем на try it out

# пишете пост
```bash
{
  "title": "stringxascxasxas",
  "content": "string",
  "is_published": true,
  "user": 1
}
```
# потом нажимаете на Execute
# И у нас создаеться пост

# тепер если мы хотим изменить пост 
# переходим на put /blogposts/
# Также нажимем на try it out

# указываете id своего поста которого хотите изменить 
# например 1

# меняет пост
```bash
{
  "title": "Я поменял пост",
  "content": "string",
  "is_published": true,
  "user": 1
}
```

# потом нажимаете на Execute
# И у нас изменился пост


# для детального просмотра поста тоже нужно указывать id переходим на get /blogpost/{id}/
# для удаление поста нужно быть создателем этого поста или администратором переходим на delete /blogpost/{id}/
# делаем те же самые действия напримере изменения поста 

# на этом все







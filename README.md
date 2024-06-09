# Как запустить на ПК

Выбираем, куда будем кланировать (например на диск B в папку TEST_PROJECT)

```bash
cd /B/TEST_PROJECT
```

Клонируем проект:

```bash
git clone https://github.com/Vettel12/api_yatube-master
```

Заходим в директорию проекта:

```bash
cd /api_yatube-master
```

Устанавливаем виртуальное окружение:

```bash
python -m venv venv
```

Активируем виртуальное окружение:

```bash
source venv/Scripts/activate
```

> Для деактивации виртуального окружения выполним (после работы):
> ```bash
> deactivate
> ```

Устанавливаем зависимости:

```bash
python -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Применяем миграции:

```bash
python yatube/manage.py makemigrations
python yatube/manage.py migrate
```

Для запуска тестов выполним:

```bash
pytest
```

Получим:

```bash
collected 23 items

tests/test_comment.py::TestCommentAPI::test_comments_not_found PASSED                                                                                           [  4%]
tests/test_comment.py::TestCommentAPI::test_comments_get PASSED                                                                                                 [  8%]
tests/test_comment.py::TestCommentAPI::test_comments_create PASSED                                                                                              [ 13%]
tests/test_comment.py::TestCommentAPI::test_comment_get_current PASSED                                                                                          [ 17%]
tests/test_comment.py::TestCommentAPI::test_comment_patch_current PASSED                                                                                        [ 21%]
tests/test_comment.py::TestCommentAPI::test_comment_delete_current PASSED                                                                                       [ 26%]
tests/test_follow.py::TestFollowAPI::test_follow_not_found PASSED                                                                                               [ 30%]
tests/test_follow.py::TestFollowAPI::test_follow_not_auth PASSED                                                                                                [ 34%]
tests/test_follow.py::TestFollowAPI::test_follow_get PASSED                                                                                                     [ 39%]
tests/test_follow.py::TestFollowAPI::test_follow_create PASSED                                                                                                  [ 43%]
tests/test_follow.py::TestFollowAPI::test_follow_search_filter PASSED                                                                                           [ 47%]
tests/test_group.py::TestGroupAPI::test_group_not_found PASSED                                                                                                  [ 52%]
tests/test_group.py::TestGroupAPI::test_group_not_auth PASSED                                                                                                   [ 56%]
tests/test_group.py::TestGroupAPI::test_group_get PASSED                                                                                                        [ 60%]
tests/test_group.py::TestGroupAPI::test_group_create PASSED                                                                                                     [ 65%]
tests/test_group.py::TestGroupAPI::test_group_get_post PASSED                                                                                                   [ 69%]
tests/test_post.py::TestPostAPI::test_post_not_found PASSED                                                                                                     [ 73%]
tests/test_post.py::TestPostAPI::test_post_not_auth PASSED                                                                                                      [ 78%]
tests/test_post.py::TestPostAPI::test_posts_get PASSED                                                                                                          [ 82%]
tests/test_post.py::TestPostAPI::test_post_create PASSED                                                                                                        [ 86%]
tests/test_post.py::TestPostAPI::test_post_get_current PASSED                                                                                                   [ 91%]
tests/test_post.py::TestPostAPI::test_post_patch_current PASSED                                                                                                 [ 95%]
tests/test_post.py::TestPostAPI::test_post_delete_current PASSED                                                                                                [100%]

======================================================================== 23 passed in 14.25s ========================================================================= 
```

Создать суперпользователя:

```bash
python manage.py createsuperuser
```

Запустить проект:

```bash
python manage.py runserver
```

# Примеры запросов API в Postman

Вся информация по работе API по адресу: http://127.0.0.1:8000/redoc/

Получить токен по (POST) запросу: http://127.0.0.1:8000/api/v1/token/

Для получения токена надо ввести username и password (которые вы ранее создали для суперпользователя)

<img width="1000px" src="https://github.com/Vettel12/api_yatube-master/blob/main/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-05-30%20210358+.png?raw=true" align="center" alt="GitHub Readme Stats" />

Ввести в Authorization наш Bearer eyJh*****

Создать пост (POST): http://127.0.0.1:8000/api/v1/posts/

Ввести text и в Value наш текст поста

<img width="1000px" src="https://github.com/Vettel12/api_yatube-master/blob/main/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-05-30%20214854+.png?raw=true" align="center" alt="GitHub Readme Stats" />

Создать комментарий (POST): http://127.0.0.1:8000/api/v1/posts/1/comments/

Ввести post, text и в Value id поста и наш  комментарий

<img width="1000px" src="https://github.com/Vettel12/api_yatube-master/blob/main/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-05-30%20214854+.png?raw=true" align="center" alt="GitHub Readme Stats" />

Обновить комментарий (PUT): http://127.0.0.1:8000/api/v1/posts/1/

Ввести post, text и в Value id поста и наш новый комментарий

<img width="1000px" src="https://github.com/Vettel12/api_yatube-master/blob/main/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-05-30%20214854+.png?raw=true" align="center" alt="GitHub Readme Stats" />

Обновить частично комментарий (PATCH): http://127.0.0.1:8000/api/v1/posts/1/comments/1/

Ввести post, text и в Value id поста и комментарий

<img width="1000px" src="https://github.com/Vettel12/api_yatube-master/blob/main/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-05-30%20214854+.png?raw=true" align="center" alt="GitHub Readme Stats" />
from flask import Flask, render_template, request, jsonify
from utils import PostsHandler
import logging
import pytest

POST_PATH = 'data/posts.json'
COMMENTS_PATH = 'data/comments.json'
BOOKMARKS_PATH = 'data/bookmarks.json'


app = Flask(__name__)

app.config['POST_PATH'] = POST_PATH
app.config['COMMENTS_PATH'] = COMMENTS_PATH
app.config['BOOKMARKS_PATH'] = BOOKMARKS_PATH
app.config['JSON_AS_ASCII'] = False

post_handler = PostsHandler(POST_PATH, COMMENTS_PATH)


@app.route('/')
def index_page():
    """
    Главная страничка, отображает все посты
    """
    posts = post_handler.get_posts_all()
    return render_template('index.html', posts=posts)


@app.route('/posts/<post_id>')
def single_post_page(post_id):
    """
    Страничка отдельного поста
    """
    posts = post_handler.get_posts_by_pk(post_id)
    comments = post_handler.get_comments_by_post_id(post_id)
    return render_template('post.html', posts=posts, comments=comments)


@app.route('/search')
def search_by_query():
    """
    Поиск по ключевому слову
    """
    result = request.args.get('s', '')
    posts = post_handler.search_for_posts(result)

    return render_template('search.html', posts=posts, result=result)


@app.route('/users/<user_name>')
def user_posts_page(user_name):
    """
    Все посты пользователя
    """
    posts = post_handler.get_posts_by_user(user_name)
    return render_template('user-feed.html', posts=posts, user=user_name)


@app.route('/api/posts')
def get_json_posts_all():
    """
    Возвращает список всех постов в виде словаря JSON
    """
    posts = post_handler.get_posts_all()
    logging.basicConfig(
        filename='logs/api.log',
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s'
    )
    print(posts[0].keys())
    return posts


@app.route('/api/posts/<int:post_id>')
def get_json_post_by_id(post_id):
    """
    Возвращает один пост в виде словаря JSON
    """
    post = post_handler.get_posts_by_pk(post_id)
    logging.basicConfig(
        filename='logs/api.log',
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s'
    )

    return post


@app.errorhandler(404)
def page_not_found(e):
    """
    Ошибка 404
    """
    error_num = "Ошибка 404"
    error_dis = "Страница не найдена!"
    return render_template('error_page.html', error_num=error_num, error_dis=error_dis), 404


@app.errorhandler(500)
def server_error_page(e):
    """
    Ошибка 500
    """
    error_num = "Ошибка 500"
    error_dis = "Ошибка сервера"
    return render_template('error_page.html', error_num=error_num, error_dis=error_dis), 500


@pytest.fixture()
def test_client():
    return app.test_client()


def test_get_json_posts_all(test_client):
    response = test_client.get('/api/posts/')
    data = response.json
    assert type(data) == list, "возвращается не список"


if __name__ == '__main__':
    app.run(debug=True)

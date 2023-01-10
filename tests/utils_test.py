import pytest
from utils import PostsHandler

POST_PATH = 'data/posts.json'
COMMENTS_PATH = 'data/comments.json'

posts_handler = PostsHandler(POST_PATH, COMMENTS_PATH)


def test_get_posts_all():
    data = posts_handler.get_posts_all()
    assert type(data) == list, "возвращается не список"


def test_get_comments_all():
    data = posts_handler.get_comments_all()
    assert type(data) == list, "возвращается не список"


def test_get_posts_by_user():
    user_name = ''
    for line in posts_handler.get_posts_all():
        user_name = (line['poster_name'])
        break
    data = posts_handler.get_posts_by_user(user_name)
    assert type(data) == list, "возвращается не список"


def test_get_posts_by_user_value_error():
    with pytest.raises(ValueError):
        posts_handler.get_posts_by_user('')


def test_get_comments_by_post_id():
    post_id = 1
    data = posts_handler.get_comments_by_post_id(post_id)
    assert type(data) == list, "возвращается не список"


def test_get_comments_by_post_id_value_error():
    with pytest.raises(ValueError):
        posts_handler.get_comments_by_post_id(-100)


def test_get_posts_by_pk():
    post_id = 1
    data = posts_handler.get_posts_by_pk(post_id)
    assert type(data) == list, "возвращается не список"


def test_search_for_posts():
    query = ''
    data = posts_handler.search_for_posts(query)
    assert type(data) == list, "возвращается не список"

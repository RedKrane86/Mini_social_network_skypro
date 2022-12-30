import pytest
from main import app


@pytest.fixture()
def test_client():
    return app.test_client()


def test_get_json_posts_all(test_client):
    response = test_client.get('/api/posts')
    data = response.json
    data_keys = data[0].keys()
    keys_to_check = ['poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk']
    assert type(data) == list, "возвращается не список"
    assert set(data_keys) == set(keys_to_check)


def test_get_json_post_by_id(test_client):
    response = test_client.get('/api/posts/1')
    data = response.json
    data_keys = data[0].keys()
    keys_to_check = ['poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk']
    assert type(data[0]) == dict, "возвращается не словарь"
    assert set(data_keys) == set(keys_to_check)

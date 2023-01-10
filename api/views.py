from flask import Blueprint, jsonify
import logging
from utils import PostsHandler

POST_PATH = 'data/posts.json'
COMMENTS_PATH = 'data/comments.json'

api_blueprint = Blueprint('api_blueprint', __name__)
post_handler = PostsHandler(POST_PATH, COMMENTS_PATH)


@api_blueprint.route('/api/posts')
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

    return jsonify(posts)


@api_blueprint.route('/api/posts/<int:post_id>')
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

    return jsonify(post)

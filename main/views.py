from flask import Blueprint, render_template, request
from utils import PostsHandler


POST_PATH = 'data/posts.json'
COMMENTS_PATH = 'data/comments.json'

posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='templates')
post_handler = PostsHandler(POST_PATH, COMMENTS_PATH)


@posts_blueprint.route('/')
def index_page():
    """
    Главная страничка, отображает все посты
    """
    posts = post_handler.get_posts_all()
    return render_template('index.html', posts=posts)


@posts_blueprint.route('/posts/<post_id>')
def single_post_page(post_id):
    """
    Страничка отдельного поста
    """
    posts = post_handler.get_posts_by_pk(post_id)
    comments = post_handler.get_comments_by_post_id(post_id)
    return render_template('post.html', posts=posts, comments=comments)


@posts_blueprint.route('/search')
def search_by_query():
    """
    Поиск по ключевому слову
    """
    result = request.args.get('s', '')
    posts = post_handler.search_for_posts(result)

    return render_template('search.html', posts=posts, result=result)


@posts_blueprint.route('/users/<user_name>')
def user_posts_page(user_name):
    """
    Все посты пользователя
    """
    posts = post_handler.get_posts_by_user(user_name)
    return render_template('user-feed.html', posts=posts, user=user_name)

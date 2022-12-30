import json


class PostsHandler:
    def __init__(self, post_path, comment_path):
        self.post_path = post_path
        self.comment_path = comment_path

    def get_posts_all(self):
        """
        Возвращает все посты
        """
        with open(self.post_path, 'r', encoding='utf-8') as file:
            posts = json.load(file)
        return posts

    def get_comments_all(self):
        """
        Возвращает все комментарии
        """
        with open(self.comment_path, 'r', encoding='utf-8') as file:
            comments = json.load(file)
        return comments

    def get_posts_by_user(self, user_name):
        """
        Возвращает посты указанного пользователя или пустой список, если у пользователя нет постов.
        Вызывает ошибу 'ValueError', если такого пользователя нет
        """
        posts = []
        try:
            for line in self.get_posts_all():
                if user_name.lower() in line['poster_name'].lower():
                    posts.append(line)
            return posts
        except ValueError:
            return f'Пользователя "{user_name}" не существует'

    def get_posts_by_pk(self, pk):
        """
        Возвращает пост по его идентификатору
        """
        posts = []
        for line in self.get_posts_all():
            if int(pk) == line['pk']:
                posts.append(line)
        return posts

    def get_comments_by_post_id(self, post_id):
        """
        Возвращает комментарии указанного поста или пустой список, если у поста нет комментариев.
        Вызывает ошибу 'ValueError', если такого поста нет
        """
        comments = []
        try:
            for line in self.get_comments_all():
                if int(post_id) == line['post_id']:
                    comments.append(line)
            return comments
        except ValueError:
            return f'Поста не существует'

    def search_for_posts(self, query):
        """
        Вызывает список постов по ключевому слову
        """
        posts = []
        for line in self.get_posts_all():
            if query.lower() in line['content'].lower():
                posts.append(line)
        return posts

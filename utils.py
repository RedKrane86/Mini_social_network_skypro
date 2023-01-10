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
        user_name_list = []
        for line in self.get_posts_all():
            if user_name.lower() in line['poster_name'].lower():
                posts.append(line)
                user_name_list.append(line['poster_name'])
        if user_name.lower() not in user_name_list:
            raise ValueError(f'Пользователя {user_name} не существует')
        return posts

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
        post_id_count = 0
        for line in self.get_comments_all():
            if int(post_id) == line['post_id']:
                comments.append(line)
                post_id_count = int(post_id)
        if post_id_count == 0:
            raise ValueError(f'Поста не существует')
        return comments

    def search_for_posts(self, query):
        """
        Вызывает список постов по ключевому слову
        """
        posts = []
        for line in self.get_posts_all():
            if query.lower() in line['content'].lower():
                posts.append(line)
        return posts

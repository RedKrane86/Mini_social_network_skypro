from flask import Flask, render_template
from main.views import posts_blueprint
from api.views import api_blueprint

app = Flask(__name__)

app.register_blueprint(posts_blueprint)
app.register_blueprint(api_blueprint)

app.config['JSON_AS_ASCII'] = False


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


if __name__ == '__main__':
    app.run(debug=True)

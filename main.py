from flask import Flask, render_template, redirect, request, make_response, session, jsonify
from flask_restful import Api
import os

from data import db_session
from data.users import User
from data.forums import Forum
from data.forum_messages import ForumMessage

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/forum1.sqlite")



@app.route('/')
@app.route('/index')
def index():
    session = db_session.create_session()
    print('kkk', session)
    forums = []
    for forum in session.query(Forum).all():
        forums.append((forum.id_forum, forum.title))
        print(forums)
    session.commit()
    return render_template('index.html', forums=forums)


@app.route('/index/<int:id>', methods=['PUT', 'GET', 'POST'])
def index_forum(id):
    """
    Основная страница сайта, открытие одного форума с переданным id
    """
    session = db_session.create_session()
    forum_messages = []
    forums = []
    for forum in session.query(Forum).all():
        forums.append((forum.id_forum, forum.title))
        if forum.id_forum == id:
            for i in forum.messages:
                forum_messages.append((i.user.nickname, i.text))
    session.commit()
    print(forums)
    return render_template('index.html', forums=forums, selection=id, messages=forum_messages)


if __name__ == '__main__':
    main()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

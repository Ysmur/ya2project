import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class ForumMessage(SqlAlchemyBase):
    __tablename__ = 'forumMessages'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    text = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    sender = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id_user"))
    user = orm.relation('User')
    forum = sqlalchemy.Column(sqlalchemy.Integer,
                               sqlalchemy.ForeignKey("forums.id_forum"))
    forums = orm.relation('Forum')

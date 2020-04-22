import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Forum(SqlAlchemyBase):
    __tablename__ = 'forums'

    id_forum = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    messages = orm.relation("ForumMessage", back_populates='forums')

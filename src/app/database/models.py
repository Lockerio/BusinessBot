from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app.database.database import Base


class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)
    is_bot = Column(Boolean)

    messages = relationship('DelayedMessage', back_populates='user')


class MessageTemplate(Base):
    __tablename__ = 'MessageTemplate'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    text = Column(String)
    delay_time = Column(Integer)

    messages = relationship('DelayedMessage', back_populates='template')


class DelayedMessage(Base):
    __tablename__ = 'DelayedMessage'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    message_id = Column(Integer, ForeignKey('MessageTemplate.id'))
    time_to_send = Column(DateTime)

    user = relationship('User', back_populates='messages')
    template = relationship('MessageTemplate', back_populates='messages')

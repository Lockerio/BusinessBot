from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship

from app.database.database import Base


class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, unique=True, nullable=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    username = Column(String, nullable=True)
    is_bot = Column(Boolean)
    registration_date = Column(DateTime, default=func.current_date())

    messages = relationship('DelayedMessage', back_populates='user')


class MessageTemplate(Base):
    __tablename__ = 'MessageTemplate'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=True)
    text = Column(String, nullable=True)
    delay_time = Column(Integer, nullable=True)

    messages = relationship('DelayedMessage', back_populates='template')


class DelayedMessage(Base):
    __tablename__ = 'DelayedMessage'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    message_id = Column(Integer, ForeignKey('MessageTemplate.id'))
    time_to_send = Column(DateTime, nullable=True)

    user = relationship('User', back_populates='messages')
    template = relationship('MessageTemplate', back_populates='messages')

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    channels = relationship("Channel", back_populates="owner")
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)


class Channel(Base):
    __tablename__ = "channels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="channels")

    # Связь с текстовыми и голосовыми комнатами
    text_chats = relationship("TextChat", back_populates="channel")
    voice_rooms = relationship("VoiceRoom", back_populates="channel")


class TextChat(Base):
    __tablename__ = "text_chats"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)  # Имя текстового чата
    channel_id = Column(Integer, ForeignKey("channels.id"))
    channel = relationship("Channel", back_populates="text_chats")

    # Сообщения в текстовом чате
    messages = relationship("Message", back_populates="text_chat")


class VoiceRoom(Base):
    __tablename__ = "voice_rooms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)  # Имя голосовой комнаты
    channel_id = Column(Integer, ForeignKey("channels.id"))
    channel = relationship("Channel", back_populates="voice_rooms")

    # Участники голосовой комнаты
    participants = relationship("User", secondary="voice_room_participants")


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    text_chat_id = Column(Integer, ForeignKey("text_chats.id"))
    text_chat = relationship("TextChat", back_populates="messages")


class VoiceRoomParticipants(Base):
    __tablename__ = "voice_room_participants"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    voice_room_id = Column(Integer, ForeignKey("voice_rooms.id"), primary_key=True)

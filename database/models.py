from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, func
from datetime import datetime


class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = 'book'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey('author.id'), nullable=False)
    genre_id: Mapped[int] = mapped_column(ForeignKey('genre.id'), nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    author: Mapped['Author'] = relationship(back_populates='books')
    genre: Mapped['Genre'] = relationship(back_populates='books')


class Author(Base):
    __tablename__ = 'author'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    books: Mapped[list['Book']] = relationship(back_populates='author')


class Genre(Base):
    __tablename__ = 'genre'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    books: Mapped[list['Book']] = relationship(back_populates='genre')

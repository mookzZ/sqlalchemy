from .models import Book, Author, Genre
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


async def add_author(session: AsyncSession, name: str):
    if not name or not isinstance(name, str):
        raise ValueError("Имя автора должно быть непустой строкой.")

    new_author = Author(name=name)
    session.add(new_author)
    await session.commit()
    return new_author


async def add_genre(session: AsyncSession, name: str):
    if not name or not isinstance(name, str):
        raise ValueError("Название жанра должно быть непустой строкой.")

    new_genre = Genre(name=name)
    session.add(new_genre)
    await session.commit()
    return new_genre


async def add_book(session: AsyncSession, title: str, author_id: int, genre_id: int):
    if not title or not isinstance(title, str):
        raise ValueError("Название книги должно быть непустой строкой.")
    if not isinstance(author_id, int) or author_id <= 0:
        raise ValueError("ID автора должен быть положительным числом.")
    if not isinstance(genre_id, int) or genre_id <= 0:
        raise ValueError("ID жанра должен быть положительным числом.")

    # Проверка существования автора
    author = await session.execute(select(Author).filter_by(id=author_id))
    if not author.scalar_one_or_none():
        raise ValueError(f"Автор с ID {author_id} не найден.")

    # Проверка существования жанра
    genre = await session.execute(select(Genre).filter_by(id=genre_id))
    if not genre.scalar_one_or_none():
        raise ValueError(f"Жанр с ID {genre_id} не найден.")

    new_book = Book(title=title, author_id=author_id, genre_id=genre_id)
    session.add(new_book)
    await session.commit()
    return new_book


async def get_all_books(session: AsyncSession):
    result = await session.execute(select(Book))
    return result.scalars().all()


async def get_book_by_id(session: AsyncSession, book_id: int):
    if not isinstance(book_id, int) or book_id <= 0:
        raise ValueError("ID книги должен быть положительным числом.")

    result = await session.execute(select(Book).filter_by(id=book_id))
    book = result.scalar_one_or_none()
    if not book:
        raise ValueError(f"Книга с ID {book_id} не найдена.")
    return book


async def delete_book_by_id(session: AsyncSession, book_id: int):
    if not isinstance(book_id, int) or book_id <= 0:
        raise ValueError("ID книги должен быть положительным числом.")

    result = await session.execute(select(Book).filter_by(id=book_id))
    book = result.scalar_one_or_none()
    if not book:
        raise ValueError(f"Книга с ID {book_id} не найдена.")

    await session.delete(book)
    await session.commit()
    return True

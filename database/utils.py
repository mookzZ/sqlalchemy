from .models import Book, Author, Genre
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


async def add_author(session: AsyncSession, name: str):
    new_author = Author(name=name)
    session.add(new_author)
    await session.commit()
    return new_author


async def add_genre(session: AsyncSession, name: str):
    new_genre = Genre(name=name)
    session.add(new_genre)
    await session.commit()
    return new_genre


async def add_book(session: AsyncSession, title: str, author_id: int, genre_id: int):
    new_book = Book(title=title, author_id=author_id, genre_id=genre_id)
    session.add(new_book)
    await session.commit()
    return new_book


async def get_all_books(session: AsyncSession):
    result = await session.execute(select(Book).options())
    return result.scalars().all()


async def get_book_by_id(session: AsyncSession, book_id: int):
    result = await session.execute(select(Book).filter_by(id=book_id))
    return result.scalar_one_or_none()


async def delete_book_by_id(session: AsyncSession, book_id: int):
    result = await session.execute(select(Book).filter_by(id=book_id))
    book = result.scalar_one_or_none()
    if book:
        await session.delete(book)
        await session.commit()
        return True
    return False

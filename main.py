import asyncio
from database import async_session, init_db
from database.utils import (
    add_author,
    add_genre,
    add_book,
    get_all_books,
    get_book_by_id,
    delete_book_by_id,
)


async def main():
    await init_db()

    async with async_session() as session:
        author = await add_author(session, "J.K. Rowling")
        genre = await add_genre(session, "Fantasy")
        book = await add_book(session, "Harry Potter", author.id, genre.id)
        books = await get_all_books(session)
        print(f"Список книг: {[book.title for book in books]}")
        book_info = await get_book_by_id(session, book.id)
        if book_info:
            print(f"Информация о книге: {book_info.title}")
        await delete_book_by_id(session, book.id)


if __name__ == "__main__":
    asyncio.run(main())

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

engine = create_async_engine('sqlite+aiosqlite:///books.db', echo=True)
async_session = async_sessionmaker(bind=engine, expire_on_commit=False)

async def init_db():
    from .models import Base
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
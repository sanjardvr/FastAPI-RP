import asyncio
import logging

from src.db.session import SessionLocal
# from src.models.meme import Meme


logging.basicConfig(level=logging.INFO)


logger = logging.getLogger(__name__)


async def create_init_data() -> None:
    async with SessionLocal() as session:
        # db_obj1 = Meme(
        #     submission_id="10rkfto",
        #     submission_title="Stop harassing me for being a Dogecoin Hodler",
        #     submission_url="https://i.redd.it/6bz2r1lgwrfa1.jpg",
        #     permalink="/r/dogecoin/comments/10rkfto/stop_harassing_me_for_being_a_dogecoin_hodler/",
        #     author="HumanbyNature1717",
        #     timestamp=1675324697.0,
        # )

        # session.add(db_obj1)

        await session.commit()


async def main() -> None:
    logger.info("Creating initial data")
    await create_init_data()
    logger.info("Initial data created")


if __name__ == "__main__":
    asyncio.run(main())

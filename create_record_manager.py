import asyncio

from app.constants import RECORD_MANAGER
from langchain.indexes import SQLRecordManager

record_manager = SQLRecordManager(
    namespace="Stardew", db_url=RECORD_MANAGER, async_mode=True
)


async def main():
    await record_manager.acreate_schema()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

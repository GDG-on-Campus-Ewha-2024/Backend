# https://github.com/django/channels/issues/969#issuecomment-596746621
## /mysite/__init__.py

import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
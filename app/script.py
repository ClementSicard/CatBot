import os
import time

import schedule
import telepot
from loguru import logger

if __name__ == "__main__":
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    logger.info(token)

    if token is None:
        logger.critical("TELEGRAM_TOKEN_BOT is not set")
        exit(1)

    bot = telepot.Bot(token)
    bot.sendMessage("YOUR CHAT ID", "Hello World")
    schedule.every(1).minutes.do(
        bot.sendMessage,
        "YOUR CHAT ID",
        "Hello World",
    )

    while True:
        schedule.run_pending()
        time.sleep(1)

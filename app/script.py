import argparse
from datetime import datetime, time
from time import sleep

import telepot
import utils
from consts import (
    EVENING_MESSAGE,
    MORNING_MESSAGE,
    REMINDER_EVENING,
    REMINDER_MORNING,
    TIMEZONE,
)
from loguru import logger


def run():
    TOKEN, CHAT_ID = utils.get_config()
    bot = telepot.Bot(TOKEN)
    logger.success("Bot started")
    logger.debug(f"Args: {args}")
    while True:
        send_reminder(bot, CHAT_ID)
        sleep(60)  # Wait 1 minute before checking again


# Function to send the reminder message
def send_reminder(bot: telepot.Bot, chat_id: str):
    # Get the current time in the specified timezone
    now = datetime.now(tz=TIMEZONE).time()
    now = time(hour=now.hour, minute=now.minute)

    # Check if it's time for the first or second reminder
    if now == REMINDER_MORNING or args["test"]:
        # Construct the reminder message
        logger.info("Sending morning reminder message")
        message = MORNING_MESSAGE
        logger.success("Message sent")
        # Send the message and get the message ID
        bot.sendMessage(
            chat_id,
            message,
            parse_mode="HTML",
        )
    elif now == REMINDER_EVENING:
        logger.info("Sending evening reminder message")
        message = EVENING_MESSAGE
        # Send the message and get the message ID
        bot.sendMessage(
            chat_id,
            message,
            parse_mode="HTML",
        )
        logger.success("Message sent")
    else:
        logger.error("Not time for a reminder yet")


if __name__ == "__main__":
    logger.info("Starting the bot")
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", "-t", action="store_true")
    args = vars(parser.parse_args())
    try:
        run()
    except KeyboardInterrupt:
        logger.critical("Stopping the bot")
        exit()

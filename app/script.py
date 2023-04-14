import argparse
import random
from time import sleep

import schedule
import telepot
import utils
from consts import (
    EVENING_MESSAGE,
    MORNING_MESSAGE,
    REACTION_EMOJIS,
    REMINDER_EVENING,
    REMINDER_MORNING,
)
from loguru import logger


def run():
    TOKEN, CHAT_ID, CHAT_TEST_ID = utils.get_config()
    bot = telepot.Bot(TOKEN)
    logger.success("Bot started")
    logger.debug(f"Args: {args}, CHAT_ID: {CHAT_ID}, TOKEN: {TOKEN}")

    if args["test"]:
        logger.info("Running in test mode")
        # send_reminder(bot, CHAT_ID, morning=True)
        send_reminder(bot, CHAT_TEST_ID, morning=False)
        exit()

    schedule.every().day.at(REMINDER_MORNING.strftime("%H:%M")).do(
        send_reminder,
        bot,
        CHAT_ID,
        morning=True,
    )
    logger.info(f"Morning reminder set to {REMINDER_MORNING.strftime('%H:%M')}")
    schedule.every().day.at(REMINDER_EVENING.strftime("%H:%M")).do(
        send_reminder,
        bot,
        CHAT_ID,
        morning=False,
    )
    logger.info(f"Evening reminder set to {REMINDER_EVENING.strftime('%H:%M')}")

    while True:
        schedule.run_pending()
        sleep(1)


# Function to send the reminder message
def send_reminder(bot: telepot.Bot, chat_id: str, morning: bool = True):
    # Check if it's time for the first or second reminder
    if morning:
        # Construct the reminder message
        logger.info("Sending morning reminder message")
        message = MORNING_MESSAGE
        logger.success("Message sent")
        bot.sendMessage(
            chat_id,
            message.format(*random.choices(REACTION_EMOJIS, k=2)),
            parse_mode="HTML",
        )

    else:
        logger.info("Sending evening reminder message")
        message = EVENING_MESSAGE
        bot.sendMessage(
            chat_id,
            message.format(*random.choices(REACTION_EMOJIS, k=2)),
            parse_mode="HTML",
        )

        logger.success("Message sent")


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

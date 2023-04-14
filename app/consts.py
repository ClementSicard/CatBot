from datetime import time

import pytz

CHAT_ID = "-826697665"
TIMEZONE = pytz.timezone("Europe/Zurich")
REMINDER_MORNING = time(hour=9, minute=36, tzinfo=TIMEZONE)
REMINDER_EVENING = time(hour=18, minute=0, tzinfo=TIMEZONE)

# Telegram reaction emojis
REACTION_EMOJIS = [
    "🫡",
    "❤️",
    "🐳",
    "🗿",
    "🌭",
    "👎",
    "🥰",
    "🕊️",
    "❤️‍🔥",
    "😢",
    "🤗",
    "🔥",
    "🤯",
    "🤷",
    "💅",
    "👍",
    "🆒",
    "👏",
    "😁",
    "🤔",
    "😱",
    "🤬",
    "🎉",
    "🤩",
    "🤮",
    "💩",
    "🙏🏼",
    "👌",
    "🤡",
    "🥱",
    "🥴",
    "😍",
    "🌚",
    "💯",
    "😆",
    "⚡️",
    "🍌",
    "🏆",
    "💔",
    "🤨",
    "😐",
    "🍓",
    "🍾",
    "💋",
    "🖕",
    "😈",
    "😴",
    "😭",
    "🤓",
    "👻",
    "🧑‍💻",
    "👀",
    "🎃",
    "🙈",
    "😇",
    "😨",
    "🤝",
    "✍🏼",
    "🎅🏼",
    "🎄",
    "☃️",
    "🤪",
    "💘",
    "🙉",
    "🦄",
    "😘",
    "💊",
    "🙊",
    "😎",
    "👾",
    "🤷‍♀️",
    "🤷‍♂️",
    "😡",
]


MORNING_MESSAGE = """
<b>🚨 Philippe a FAIM 🙀</b>

Lui donner:
- 1 sachet de bouffe en sauce 🍜
- Y mettre 1 complément en dragées effrité 🍬
- Et 0.5 mL de médicament dans la seringue 💉

<b>Réagissez {} à ce message si vous lui seulement donné à manger, et {} si vous avez\
      lui aussi donné le médicament 🐈🍜</b>
"""

EVENING_MESSAGE = """
<b>🚨 Le poto Philippe commence à avoir les CROCS 🙀</b>

Lui donner:
- 1 sachet de bouffe en sauce 🍜
- Y mettre 1 complément en dragées effrité 🍬
- Et 0.5 mL de médicament dans la seringue 💉

<b>Réagissez {} à ce message si vous lui seulement donné à manger, et {} si vous avez\
      lui aussi donné le médicament 🐈🍜</b>
"""

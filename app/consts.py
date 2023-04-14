from datetime import time

# UTC time
REMINDER_MORNING = time(hour=7, minute=00)
REMINDER_EVENING = time(hour=18, minute=00)

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

Petit <a href="https://drive.google.com/file/d/1tc0Dotgzbx8ana5L_DQmWI5S68qEYLSU/view?usp=share_link">manuel d'utilisation</a> si besoin 📖

<b>Réagissez {} à ce message si vous lui seulement donné à manger, et {} si vous avez lui aussi donné le médicament 🐈🍜</b>
"""

EVENING_MESSAGE = """
<b>🚨 Le poto Philippe commence à avoir les CROCS 🙀</b>

Lui donner:
- 1 sachet de bouffe en sauce 🍜
- Y mettre 1 complément en dragées effrité 🍬
- Et 0.5 mL de médicament dans la seringue 💉

Petit <a href="https://drive.google.com/file/d/1tc0Dotgzbx8ana5L_DQmWI5S68qEYLSU/view?usp=share_link">manuel d'utilisation</a> si besoin 📖

<b>Réagissez {} à ce message si vous lui seulement donné à manger, et {} si vous avez lui aussi donné le médicament 🐈🍜</b>
"""

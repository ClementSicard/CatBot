from datetime import time

import pytz

CHAT_ID = "-826697665"
TIMEZONE = pytz.timezone("Europe/Zurich")
REMINDER_MORNING = time(hour=7, minute=0)
REMINDER_EVENING = time(hour=18, minute=0)


MORNING_MESSAGE = """
<b>🚨 Philippe a FAIM 🙀</b>

🚧 Ne pas oublier la petite 💉 dans la bouche

Mettez une petite réaction "🐳" à ce message si vous lui avez donné à manger 🐈🍜
"""

EVENING_MESSAGE = """
<b>🚨 Le poto Philippe commence à avoir les CROCS 🙀</b>

🚧 Ne pas oublier le medoc

Réagissez avec "🌭" à ce message quand vous lui avez donné à manger 😋🐈
"""

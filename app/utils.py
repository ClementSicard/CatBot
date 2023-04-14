import yaml
from yaml import SafeLoader


def get_config():
    with open("config.yaml") as f:
        config = yaml.load(f, SafeLoader)["config"]

    return config["TELEGRAM_TOKEN"], config["CHAT_ID"], config["CHAT_ID_TEST"]

import slack
import json
import ssl as ssl_lib
import certifi
import random
import os
import configparser
from algorithms import insertion_sort


class Bot(object):
    timestamp = ""
    channel = "sorting-service"
    username = "pi_sorting_service"

    message = {}
    message["channel"] = "sorting-service"
    message["username"] = "pi_sorting_service"

    WELCOME_FILE_PATH = os.path.join(os.path.dirname(__file__), "welcome_message.json")

    with open(WELCOME_FILE_PATH, "r") as welcome_file:
        welcome_blocks = json.loads(welcome_file.read())
    
    def write_message(message, web_client):
        Bot.message["blocks"] = [{"type":"section", "text":{"type":"mrkdwn", "text":f"`{message}`"}}]
        return web_client.chat_postMessage(**Bot.message)

    def generate_numbers():
        return [random.randint(1, 100) for i in range(10)]

    @slack.RTMClient.run_on(event="hello")
    def introduction(**payload):
        web_client = payload["web_client"]
        Bot.message["blocks"] = Bot.welcome_blocks
        response = web_client.chat_postMessage(**Bot.message)

    @slack.RTMClient.run_on(event="message")
    def read_message(**payload):
        data = payload["data"]
        web_client = payload["web_client"]
        text = data.get("text")

        if text and text.lower().startswith("generate:"):
            the_numbers = Bot.generate_numbers()
            Bot.write_message("generated: " + str(the_numbers), web_client)
            Bot.write_message("sorted: " + str(insertion_sort.sort(the_numbers)), web_client)
        
        elif text and text.lower().startswith("sort:"):
            text = text.replace("sort:", "").strip().strip("`")
            if not text.startswith("["):
                text = "[" + text
            
            if not text.endswith("]"):
                text = text + "]"
            
            numbers = json.loads(text)
            Bot.write_message(str(insertion_sort.sort(numbers)), web_client)


def run():
    ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
    
    if not os.path.exists("config.cfg"):
        with open("config.cfg", "w") as c:
            c.write("[Bot]\nbot_slack_token =")

    config = configparser.ConfigParser()
    config.read("config.cfg")
    try:
        slack_token = config["Bot"]["bot_slack_token"]
    
    except KeyError:
        print("Error: no bot_slack_token in config.cfg.")
        return -1

    rtm_client = slack.RTMClient(token=slack_token, ssl=ssl_context)
    print("Created bot.")
    rtm_client.start()
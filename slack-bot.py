import os
import time
import re
from slackclient import SlackClient
import requests
import csv
import utils


slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
starterbot_id = None

RTM_READ_DELAY = 1 
EXAMPLE_COMMAND = "start"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

def download_csv_file(response):
    with open('data.csv', 'w') as f:
        writer = csv.writer(f)
        for line in response.iter_lines():
            writer.writerow(line.decode('utf-8').split(','))

def parse_bot_commands(slack_events):
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            if "files" in event.keys() and "url_private" in event["files"][0].keys():
                url = event["files"][0]["url_private"]
                token = os.environ.get('SLACK_BOT_TOKEN')
                response = requests.get(url, headers={'Authorization': 'Bearer %s' % token})
                download_csv_file(response)

            user_id, message = parse_direct_mention(event["text"])
            if user_id == starterbot_id:
                return message, event["channel"]
    return None, None

def parse_direct_mention(message_text):
    matches = re.search(MENTION_REGEX, message_text)
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

def handle_command(command, channel):
    default_response = "Not sure what you mean. Try *{}*.".format(EXAMPLE_COMMAND)

    
    response = None
    if command.startswith(EXAMPLE_COMMAND):
        response = "Please upload the CSV file as an attachment."

    elif command.startswith("file "):
        response = "Please enter the mode as 'mode <number>'."
    
    elif command.startswith("mode "):
        mode = int(command.split(" ")[1])

        if mode == 1:
            response = "Please input plot type as 'plot <option>'. "



    slack_client.api_call(
        "chat.postMessage",
        channel = channel,
        text = response or default_response
    )

if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Starter Bot connected and running!")
        # Read bot's user ID by calling Web API method `auth.test`
        starterbot_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            command, channel = parse_bot_commands(slack_client.rtm_read())
            if command:
                handle_command(command, channel)
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")
import os
import time
import re
from slackclient import SlackClient
from data_visualization import Visualization
import requests
import csv
import utils
from qna import QnA
import pandas as pd
import io


slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
starterbot_id = None
# globalQ_ID
Q_ID = 0

RTM_READ_DELAY = 1 
EXAMPLE_COMMAND = "start"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

def download_csv_file(response):
    with open('data.csv', 'w') as f:
        writer = csv.writer(f)
        for line in response.iter_lines():
            data = line.decode('utf-8').split(',')
            if (len(data) > 3):
                writer.writerow(data)

def parse_bot_commands(slack_events):
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            # print(event)
            if "files" in event.keys() and "url_private" in event["files"][0].keys() and event["files"][0]['mimetype'] == 'text/csv':
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
    global Q_ID
    flag = False
    default_response = "Not sure what you mean. Try *{}*.".format(EXAMPLE_COMMAND)

    
    response = None
    if command.startswith(EXAMPLE_COMMAND):
        response = "Please upload the CSV file as an attachment."

    elif command.startswith("file"):
        response = "Please enter the mode as 'mode <number>'.\n" + utils.print_mode_options()
    
    elif command.startswith("mode "):
        mode = int(command.split(" ")[1])

        if mode == 3:
            response = utils.print_questions() + "\n Please input question number as 'question <option>'."
        
    elif command.startswith("question "):
        q_id = int(command.split(" ")[1])
        Q_ID = q_id
        if q_id == 1 or q_id == 2 or q_id == 5:
            response = "Please enter the name of category column and variable name as 'options1 <category> <variable_name>'. "

        elif q_id == 4:
            response = "Please enter the name of category column and variable name as 'options2 <category> <variable_name1> <variable_name2>'. "

        elif q_id == 3:
            # response = "Please enter the name of category column and variable name as 'options0'. "
            flag = True
            df = pd.read_csv('data.csv')
            viz = Visualization(df)
            viz.visualize('Heat Map')
            qna = QnA(df, [])
            answer = qna.get_answer(Q_ID, [])
            response = answer + "\nPlease enter the mode as 'mode <number>'.\n" + utils.print_mode_options()


    # elif command.startswith("options0"):
        

    elif command.startswith("options1 "):
        flag = True
        df = pd.read_csv('data.csv')
        viz = Visualization(df)
        cat_var = command.split(" ")[1: ]
        viz.visualize('Violin Plot', cat_var[0], cat_var[1])
        qna = QnA(df, cat_var[0])
        answer = qna.get_answer(Q_ID, [cat_var[1]])
        response = answer + "\nPlease enter the mode as 'mode <number>'.\n" + utils.print_mode_options()

    elif command.startswith("options2 "):
        flag = True
        df = pd.read_csv('data.csv')
        viz = Visualization(df)
        cat_var = command.split(" ")[1: ]
        viz.visualize('Scatter Plot', cat_var[1], cat_var[2], cat_var[0])
        qna = QnA(df, cat_var[0])
        answer = qna.get_answer(Q_ID, cat_var[1:])
        response = answer + "\nPlease enter the mode as 'mode <number>'.\n" + utils.print_mode_options()


    slack_client.api_call(
        "chat.postMessage",
        channel = channel,
        text = response or default_response
        
    )

    if flag:
    # path_to_image = 
        with open('/Users/manvi.goel/Documents/accessible_data_visualizations/plot.png', 'rb') as f:
        # with open('/Users/manvi.goel/Documents/accessible_data_visualizations/plot.png', 'rb', ) as f:
            slack_client.api_call(
                "files.upload",
                channels=channel,
                filename='plot.png',
                title='sampletitle',
                # initial_comment='sampletext',
                file = f.read()
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
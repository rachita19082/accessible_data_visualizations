"""
Helper Functions
"""
from gtts import gTTS
from playsound import playsound

language = 'en'

def map_value(value, min_value, max_value, min_result, max_result):
    result = min_result + (value - min_value)/(max_value - min_value)*(max_result - min_result) + 0.2
    return result

def print_mode_options():
    mode_options = 'How would you like to interact with the data visualization?\n1: Listen to sonified version.\n2: Get summary of the information contained.\n3: Interact through questions.\n4: Exit'
    play_text(mode_options)
    print(mode_options)
    return mode_options

def print_format_options():
    format_options = 'Which type of visualization would you like to see?\n1: Line Plot\n2: Bar Plot\n3: Pie Chart\n4: Heatmap\n5: Scatter Plot\n6: Violin Plot\n7: Other'
    play_text(format_options)
    print(format_options)
    return format_options


def print_questions():
    questions = 'What is your question?\n1: What is the mean of variable1 for each category?\n2: What is the standard deviation of variable1 for each category?\n3: Which variables have the highest correlation?\n4: What is the type of relationship between variable1 and variable2 for each category?\n5: How many outliers are there in variable1 for each category?\n6: Other'
    play_text(questions)
    print(questions)
    return questions

def prompt_input_sonification():
    play_text('Select visualization type')
    viz_type = int(input('Select visualization type: '))
    play_text('Enter name of category column')
    class_name = input('Enter name of category column: ')
    play_text('Enter variable on x-axis')
    var_x = input('Enter variable on x-axis: ')
    play_text('Enter variable on y-axis')
    var_y = input('Enter variable on y-axis: ')
    return viz_type, class_name, var_x, var_y

def prompt_input_summary():
    play_text('Select visualization type')
    viz_type = int(input('Select visualization type: '))
    play_text('Enter name of category column')
    class_name = input('Enter name of category column: ')
    play_text('Enter variable on x-axis')
    var_x = input('Enter variable on x-axis: ')
    return viz_type, class_name, var_x

def prompt_input_qna(q_id):
    vars = []
    class_name = ''
    if q_id == 1 or q_id == 2 or q_id == 5:
        play_text('Enter name of category column')
        class_name = input('Enter name of category column: ')
        play_text('Enter variable1')
        var1 = input('Enter variable1: ')
        vars = [var1]
    elif q_id == 4:
        play_text('Enter name of category column')
        class_name = input('Enter name of category column: ')
        play_text('Enter variable1')
        var1 = input('Enter variable1: ')
        play_text('Enter variable2')
        var2 = input('Enter variable2: ')
        vars = [var1, var2]
    return class_name, vars

def print_sonification_categories(categories):
    all_categories = 'For which category would you like to hear the sonification?'
    i = 1
    for category in categories:
        all_categories = f'{all_categories}\n{i}: {category}'
        i += 1
    all_categories = f'{all_categories}\n{i}: Exit'
    play_text(all_categories)
    print(all_categories)
    return i, all_categories

def play_text(text):
    speech = gTTS(text=text, lang=language, slow=False)
    speech.save('speech.mp3')
    playsound('speech.mp3')




    



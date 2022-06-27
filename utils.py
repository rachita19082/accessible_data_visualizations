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
    speech = gTTS(text=mode_options, lang=language, slow=False)
    speech.save('speech.mp3')
    playsound('speech.mp3')
    print(mode_options)

def print_format_options():
    format_options = 'Which type of visualization would you like to see?\n1: Line Plot\n2: Bar Plot\n3: Pie Chart\n4: Heatmap\n5: Scatter Plot\n6: Violin Plot\n7: Other'
    speech = gTTS(text=format_options, lang=language, slow=False)
    speech.save('speech.mp3')
    playsound('speech.mp3')
    print(format_options)


def print_questions():
    print('1: What is the mean of variable1 for each category?')
    print('2: What is the standard deviation of variable1 for each category?')
    print('3: Which variables have the highest correlation?')
    print('4: What is the type of relationship between variable1 and variable2 for each category?')
    print('5: How many outliers are there in variable1 for each category?')
    print('6: Other')

def prompt_input_sonification():
    viz_type = int(input('Select visualization type: '))
    class_name = input('Enter name of category column: ')
    var_x = input('Enter variable on x-axis: ')
    var_y = input('Enter variable on y-axis: ')
    return viz_type, class_name, var_x, var_y

def prompt_input_summary():
    viz_type = int(input('Select visualization type: '))
    class_name = input('Enter name of category column: ')
    var_x = input('Enter variable on x-axis: ')
    return viz_type, class_name, var_x

def prompt_input_qna(q_id):
    vars = []
    class_name = ''
    if q_id == 1 or q_id == 2 or q_id == 5:
        class_name = input('Enter name of category column: ')
        var1 = input('Enter variable1: ')
        vars = [var1]
    elif q_id == 4:
        class_name = input('Enter name of category column: ')
        var1 = input('Enter variable1: ')
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
    speech = gTTS(text=all_categories, lang=language, slow=False)
    speech.save('speech.mp3')
    playsound('speech.mp3')
    print(all_categories)
    return i




    



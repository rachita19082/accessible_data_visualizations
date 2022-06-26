"""
Helper Functions
"""

def map_value(value, min_value, max_value, min_result, max_result):
    result = min_result + (value - min_value)/(max_value - min_value)*(max_result - min_result) + 0.2
    return result

def print_mode_options():
    print('How would you like to interact with the data visualization?')
    print('1: Listen to sonified version of the visualization.')
    print('2: Get summary of the information contained in the visualization.')
    print('3: Interact with the visualization through questions.')
    print('4: Exit')

def print_format_options():
    print('Which type of visualization would you like to see?')
    print('1: Line Plot')
    print('2: Bar Plot')
    print('3: Pie Chart')
    print('4: Heatmap')
    print('5: Scatter Plot')
    print('6: Violin Plot')
    print('7: Other')

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
    print('For which category would you like to hear the sonification?')
    i = 1
    for category in categories:
        print(f'{i}: {category}')
        i += 1
    print(f'{i}: Exit')
    return i




    



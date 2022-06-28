import pandas as pd
from data_visualization import Visualization
from sonification import Sonification
from summary import Summary
from qna import QnA
import utils
from gtts import gTTS
from playsound import playsound

def main():
    language = 'en'
    utils.play_text('Enter path of CSV file')
    filepath = input('Enter path of CSV file: ')
    df = pd.read_csv(filepath)
    viz = Visualization(df)

    while True:
        utils.print_mode_options()
        utils.play_text('Select mode')
        mode = int(input('Select mode: '))
        if mode == 1:
            utils.print_format_options()
            viz_type, class_name, var_x, var_y = utils.prompt_input_sonification()
            if viz_type == 1:
                viz.visualize('Line Plot', var_x, var_y, class_name)
                sonify = Sonification(df, class_name)
                all_categories = sonify.make_sonifications(vars = [var_x, var_y])
                exit_code, categories = utils.print_sonification_categories(all_categories)
                while True:
                    utils.play_text('Select category')
                    category_int = int(input('Select category: '))
                    if category_int == exit_code:
                        break
                    category = all_categories[category_int-1]
                    sonify.play_plot(category)
        elif mode == 2:
            utils.print_format_options()
            viz_type, class_name, var_x = utils.prompt_input_summary()
            if viz_type == 2:
                viz.visualize('Bar Plot', class_name, var_x)
                summary = Summary(df)
                summ = summary.get_summary()
                utils.play_text(summ)
                print(summ)
        elif mode == 3:
            utils.print_questions()
            utils.play_text('Select question')
            q_id = int(input('Select question: '))
            class_name, vars = utils.prompt_input_qna(q_id)
            if q_id == 3:
                viz.visualize('Heat Map')
            elif q_id == 4:
                viz.visualize('Scatter Plot', vars[0], vars[1], class_name)
            elif q_id == 5:
                viz.visualize('Violin Plot', class_name, vars[0])
            qna = QnA(df, class_name)
            answer = qna.get_answer(q_id, vars)
            utils.play_text(answer)
            print(answer)
        elif mode == 4:
            break

if __name__ == '__main__':
    main()
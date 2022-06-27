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
    intro_speech = gTTS(text='Enter path of CSV file', lang=language, slow=False)
    intro_speech.save('intro.mp3')
    playsound('intro.mp3')
    filepath = input('Enter path of CSV file: ')
    df = pd.read_csv(filepath)
    viz = Visualization(df)

    while True:
        utils.print_mode_options()
        mode = int(input('Select mode: '))
        if mode == 1:
            utils.print_format_options()
            viz_type, class_name, var_x, var_y = utils.prompt_input_sonification()
            if viz_type == 1:
                viz.visualize('Line Plot', var_x, var_y, class_name)
                sonify = Sonification(df, class_name)
                all_categories = sonify.make_sonifications(vars = [var_x, var_y])
                exit_code = utils.print_sonification_categories(all_categories)
                while True:
                    category_int = int(input('Select category: '))
                    if category == exit_code:
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
                summ_speech = gTTS(text=summ, lang=language, slow=False)
                summ_speech.save('summary_speech.mp3')
                playsound('summary_speech.mp3')
                print(summ)
        elif mode == 3:
            utils.print_questions()
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
            answer_speech = gTTS(text=answer, lang=language, slow=False)
            answer_speech.save('answer_speech.mp3')
            playsound('answer_speech.mp3')
            print(answer)
        elif mode == 4:
            break

if __name__ == '__main__':
    main()
import pandas as pd
from sonification import Sonification
from qna import QnA
import utils

def main():
    filepath = input('Enter path of CSV file: ')
    df = pd.read_csv(filepath)

    while True:
        utils.print_mode_options()
        mode = int(input('Select mode: '))
        if mode == 1:
            utils.print_format_options()
            viz_type, class_name, var_x, var_y = utils.prompt_input_sonification()
            #print categories formed
            #input - category name
            if viz_type == 1:
                sonify = Sonification(df, class_name)
                all_categories = sonify.make_sonifications(vars = [var_x, var_y])
                # exit_code = utils.print_sonification_categories(all_categories)
                # while True:
                #     category = int(input('Select category: '))
                #     if category == exit_code:
                #         break
                # sonify.play_plot('West Bengal')
        elif mode == 2:
            pass
        elif mode == 3:
            utils.print_questions()
            q_id = int(input('Select question: '))
            class_name, vars = utils.prompt_input_qna(q_id)
            qna = QnA(df, class_name)
            answer = qna.get_answer(q_id, vars)
            print(answer)
        elif mode == 4:
            break

if __name__ == '__main__':
    main()
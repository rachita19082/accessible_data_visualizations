import pandas as pd
import numpy as np

class QnA:
    questions = {
        1: 'What is the mean of X?',
        2: 'What is the standard deviation of X?',
        3: 'Which variables have the highest correlation?',
        4: 'What is the type of relationship between X and Y variables?',
        5: 'How many outliers are there in X?'
    }

    def __init__(self, df, class_name):
        self.df = df
        self.class_name = class_name
    
    def get_answer(self, q_id, vars=[]):
        if q_id==1:
            answer = self.handle_q1(vars)
        elif q_id==2:
            answer = self.handle_q2(vars)
        elif q_id==3:
            answer = self.handle_q3()
        elif q_id==4:
            answer = self.handle_q4(vars)
        elif q_id==5:
            answer = self.handle_q5(vars)
        return answer

    def handle_q1(self, vars):
        answer = ''
        classes = self.df[self.class_name].unique()
        for category in classes:
            df_class = self.df.loc[self.df[self.class_name] == category]
            mean = df_class[vars].mean()
            answer = f'{answer}The mean {vars[0]} for category {category} is {mean[0]}.\n'
        return answer
    
    def handle_q2(self, vars):
        answer = ''
        classes = self.df[self.class_name].unique()
        for category in classes:
            df_class = self.df.loc[self.df[self.class_name] == category]
            std = df_class[vars].std()
            answer = f'{answer}The standard deviation of {vars[0]} for category {category} is {std[0]}.\n'
        return answer
    
    def handle_q3(self):
        corr_mat = self.df.corr(method='pearson')
        upper_corr_mat = corr_mat.where(np.triu(np.ones(corr_mat.shape), k=1).astype(bool))
        unique_corr_pairs = upper_corr_mat.unstack().dropna()
        sorted_mat = unique_corr_pairs.sort_values(ascending=False)[:1]
        for row in sorted_mat.index:
            var1 = row[0]
            var2 = row[1]
        answer = f'The variables with highest correlation are {var1} and {var2} and their correlation is {sorted_mat[0]}.'
        return answer

    def handle_q4(self, vars):
        answer = ''
        classes = self.df[self.class_name].unique()
        for category in classes:
            df_class = self.df.loc[self.df[self.class_name] == category]
            corr = df_class[vars[0]].corr(df_class[vars[1]])
            if corr>0 and abs(corr)>0.5:
                answer = f'{answer}There is Strong Positive Correlation between {vars[0]} and {vars[1]} for category {category}.\n'
            elif corr>0 and abs(corr)<=0.5:
                answer = f'{answer}There is Weak Positive Correlation between {vars[0]} and {vars[1]} for category {category}.\n' 
            elif corr<0 and abs(corr)>0.5:
                answer = f'{answer}There is Strong Negative Correlation between {vars[0]} and {vars[1]} for category {category}.\n' 
            else:
                answer = f'{answer}There is Weak Negative Correlation between {vars[0]} and {vars[1]} for category {category}.\n'
        return answer
    
    def handle_q5(self, vars):
        answer = ''
        classes = self.df[self.class_name].unique()
        for category in classes:
            df_class = self.df.loc[self.df[self.class_name] == category]
            Q1 = df_class[vars].quantile(0.25)
            Q3 = df_class[vars].quantile(0.75)
            IQR = Q3 - Q1
            df2 = df_class[~((df_class[vars] < (Q1 - 1.5 * IQR)) |(df_class[vars] > (Q3 + 1.5 * IQR))).any(axis=1)]
            percentage = (df2.shape[0]/df_class.shape[0])*100
            percentage = round(percentage, 2)
            answer = f'{answer}The percentage of outliers in {vars[0]} is {percentage} for category {category}.\n'
        return answer

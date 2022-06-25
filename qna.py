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

    def __init__(self, df):
        self.df = df
    
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

    def handle_q1(self, vars):
        mean = self.df[vars].mean()
        answer = f'The mean {vars[0]} is {mean[0]}.'
        print(answer)
        return answer
    
    def handle_q2(self, vars):
        std = self.df[vars].std()
        answer = f'The standard deviation of {vars[0]} is {std[0]}.'
        print(answer)
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
        print(answer)
        return answer

    def handle_q4(self, vars):
        corr = df[vars[0]].corr(df[vars[1]])

        if corr>0 and abs(corr)>0.5:
            answer = f'There is Strong Positive Correlation between {vars[0]} and {vars[1]}.'
        elif corr>0 and abs(corr)<=0.5:
            answer = f'There is Weak Positive Correlation between {vars[0]} and {vars[1]}.' 
        elif corr<0 and abs(corr)>0.5:
            answer = f'There is Strong Negative Correlation between {vars[0]} and {vars[1]}.' 
        else:
            answer = f'There is Weak Negative Correlation between {vars[0]} and {vars[1]}.' 
        print(answer)
        return answer
    
    def handle_q5(self, vars):
        Q1 = self.df[vars].quantile(0.25)
        Q3 = self.df[vars].quantile(0.75)
        IQR = Q3 - Q1
        df2 = self.df[~((df[vars] < (Q1 - 1.5 * IQR)) |(self.df[vars] > (Q3 + 1.5 * IQR))).any(axis=1)]
        percentage = (df2.shape[0]/self.df.shape[0])*100
        percentage = round(percentage, 2)
        answer = f'The percentage of outliers in {vars[0]} is {percentage}.'
        print(answer)
        return answer



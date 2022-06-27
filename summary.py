import pandas as pd


class Summary:
	def __init__(self, dataframe, graph='Bar Plot'):
		self.df= dataframe

	def get_summary(self):
		df1 = self.df.iloc[:, [1]]
		mean = df1.mean()
		name = str(mean).split()[0]
		median = df1.median()
		mode = df1.mode()
		max = df1.max()
		min = df1.min()
		answer = '\nThe mean of ' + name + ' is '+ str(mean).split()[1] + '.\nThe median of ' + name + ' is ' +str(median).split()[1] + '.\nThe mode of ' + name + ' is '+ str(mode).split()[1] + '.\nThe maximum and minimum value of ' + name + ' is '+ str(max).split()[1] +' and '+ str(min).split()[1]+' respectively.\n'
		return answer

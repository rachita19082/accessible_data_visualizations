import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

class Visualization:
    def __init__(self, data):
        self.data = data

    def visualize(self, plot_type, X= None, Y=None, category=None):
        if(plot_type == "Bar Plot"):
            self.barPlot_visualize(X, Y)
        elif(plot_type == "Line Plot"):
            self.linePlot_visualize(X, Y, category)
        elif(plot_type == "Scatter Plot"):
            self.scatterPlot_visualize(X, Y, category)
        elif(plot_type == "Heat Map"):
            self.heatMap_visualize()
        elif(plot_type == "Violin Plot"):
            self.violinPlot_visualize(X, Y)
        else:
            print("Plot is not supported. Supported Plots: Bar Plot, Line Plot, Scatter Plot, Heat Map, Scatter Plot")

    def barPlot_visualize(self, X, Y):
        self.setup()
        dataset= self.data
        p= sns.barplot(x = X, y = Y, data = dataset)
        p.set_title("Bar Plot", fontsize = 70)
        hatches = ['-', '+', 'x', '\\', '*', 'o']
        for i,thisbar in enumerate(p.patches):
            thisbar.set_hatch(hatches[i])
        ax= plt.subplot(111)
        plt.yticks(np.arange(int(ax.get_ylim()[0]),ax.get_ylim()[1], 5))
        self.show(p, X, Y)

    def linePlot_visualize(self, X, Y, category):
        self.setup()
        dataset = self.data
        p= sns.lineplot(x=X, y=Y, hue=category, style=category, data=dataset, markers=True, markersize=30)
        p.set_title("Line Plot", fontsize = 70)
        self.show(p, X, Y)

    def scatterPlot_visualize(self, X, Y, category):
        self.setup()
        color= sns.color_palette("colorblind", as_cmap= True)
        dataset = self.data
        p= sns.scatterplot(x= X, y=Y,data=dataset, hue=category, style=category, s=300, cmap= color)
        p.set_title("Scatter Plot", fontsize = 70)
        self.show(p, X, Y)

    def heatMap_visualize(self):
        self.setup()
        color= sns.color_palette("colorblind", as_cmap= True)
        dataset = self.data  
        linewidths = 2
        linecolor = "yellow"
        corrMatrix = dataset.corr()
        p= sns.heatmap(corrMatrix,linewidths=linewidths,linecolor=linecolor, cmap= color, annot=True)
        p.set_title("Heat Map", fontsize = 70)
        plt.show()

    def violinPlot_visualize(self, X, Y):
        self.setup()
        color= sns.color_palette("colorblind", as_cmap= True)
        dataset = self.data  
        p= sns.violinplot(x = X, y = Y, data = dataset, cmap= color)
        p.set_title("Violin Plot", fontsize = 70)
        self.show(p, X, Y)
        
    def setup(self):
        plt.figure(figsize=(40, 18))
        sns.set(font_scale = 4)
        sns.set_theme(style="whitegrid")
        sns.color_palette("colorblind", as_cmap= True)
        sns.set(font_scale = 3)
        
    def show(self, p, X, Y):
        p.set_xlabel(X, fontsize = 60)
        p.set_ylabel(Y, fontsize = 60)
        plt.legend(markerscale=4)
        plt.show()
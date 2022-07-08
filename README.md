# Acc-Viz

Acc-Viz is a utility which makes data visualizations more accessible for the partially sighted, visually impaired and blind. 
This video demonstrates the basic functions on Acc-Viz. 
[Video](https://user-images.githubusercontent.com/55682355/177938225-5c8f76ee-2fa9-4c79-a261-4db9fc3a9f70.mp4)

## About the Project

### Use Case




Data Visualization, such as statistical charts, pie charts, graphs, plots etc., helps effectively represent, analyze and explore data. Also, it identifies and shares meaningful data-driven insights that are hard to decipher by just looking at the data values. 

People with visual disabilities face many challenges in accessing data visualizations. Data for many important matters such as health, election outcomes and economic indications are presented in the form of graphs and plots. But, interpreting insights from such data visualizations becomes an incredibly difficult task for people with low vision or colourblindness. The visualization research community has not paid enough attention to the needs of people with disabilities. For instance, W3C guidelines recommend that online graphics provide alt text and an alternative text description. In practice, however, alt text is frequently missing or inadequate. And even though many figures provide detailed text descriptions, they are not enough for in-depth data analysis. Screen readers are also unable to give a detailed overview or summary of the complex data relationships represented through charts. 

There is a pressing need to prioritize accessibility and inclusive approaches while employing visualizations adequately.


### Methodology

Acc-Viz has been developed as a python module which can be easily installed and integrated with all software to enable the visually impaired to access all the data visualizations provided by the software. The functionalities and features provided are described below. 

#### Modularity via principles of object-oriented programming
The code is highly modular and all the features which are integrated into one here can easily be separately used by developers to incorporate accessibility into their softwares. 

#### Accessible Data Visualizations
The visualizations we create have been developed keeping in mind the problems faced by the color blind and partially sighted. They have the following . . . . features :

 * Large font size of headings and labels
 * Color-blind pallette to apply easily distinguishable colors to legends
 * Texture added to plots to clearly distinguish different classes
 * Large marker-size for plotted points
 * More labels on x and y axis to make it easier to read values

In order to create the visualizations, an instance of `class Visualization` is created which simply calls the method `visualize()` with the parameters type of plot, variables on x and y axis to create an accessible visualization of the data.

#### Data Sonification
In order to make the visualizations more accessible to the visually-impaired, we map the data in the visualization to a musical scale, enabling listeners to interpret possible data trends or patterns.

In order to create the sonifications, an instance of `class Sonification` is created which calls the method `make_sonifications()` with the parameters type of plot, variables on x and y axis to create sonified version of the visualization. Then the method `play_plot()` takes a category as parameter and plays the sonifications for the chosen category.

#### Question and Answer Mode
In order to make information about data which can easily be inferred by looking at the visualization accessible for the visually impaired used, we included the question and answer mode. In this mode, the user can interact with the data through predefined or custom questions and gain insights about the data.
Some of the questions available are:

* What is the mean of X?
* What is the standard deviation of X?
* Which variables have the highest correlation?
* What is the type of relationship between X and Y variables?
* How many outliers are there in X?

#### Summary

The summary mode offers a verbal summary of the information contained in the visualization.

#### Slack Integration

For users who only need to interact with the data visualization and gain insights from it, we have created a slack bot acc-viz which provides all the above functionality.

## Getting Started

Acc-Viz is a python module which can easily be installed and integrated with all software. Use the following instructions to install the package.

### Dependencies

Please ensure that you have >=Python 3.7 and pip installed on your machine.

### Installation

1. Clone the repo

   ```sh
   git clone https://github.com/rachita19082/accessible_data_visualizations.git
   ```
2. Change to project directory

    ```sh
   cd accessible-data-visualizations
   ```
3. Install required packages

   ```sh
   pip install .
   ```
4. Run the program

   ```sh
   python3 main.py
   ```

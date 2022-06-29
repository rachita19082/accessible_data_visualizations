# accessible_data_visualizations

Acc-Viz is a utility which makes data visualizations more accessible for the partially sighted, visually impaired and blind.

## About the Project

### Use Case

(Include problem statement and current solutions)

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

## Usage Example

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)
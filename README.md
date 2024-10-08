# Datascience-X-Logistic-Regression
This project tackles the challenge of implementing a multi-class logistic regression model, inspired by a whimsical scenario in the world of Harry Potter, to classify Hogwarts houses. The goal is to analyze, visualize, and predict data efficiently using various Python scripts.
## Project Structure
The project is divided into three main folders:

### DataAnalysis
- describe.py: A script to perform data analysis. It prompts the user to select four features (or subjects) to analyze and displays key statistical measures for these features.
### DataVisualization
- histogram.py: Generates a histogram to explore the distribution of scores across the four Hogwarts houses.
- pair_plot.py: Creates a pair plot to visually assess relationships between pairs of features.
- scatter_plot.py: Plots scatter plots to identify similarities between two chosen features.
### LogisticRegression
- logreg_train.py: Trains the logistic regression model using a gradient descent algorithm. This script saves the model weights for prediction purposes.
- logreg_predict.py: Utilizes the trained weights to predict the Hogwarts house for each student in a test dataset.
- logreg_accuracy.py: Calculates the accuracy of the logistic regression model based on its predictions.
## Installation
To get started, clone the repository and make sure you have Python installed along with the necessary libraries such as NumPy, Pandas, and Matplotlib.
```
git clone git@github.com:Maeltarh/Datascience-X-Logistic-Regression.git
cd Datascience-X-Logistic-Regression
```
## Usage
### Data Analysis:
Run describe.py to get statistics on specific features.
```
python DataAnalysis/describe.py
```
### Data Visualization:
Create different plots for data exploration:

Histogram:
```
python DataVisualization/histogram.py
```
Pair Plot:
```
python DataVisualization/pair_plot.py
```
Scatter Plot:
```
python DataVisualization/scatter_plot.py
```
### Logistic Regression:
Train and test the model with logistic regression:

Training:
```
python LogisticRegression/logreg_train.py
```
Prediction:
```
python LogisticRegression/logreg_predict.py
```
Evaluate Accuracy:
```
python LogisticRegression/logreg_accuracy.py
```
## Requirements
Recent version of python 3
### Libraries:
- json: For handling JSON data.
- pandas: For data manipulation and analysis.
- matplotlib: For data visualization.
- numpy: For numerical operations.
- subprocess: For managing system processes.
- scikit-learn (StandardScaler, MinMaxScaler): For feature scaling.
- seaborn: For enhanced data visualization.
You can install these libraries using:
```
pip install json pandas matplotlib numpy subprocess scikit-learn seaborn
```
Or:
```
python3 -m pip install json pandas matplotlib numpy subprocess scikit-learn seaborn
```

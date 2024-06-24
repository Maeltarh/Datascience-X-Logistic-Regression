# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pair_plot.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mhugueno <mhugueno@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/20 21:18:10 by mhugueno          #+#    #+#              #
#    Updated: 2024/06/07 22:07:26 by mhugueno         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def remove_extreme_values_by_group(df, group_col):
    cleaned_groups = []
    for house, group in df.groupby(group_col):
        for col in group.select_dtypes(include=[np.number]).columns:
            Q1 = group[col].quantile(0.25)
            Q3 = group[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            group = group[(group[col] >= lower_bound) & (group[col] <= upper_bound)]
        cleaned_groups.append(group)
    return pd.concat(cleaned_groups)


def fileRead(file_path):
    df = pd.read_csv(file_path)
    return df


def display(df):
    palette = {'Gryffindor': 'red', 'Slytherin': 'green', 'Hufflepuff': 'blue', 'Ravenclaw': 'orange'}
    scatter_matrix = sns.pairplot(df.dropna(), hue='Hogwarts House', diag_kind='kde', palette=palette)
    plt.show()

def main():
    df = fileRead('../datasets/dataset_train.csv')
    df = remove_extreme_values_by_group(df, "Hogwarts House")
    display(df)


if __name__ == "__main__":
    main()

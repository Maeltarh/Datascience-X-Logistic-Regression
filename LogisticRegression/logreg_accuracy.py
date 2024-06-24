# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logreg_accuracy.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mhugueno <mhugueno@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/04 20:57:17 by mhugueno          #+#    #+#              #
#    Updated: 2024/06/16 17:22:54 by mhugueno         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import pandas as pd
import numpy as np
import json
from sklearn.preprocessing import StandardScaler, MinMaxScaler


def fileReadDf(file_path):
    df = pd.read_csv(file_path)
    return df


def fileReadJson(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data.get("result")


def calcAccuracy(df, result):
    count = 0
    r = 0
    s = 0
    g = 0
    h = 0
    for i in range(len(df)):
        row = df.iloc[i]
        if (row["Hogwarts House"] == result[i]):
            count += 1
        else:
            if (row["Hogwarts House"] == "Ravenclaw"):
                r += 1
            if (row["Hogwarts House"] == "Slytherin"):
                s += 1
            if (row["Hogwarts House"] == "Gryffindor"):
                g += 1
            if (row["Hogwarts House"] == "Hufflepuff"):
                h += 1
            print(i, row["Hogwarts House"], result[i])
    print((count / len(df))* 100, r, s, g, h)


def fillmeupdaddy(df, df_stats):
    for subject in df_stats['Name']:
        median_value = df_stats.loc[df_stats['Name'] == subject, '50%'].values[0]
        df[subject] = df[subject].fillna(median_value)
    return df


def main():
    df = fileReadDf("../datasets/dataset_train.csv")
    result = fileReadJson("data.json")
    calcAccuracy(df, result)

if __name__ == "__main__":
    main()

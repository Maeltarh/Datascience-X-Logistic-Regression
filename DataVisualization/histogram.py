# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    histogram.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mhugueno <mhugueno@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/18 20:39:31 by mhugueno          #+#    #+#              #
#    Updated: 2024/05/20 22:19:11 by mhugueno         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calcCount(df, dict_list):
    for column_name in df.columns:
        dict_list["Name"].append(column_name)
        count = 0
        y = 0
        for value in df[column_name]:
            if pd.notna(value):
                if df["Hogwarts House"][y] in dict_list["House"]:
                    count += 1
            y += 1
        dict_list["Count"].append(count)


def calcMean(df, df_bis, dict_list):
    i = 0
    for column_name in df.columns:
        Mean = 0
        y = 0
        for value in df[column_name]:
            if pd.notna(value):
                if isinstance(value, (int, np.integer, float, np.floating, complex, np.complexfloating)):
                    if df["Hogwarts House"][y] in dict_list["House"]:
                        Mean += value
            y += 1
        Mean = Mean / dict_list["Count"][i]
        val = df_bis["Max"][i] - df_bis["Min"][i]
        if Mean >= 0 and df_bis["Min"][i] < 0:
            Mean = Mean + df_bis["Min"][i]
        else:
            Mean = Mean - df_bis["Min"][i]
        Mean = (Mean / val) * 100
        if Mean < 0:
            Mean *= -1
        if Mean != 0:
            dict_list["Mean"].append(Mean)
        else:
            dict_list["Mean"].append("NaN")
        i += 1


def calcIndex(Ravenclaw_dict, Hufflepuff_dict, Slytherin_dict, Gryffindor_dict):
    i = 6
    values = [int(Ravenclaw_dict["Mean"][6]), int(Hufflepuff_dict["Mean"][6]), int(Slytherin_dict["Mean"][6]), int(Gryffindor_dict["Mean"][6])]
    tmp = (max(values) - min(values))
    index = 6
    for i in range(18):
        if pd.notna(Ravenclaw_dict["Mean"][i]):
            values = [int(Ravenclaw_dict["Mean"][i]), int(Hufflepuff_dict["Mean"][i]), int(Slytherin_dict["Mean"][i]), int(Gryffindor_dict["Mean"][i])]
            if (max(values) - min(values)) < tmp:
                tmp = (max(values) - min(values))
                index = i
        i += 1
    return index


def displayHisto(Ravenclaw_dict, Hufflepuff_dict, Slytherin_dict, Gryffindor_dict, index):
    valeurs = [Ravenclaw_dict["Mean"][index], Hufflepuff_dict["Mean"][index], Slytherin_dict["Mean"][index], Gryffindor_dict["Mean"][index]]
    labels = ['Ravenclaw', 'Hufflepuff', 'Slytherin', 'Gryffindor']
    plt.figure(figsize=(8, 4))
    plt.bar(labels, valeurs, color=['blue', 'yellow', 'green', 'red'])
    plt.title(Ravenclaw_dict["Name"][index])
    plt.xlabel('Catégories')
    plt.ylabel('Valeurs')
    lower_limit = min(valeurs) - abs(min(valeurs) * 0.1)
    upper_limit = max(valeurs) + abs(max(valeurs) * 0.1)
    plt.ylim(lower_limit, upper_limit)
    plt.show()


def fileRead(file_path):
    df = pd.read_csv(file_path)
    return df


def main():
    df = fileRead('../datasets/dataset_train.csv')
    df_bis = fileRead('../DataAnalysis/result.csv')
    Ravenclaw_dict = {
        "House": ["Ravenclaw"],
        "Name": [],
        "Count": [],
        "Mean": [],
    }
    Hufflepuff_dict = {
        "House": ["Hufflepuff"],
        "Name": [],
        "Count": [],
        "Mean": []
    }
    Slytherin_dict = {
        "House": ["Slytherin"],
        "Name": [],
        "Count": [],
        "Mean": []
    }
    Gryffindor_dict = {
        "House": ["Gryffindor"],
        "Name": [],
        "Count": [],
        "Mean": []
    }
    calcCount(df, Ravenclaw_dict)
    calcMean(df, df_bis, Ravenclaw_dict)
    calcCount(df, Hufflepuff_dict)
    calcMean(df, df_bis, Hufflepuff_dict)
    calcCount(df, Slytherin_dict)
    calcMean(df, df_bis, Slytherin_dict)
    calcCount(df, Gryffindor_dict)
    calcMean(df, df_bis, Gryffindor_dict)
    i = 0
    for value in Ravenclaw_dict["Name"]:
        print(i, " : ", value)
        i += 1
    while True:
        try:
            index = input(f"Which of the {len(Ravenclaw_dict['Name'])} course do you want to see ? : ")
            index = int(index)
            if (index < 6 or index > len(Ravenclaw_dict['Name']) - 1):
                raise ValueError
            displayHisto(Ravenclaw_dict, Hufflepuff_dict, Slytherin_dict, Gryffindor_dict, index)
            break
        except ValueError:
            if index == "answer":
                index = calcIndex(Ravenclaw_dict, Hufflepuff_dict, Slytherin_dict, Gryffindor_dict)
                displayHisto(Ravenclaw_dict, Hufflepuff_dict, Slytherin_dict, Gryffindor_dict, index)
                break
            print("Input must be a number and in the range of avaible data.")


if __name__ == "__main__":
    main()

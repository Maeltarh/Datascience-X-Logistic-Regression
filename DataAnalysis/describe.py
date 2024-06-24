# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    describe.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mhugueno <mhugueno@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/18 20:39:39 by mhugueno          #+#    #+#              #
#    Updated: 2024/05/20 22:17:48 by mhugueno         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import numpy as np


def calcCount(df, dict_list):
    for column_name in df.columns:
        dict_list["Name"].append(column_name)
        empty = 0
        for value in df[column_name]:
            if pd.notna(value):
                pass
            else:
                empty += 1
        dict_list["Count"].append((len(df[column_name]) - empty))


def calcMean(df, dict_list):
    i = 0
    for column_name in df.columns:
        Mean = 0
        for value in df[column_name]:
            if pd.notna(value):
                if isinstance(value, (int, np.integer, float, np.floating, complex, np.complexfloating)):
                    Mean += value
        Mean = Mean / dict_list["Count"][i]
        if Mean != 0:
            dict_list["Mean"].append(Mean)
        else:
            dict_list["Mean"].append("NaN")
        i += 1


def calcStd(df, dict_list):
    i = 0
    for column_name in df.columns:
        std = 0
        for value in df[column_name]:
            if pd.notna(value):
                if isinstance(value, (int, np.integer, float, np.floating, complex, np.complexfloating)):
                    std += (value - dict_list["Mean"][i]) ** 2
        std = std / dict_list["Count"][i]
        std = std ** 0.5
        if std != 0:
            dict_list["Std"].append(std)
        else:
            dict_list["Std"].append("NaN")
        i += 1


def calcMin(df, dict_list):
    for column_name in df.columns:
        min = df[column_name][1]
        for value in df[column_name]:
            if isinstance(value, (int, np.integer, float, np.floating, complex, np.complexfloating)):
                if value < min:
                    min = value
        if isinstance(min, (int, np.integer, float, np.floating, complex, np.complexfloating)):
            dict_list["Min"].append(min)
        else:
            dict_list["Min"].append("NaN")


def calc25(df, dict_list):
    i = 0
    for column_name in df.columns:
        if isinstance(df[column_name][1], (int, np.integer, float, np.floating, complex, np.complexfloating)):
            liste = sorted(df[column_name][df[column_name].notna() & (df[column_name] != '')])
            index = dict_list["Count"][i] * 0.25
            centile = liste[int(index)]
            dict_list["25%"].append(centile)
        else:
            dict_list["25%"].append("NaN")
        i += 1


def calc50(df, dict_list):
    i = 0
    for column_name in df.columns:
        if isinstance(df[column_name][1], (int, np.integer, float, np.floating, complex, np.complexfloating)):
            liste = sorted(df[column_name][df[column_name].notna() & (df[column_name] != '')])
            index = dict_list["Count"][i] * 0.50
            centile = liste[int(index)]
            dict_list["50%"].append(centile)
        else:
            dict_list["50%"].append("NaN")
        i += 1


def calc75(df, dict_list):
    i = 0
    for column_name in df.columns:
        if isinstance(df[column_name][1], (int, np.integer, float, np.floating, complex, np.complexfloating)):
            liste = sorted(df[column_name][df[column_name].notna() & (df[column_name] != '')])
            index = dict_list["Count"][i] * 0.75
            centile = liste[int(index)]
            dict_list["75%"].append(centile)
        else:
            dict_list["75%"].append("NaN")
        i += 1


def calcMax(df, dict_list):
    for column_name in df.columns:
        max = df[column_name][1]
        for value in df[column_name]:
            if isinstance(value, (int, np.integer, float, np.floating, complex, np.complexfloating)):
                if value > max:
                    max = value
        if isinstance(max, (int, np.integer, float, np.floating, complex, np.complexfloating)):
            dict_list["Max"].append(max)
        else:
            dict_list["Max"].append("NaN")


def fileRead():
    file_path = '../datasets/dataset_train.csv'
    df = pd.read_csv(file_path)
#    print(df["Arithmancy"][20])
    return df


def printSpace(value):
    for i in range(value):
        print(" ", end="")


def printDict(dict_list):
    print("Chose 4 row to display.")
    i = 0
    for value in dict_list["Name"]:
        print(i, " : ", value)
        i += 1
    while True:
        try:
            index1 = int(input(f"Which of the {len(dict_list['Name'])} do you want to see ? : "))
            if (index1 < 0 or index1 > len(dict_list['Name']) - 1):
                raise ValueError
            index2 = int(input(f"Which of the {len(dict_list['Name'])} do you want to see ? : "))
            if (index2 < 0 or index2 > len(dict_list['Name']) - 1):
                raise ValueError
            index3 = int(input(f"Which of the {len(dict_list['Name'])} do you want to see ? : "))
            if (index3 < 0 or index3 > len(dict_list['Name']) - 1):
                raise ValueError
            index4 = int(input(f"Which of the {len(dict_list['Name'])} do you want to see ? : "))
            if (index4 < 0 or index4 > len(dict_list['Name']) - 1):
                raise ValueError
            break
        except ValueError:
            print("Input must be a number and in the range of avaible data.")
    for value in dict_list:
        print(value[:15], end="")
        printSpace(30 - len(value))
        if (isinstance(dict_list[value][index1], (int, np.integer, float, np.floating, complex, np.complexfloating))):
            print(f"{dict_list[value][index1]:.5f}", end="")
            formatted_value = f"{dict_list[value][index1]:.5f}"
            printSpace(30 - len(formatted_value))
        else:
            print(dict_list[value][index1][:15], end="")
            printSpace(30 - len(dict_list[value][index1][:15]))

        if (isinstance(dict_list[value][index2], (int, np.integer, float, np.floating, complex, np.complexfloating))):
            print(f"{dict_list[value][index2]:.5f}", end="")
            formatted_value = f"{dict_list[value][index2]:.5f}"
            printSpace(30 - len(formatted_value))
        else:
            print(dict_list[value][index2][:15], end="")
            printSpace(30 - len(dict_list[value][index2][:15]))

        if (isinstance(dict_list[value][index3], (int, np.integer, float, np.floating, complex, np.complexfloating))):
            print(f"{dict_list[value][index3]:.5f}", end="")
            formatted_value = f"{dict_list[value][index3]:.5f}"
            printSpace(30 - len(formatted_value))
        else:
            print(dict_list[value][index3][:15], end="")
            printSpace(30 - len(dict_list[value][index3][:15]))

        if (isinstance(dict_list[value][index4], (int, np.integer, float, np.floating, complex, np.complexfloating))):
            print(f"{dict_list[value][index4]:.5f}", end="")
            formatted_value = f"{dict_list[value][index4]:.5f}"
        else:
            print(dict_list[value][index4][:15], end="")

        print("\n")


def fileWrite(dict_list):
    df = pd.DataFrame(dict_list)
    df.to_csv("result.csv", index=False)


def main():
    df = fileRead()
    dict_list = {
        "Name": [],
        "Count": [],
        "Mean": [],
        "Std": [],
        "Min": [],
        "25%": [],
        "50%": [],
        "75%": [],
        "Max": []
    }
    calcCount(df, dict_list)
    calcMean(df, dict_list)
    calcStd(df, dict_list)
    calcMin(df, dict_list)
    calc25(df, dict_list)
    calc50(df, dict_list)
    calc75(df, dict_list)
    calcMax(df, dict_list)
    fileWrite(dict_list)
    printDict(dict_list)


if __name__ == "__main__":
    main()

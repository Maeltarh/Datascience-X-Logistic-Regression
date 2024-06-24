# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scatter_plot.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mhugueno <mhugueno@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/18 20:39:27 by mhugueno          #+#    #+#              #
#    Updated: 2024/05/20 22:19:18 by mhugueno         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def fileRead(file_path):
    df = pd.read_csv(file_path)
    return df


def calcCorre(df, df_bis, n1, n2, i1, i2):
    var = 0
    var1 = 0
    var2 = 0
    for value1, value2 in zip(df[n1], df[n2]):
        if pd.notna(value1) and pd.notna(value2):
            if isinstance(value1, (int, np.integer, float, np.floating, complex, np.complexfloating)) and isinstance(value2, (int, np.integer, float, np.floating, complex, np.complexfloating)):
                var += (value1 - df_bis["Mean"][i1]) * (value2 - df_bis["Mean"][i2])
                var1 += (value1 - df_bis["Mean"][i1])**2
                var2 += (value2 - df_bis["Mean"][i2])**2
    if (var != 0 and ((var1 * var2)**0.5) != 0):
        result = var / ((var1 * var2)**0.5)
    else:
        print("Error: value of 0 on either ", df_bis["Name"][i1]," or ",  df_bis["Name"][i2])
    return (result)


def display(df, df_bis):
    x1 = range(len(df[df_bis["Name"][7]].dropna()))
    x2 = range(len(df[df_bis["Name"][11]].dropna()))
    plt.figure(figsize=(10, 6))
    plt.scatter(x1, df[df_bis["Name"][7]].dropna(), color='red', label='Feature 1')
    plt.scatter(x2, df[df_bis["Name"][11]].dropna(), color='blue', label='Feature 2')
    plt.title('Scatter Plot des Deux Features')
    plt.xlabel('X label')
    plt.ylabel('Y label')
    plt.legend()
    plt.show()


def main():
    df = fileRead('../datasets/dataset_train.csv')
    df_bis = fileRead('../DataAnalysis/result.csv')
    """
    vifDor = [0, 0, 0]
    for i in range(6, 18):
        for j in range(6, 18):
            if (i != j):
                tmp = calcCorre(df, df_bis, df_bis["Name"][i], df_bis["Name"][j], i, j)
                if (tmp < 0):
                    if (tmp < vifDor[0]):
                        vifDor[0] = tmp
                        vifDor[1] = i
                        vifDor[2] = j
                elif (tmp > vifDor[0]):
                    vifDor[0] = tmp
                    vifDor[1] = i
                    vifDor[2] = j
    print(vifDor, df_bis["Name"][vifDor[1]], df_bis["Name"][vifDor[2]])
    """
    display(df, df_bis)


if __name__ == "__main__":
    main()

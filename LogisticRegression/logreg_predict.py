# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logreg_predict.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mhugueno <mhugueno@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/25 23:20:09 by mhugueno          #+#    #+#              #
#    Updated: 2024/06/16 17:28:33 by mhugueno         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import pandas as pd
import numpy as np
import json
from sklearn.preprocessing import StandardScaler, MinMaxScaler


def fileReadTheta(file_path):
    with open(file_path, 'r') as file:
        theta = json.load(file)
    return theta


def fileReadDf(file_path):
    df = pd.read_csv(file_path)
    return df


def modelHypotesis(row, theta, houseName):
    result = 0
    i = 0
    for column_name, value in row.items():
        if pd.notna(value) and (column_name == 'Interaction' or column_name == 'History of Magic' or column_name == 'Herbology' or column_name == 'Defense Against the Dark Arts' or column_name == 'Divination' or column_name == 'Transfiguration' or column_name == 'Muggle Studies'):
            if isinstance(value, (int, np.integer, float, np.floating, complex, np.complexfloating)):
                result += theta["theta"][houseName][i] * value
                i += 1
    result = 1 / (1 + np.exp(-result))
    return result


def assign(df, theta):
    result = ["valuer"] * len(df)
    for i in range(len(df)):
        row = df.iloc[i]
        modelR = modelHypotesis(row, theta, "thetaR")
        modelS = modelHypotesis(row, theta, "thetaS")
        modelG = modelHypotesis(row, theta, "thetaG")
        modelH = modelHypotesis(row, theta, "thetaH")
        if modelR >= modelS and modelR >= modelG and modelR >= modelH:
            result[i] = "Ravenclaw"
        elif modelS >= modelR and modelS >= modelG and modelS >= modelH:
            result[i] = "Slytherin"
        elif modelG >= modelR and modelG >= modelS and modelG >= modelH:
            result[i] = "Gryffindor"
        else:
            result[i] = "Hufflepuff"
    return result


def fileWrite(file_path, result):
    try:
        with open(file_path, 'r') as file:
            full_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        full_data = {}
    if "result" not in full_data or not isinstance(full_data["result"], dict):
        full_data["result"] = {
    }
    full_data["result"] = result
    with open(file_path, 'w') as file:
        json.dump(full_data, file, indent=4)


def fillmeupdaddy(df, df_stats):
    for subject in df_stats['Name']:
        median_value = df_stats.loc[df_stats['Name'] == subject, '50%'].values[0]
        df[subject] = df[subject].fillna(median_value)
    return df


def main():
    df = fileReadDf("../datasets/dataset_train.csv")
    df_stats = fileReadDf("../DataAnalysis/result.csv")
    df = fillmeupdaddy(df, df_stats)
    if df.empty:
        print("Le DataFrame est vide après suppression des lignes avec des valeurs manquantes.")
        return
    cols_to_normalize = df.columns[6:19]
    scaler = StandardScaler()
    df[cols_to_normalize] = scaler.fit_transform(df[cols_to_normalize])
    theta = fileReadTheta("data.json")
    result = assign(df, theta)
    fileWrite("data.json", result)
    for i in range(len(result)):
        print(i, ".", result[i])


if __name__ == "__main__":
    main()

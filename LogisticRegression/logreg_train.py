# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logreg_train.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mhugueno <mhugueno@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/25 23:20:00 by mhugueno          #+#    #+#              #
#    Updated: 2024/06/16 17:28:38 by mhugueno         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import pandas as pd
import numpy as np
import json
from sklearn.preprocessing import StandardScaler, MinMaxScaler


startTheta = 0
learningRate = 1


def fileWrite(file_path, name, theta):
    global startTheta
    try:
        with open(file_path, 'r') as file:
            full_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        full_data = {}
    if "theta" not in full_data or not isinstance(full_data["theta"], dict):
        full_data["theta"] = {
        'thetaR': [startTheta] * 14,
        'thetaS': [startTheta] * 14,
        'thetaG': [startTheta] * 14,
        'thetaH': [startTheta] * 14
    }
    full_data["theta"][name] = theta[name]
    with open(file_path, 'w') as file:
        json.dump(full_data, file, indent=4)


def fileRead(file_path):
    df = pd.read_csv(file_path)
    return df


def add_interaction_column(df, col1_index, col2_index, new_col_name):
    df[new_col_name] = df.iloc[:, col1_index] * df.iloc[:, col2_index]
    return df


def modelHypotesis(row, theta, houseName):
    result = 0
    i = 0
    for column_name, value in row.items():
        if pd.notna(value) and (column_name == 'Interaction' or column_name == 'History of Magic' or column_name == 'Herbology' or column_name == 'Defense Against the Dark Arts' or column_name == 'Divination' or column_name == 'Transfiguration' or column_name == 'Muggle Studies'):
            if isinstance(value, (int, np.integer, float, np.floating, complex, np.complexfloating)):
                result += theta[houseName][i] * value
                i += 1
    result = 1 / (1 + np.exp(-result))
    return result


def ravenclawModel(df, theta):
    global learningRate
    cost = 0
    deriv = [0] * len(theta["thetaR"])
    j = 0
    for column_name, i in zip(df.columns, range(len(df.columns))):
        row = df.iloc[i]
        model = modelHypotesis(row, theta, "thetaR")
        if row["Hogwarts House"] == "Ravenclaw":
            y = 1
        else:
            y = 0
        if (model > 0):
            cost += (y * np.log(model)) + ((1 - y) *(np.log(1 - model)))
        else:
            return (1)
        if column_name == 'Interaction' or column_name == 'History of Magic' or column_name == 'Herbology' or column_name == 'Defense Against the Dark Arts' or column_name == 'Divination' or column_name == 'Transfiguration' or column_name == 'Muggle Studies':
            i = 0
            for value in df[column_name]:
                if pd.notna(value) and (column_name == 'Interaction' or column_name == 'History of Magic' or column_name == 'Herbology' or column_name == 'Defense Against the Dark Arts' or column_name == 'Divination' or column_name == 'Transfiguration' or column_name == 'Muggle Studies'):
                    if isinstance(value, (int, np.integer, float, np.floating, complex, np.complexfloating)):
                        row = df.iloc[i]
                        y = 1 if row["Hogwarts House"] == "Ravenclaw" else 0
                        deriv[j] += (model - y) * (value)
                        i += 1
            theta["thetaR"][j] = theta["thetaR"][j] - (learningRate * (deriv[j] / len(df)))
            j += 1
    cost = (cost / len(df)) * -1
    return (cost)


def slytherinModel(df, theta):
    global learningRate
    cost = 0
    deriv = [0] * len(theta["thetaS"])
    j = 0
    for column_name, i in zip(df.columns, range(len(df.columns))):
        row = df.iloc[i]
        model = modelHypotesis(row, theta, "thetaS")
        if row["Hogwarts House"] == "Slytherin":
            y = 1
        else:
            y = 0
        if (model > 0):
            cost += (y * np.log(model)) + ((1 - y) *(np.log(1 - model)))
        else:
            return (1)
        if column_name == 'Interaction' or column_name == 'History of Magic' or column_name == 'Herbology' or column_name == 'Defense Against the Dark Arts' or column_name == 'Divination' or column_name == 'Transfiguration' or column_name == 'Muggle Studies':
            i = 0
            for value in df[column_name]:
                if pd.notna(value) and (column_name == 'Interaction' or column_name == 'History of Magic' or column_name == 'Herbology' or column_name == 'Defense Against the Dark Arts' or column_name == 'Divination' or column_name == 'Transfiguration' or column_name == 'Muggle Studies'):
                    if isinstance(value, (int, np.integer, float, np.floating, complex, np.complexfloating)):
                        row = df.iloc[i]
                        y = 1 if row["Hogwarts House"] == "Slytherin" else 0
                        deriv[j] += (model - y) * (value)
                        i += 1
            theta["thetaS"][j] = theta["thetaS"][j] - (learningRate * (deriv[j] / len(df)))
            j += 1
    cost = (cost / len(df)) * -1
    return (cost)


def gryffindorModel(df, theta):
    global learningRate
    cost = 0
    deriv = [0] * len(theta["thetaG"])
    j = 0
    for column_name, i in zip(df.columns, range(len(df.columns))):
        row = df.iloc[i]
        model = modelHypotesis(row, theta, "thetaG")
        if row["Hogwarts House"] == "Gryffindor":
            y = 1
        else:
            y = 0
        if (model > 0):
            cost += (y * np.log(model)) + ((1 - y) *(np.log(1 - model)))
        else:
            return (1)
        if column_name == 'Interaction' or column_name == 'History of Magic' or column_name == 'Herbology' or column_name == 'Defense Against the Dark Arts' or column_name == 'Divination' or column_name == 'Transfiguration' or column_name == 'Muggle Studies':
            i = 0
            for value in df[column_name]:
                if pd.notna(value) and (column_name == 'Interaction' or column_name == 'History of Magic' or column_name == 'Herbology' or column_name == 'Defense Against the Dark Arts' or column_name == 'Divination' or column_name == 'Transfiguration' or column_name == 'Muggle Studies'):
                    if isinstance(value, (int, np.integer, float, np.floating, complex, np.complexfloating)):
                        row = df.iloc[i]
                        y = 1 if row["Hogwarts House"] == "Gryffindor" else 0
                        deriv[j] += (model - y) * (value)
                        i += 1
            theta["thetaG"][j] = theta["thetaG"][j] - (learningRate * (deriv[j] / len(df)))
            j += 1
    cost = (cost / len(df)) * -1
    return (cost)


def hufflepuffModel(df, theta):
    global learningRate
    cost = 0
    deriv = [0] * len(theta["thetaH"])
    j = 0
    for column_name, i in zip(df.columns, range(len(df.columns))):
        row = df.iloc[i]
        model = modelHypotesis(row, theta, "thetaH")
        if row["Hogwarts House"] == "Hufflepuff":
            y = 1
        else:
            y = 0
        if (model > 0):
            cost += (y * np.log(model)) + ((1 - y) *(np.log(1 - model)))
        else:
            return (1)
        if column_name == 'Interaction' or column_name == 'History of Magic' or column_name == 'Herbology' or column_name == 'Defense Against the Dark Arts' or column_name == 'Divination' or column_name == 'Transfiguration' or column_name == 'Muggle Studies':
            i = 0
            for value in df[column_name]:
                if pd.notna(value) and (column_name == 'Interaction' or column_name == 'History of Magic' or column_name == 'Herbology' or column_name == 'Defense Against the Dark Arts' or column_name == 'Divination' or column_name == 'Transfiguration' or column_name == 'Muggle Studies'):
                    if isinstance(value, (int, np.integer, float, np.floating, complex, np.complexfloating)):
                        row = df.iloc[i]
                        y = 1 if row["Hogwarts House"] == "Hufflepuff" else 0
                        deriv[j] += (model - y) * (value)
                        i += 1
            theta["thetaH"][j] = theta["thetaH"][j] - (learningRate * (deriv[j] / len(df)))
            j += 1
    cost = (cost / len(df)) * -1
    return (cost)


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


def main():
    global learningRate
    df_raw = fileRead('../datasets/dataset_train.csv')
    df = df_raw.dropna()
    df = remove_extreme_values_by_group(df, "Hogwarts House")
    df = add_interaction_column(df, 8, 9, 'Interaction')
    cols_to_normalize = df.columns[6:20]
    scaler = StandardScaler()
    df[cols_to_normalize] = scaler.fit_transform(df[cols_to_normalize])
    theta = {
        'thetaR': [startTheta] * 14,
        'thetaS': [startTheta] * 14,
        'thetaG': [startTheta] * 14,
        'thetaH': [startTheta] * 14
    }
    costR = ravenclawModel(df, theta)
    costS = slytherinModel(df, theta)
    costG = gryffindorModel(df, theta)
    costH = hufflepuffModel(df, theta)
    tmp_costR = ravenclawModel(df, theta)
    tmp_costS = slytherinModel(df, theta)
    tmp_costG = gryffindorModel(df, theta)
    tmp_costH = hufflepuffModel(df, theta)
    while True:
        if (tmp_costR < costR and costR - tmp_costR > 0.0000001):
            costR = tmp_costR
            tmp_costR = ravenclawModel(df, theta)
            if (tmp_costR < costR and costR - tmp_costR > 0.0000001):
                fileWrite("data.json", "thetaR", theta)
            print("R : ", costR, end=" | ")
        if (tmp_costS < costS and costS - tmp_costS > 0.0000001):
            costS = tmp_costS
            tmp_costS = slytherinModel(df, theta)
            if (tmp_costS < costS and costS - tmp_costS > 0.0000001):
                fileWrite("data.json", "thetaS", theta)
            print("S :", costS, end=" | ")
        if (tmp_costG < costG and costG - tmp_costG > 0.0000001):
            costG = tmp_costG
            tmp_costG = gryffindorModel(df, theta)
            if (tmp_costG < costG and costG - tmp_costG > 0.0000001):
                fileWrite("data.json", "thetaG", theta)
            print("G :", costG, end=" | ")
        if (tmp_costH < costH and costH - tmp_costH ):
            costH = tmp_costH
            tmp_costH = hufflepuffModel(df, theta)
            if (tmp_costH < costH and costH - tmp_costH > 0.0000001):
                fileWrite("data.json", "thetaH", theta)
            print("H :", costH)
        if ((tmp_costR > costR or costR - tmp_costR < 0.0000001) and (tmp_costS > costS or costS - tmp_costS < 0.0000001) and (tmp_costG > costG or costG - tmp_costG < 0.0000001) and (tmp_costH > costH or costH - tmp_costH < 0.0000001)):
            print(f"Ravenclaw cost : {costR}\nSlytherin cost : {costS}\nGryffindor cost : {costG}\nHufflepuff cost : {costH}")
            break
        

if __name__ == "__main__":
    main()

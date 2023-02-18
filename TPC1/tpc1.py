from data import *
from person import *
from validator import *
import matplotlib.pyplot as plt
import numpy as np


def load_data(path):
    file = open(path)
    f = file.readlines()
    f.pop(0) # tirar a primeira linha do comentario

    data = list()
    bounds = {
        "age" : {
            "max" : float('-inf'),
            "min" : float('inf')
        },
        "cholesterol": {
            "max" : float('-inf'),
            "min" : float('inf')
        }
    }

    for line in f:
        lines = line.replace("\n", "").split(",")

        if len(lines) == 6:
            if validate_positive_integer(lines[0]) \
            and validate_gender(lines[1]) \
            and validate_positive_integer(lines[2]) \
            and validate_positive_integer(lines[3]) \
            and validate_positive_integer(lines[4]) \
            and validate_bit(lines[5]):
                age = int(lines[0])
                gender = lines[1]
                tension = int(lines[2])
                cholesterol = int(lines[3])
                pulse = int(lines[4])
                disease = bool(int(lines[5]))

                data.append(Person(age, gender, tension, cholesterol, pulse, disease))

                if age > bounds["age"]["max"]:
                    bounds["age"]["max"] = age
                elif age < bounds["age"]["min"]:
                    bounds["age"]["min"] = age
                
                if cholesterol > bounds["cholesterol"]["max"]:
                    bounds["cholesterol"]["max"] = cholesterol
                elif cholesterol < bounds["cholesterol"]["min"]:
                    bounds["cholesterol"]["min"] = cholesterol 
                    
    file.close()

    return Data(data, bounds)


def distribution_by_gender(data):
    res = {
        "M" : {
            False : 0,
            True: 0
        },
        "F" : {
            False : 0,
            True : 0
        }
    }

    for person in data.data:
        res[person.gender][person.disease] += 1

    return res


def distribution_by_age(data):
    max = data.bounds["age"]["max"]

    res = dict()    
    for i in range(0,(max//5)+1):
        res[(i*5, i*5 + 4)] = {
            False : 0,
            True : 0
        }
    
    for person in data.data:
        lower_bound = (person.age//5)*5
        upper_bound = lower_bound + 4
        res[(lower_bound, upper_bound)][person.disease] += 1

    return res


def distribution_by_cholesterol(data):
    min = data.bounds["cholesterol"]["min"]
    max = data.bounds["cholesterol"]["max"]

    res = dict()
    for i in range(min//10, (max//10)+1):
        res[(i*10, i*10 + 9)] = {
            False : 0,

            True : 0
        }

    for person in data.data:
        lower_bound = (person.cholesterol//10)*10
        upper_bound = lower_bound + 9
        res[(lower_bound, upper_bound)][person.disease] += 1

    return res


def distribution_to_table(distribution):
    table = [["", "Com doença", "Sem doença"]]
    
    for key in distribution.keys():
        table += [[str(key), str(distribution[key][True]), str(distribution[key][False])]]

    num_colunas = len(table[0])
    num_linhas = len(table)

    larguras = [max(len(table[i][j]) for i in range(num_linhas)) for j in range(num_colunas)]

    for i in range(num_linhas):
        for j in range(num_colunas):
            print("{:{}}".format(table[i][j], larguras[j]), end="  ")
        print()

def distribution_to_graph(distribution):
    x_axis = np.arange(len(distribution.keys()))
    x_coordinates = [str(elem) for elem in distribution.keys()]
    y_cd = [elem[True] for elem in distribution.values()]
    y_sd = [elem[False] for elem in distribution.values()]

    plt.figure(figsize=[19, 9])

    plt.bar(x_axis - 0.2, y_cd, label="Com doença", tick_label=x_coordinates, width=0.4)
    plt.bar(x_axis + 0.2, y_sd, label="Sem doença", tick_label=x_coordinates, width=0.4)

    plt.xticks(x_axis, distribution.keys())
    plt.ylabel("Frequência")
    plt.title("Distribuição")
    plt.legend()
    plt.show()



csv_path = input("Path do ficheiro CSV:\n")
data = load_data(csv_path)
print("Dados carregados!")

option = 0

while option != 4:
    print("------------------------------------------")
    print("Qual distribuição pretende visualizar?")
    print("1 - Distribuição por género")
    print("2 - Distribuição por idade")
    print("3 - Distribuição por colesterol")
    print("4 - Sair")
    print("------------------------------------------")

    option = int(input())

    match option:
        case 1:
            print("------------------------------------------")
            print("1 - Formato tabular")
            print("2 - Formato gráfico")
            print("------------------------------------------")
            format = int(input())

            match format:
                case 1:
                    distribution_to_table(distribution_by_gender(data))
                case 2:
                    distribution_to_graph(distribution_by_gender(data))
                case _:
                    print("Opção inválida!")
        case 2:
            print("------------------------------------------")
            print("1 - Formato tabular")
            print("2 - Formato gráfico")
            print("------------------------------------------")
            format = int(input())

            match format:
                case 1:
                    distribution_to_table(distribution_by_age(data))
                case 2:
                    distribution_to_graph(distribution_by_age(data))
                case _:
                    print("Opção inválida!")
        case 3:
            print("------------------------------------------")
            print("1 - Formato tabular")
            print("2 - Formato gráfico")
            print("------------------------------------------")
            format = int(input())

            match format:
                case 1:
                    distribution_to_table(distribution_by_cholesterol(data))
                case 2:
                    distribution_to_graph(distribution_by_cholesterol(data))
                case _:
                    print("Opção inválida!")
        case 4:
            print("A sair...")
        case _:
            print("Opção inválida!")


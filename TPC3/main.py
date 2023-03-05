import re
import json

def print_dict(dict):
    print(' ' * 50 + "| Frequência")
    print('-' * 100)
    for key in dict.keys():
        print(key + ' '*(50-len(key)) + "| " + str(dict[key]))

def processes_per_year(data):
    processes = dict()

    for process in data:
        year = process["year"]
        if year not in processes:
            processes[year] = 1
        else:
            processes[year] += 1

    return processes

def most_used_names_per_sec(first_names, last_names):
    first_name_keys_sorted = list(first_names.keys())
    last_name_keys_sorted = list(last_names.keys())

    first_name_keys_sorted.sort()
    last_name_keys_sorted.sort()
    
    print("================================================================")
    print("                         First names")
    print("================================================================")
    for sec in first_name_keys_sorted:
        print('-' * 20)
        print("     Século " + str(sec))

        items = list(first_names[sec].items())
        items.sort(key=lambda x : x[1], reverse=True)

        for i in range(0, 5):
            print(items[i])


    print("================================================================")
    print("                         Last names")
    print("================================================================")
    for sec in last_name_keys_sorted:
        print('-' * 20)
        print("     Século " + str(sec))

        items = list(last_names[sec].items())
        items.sort(key=lambda x : x[1], reverse=True)

        for i in range(0, 5):
            print(items[i])


def names_per_century(data):
    first_names = dict()
    last_names = dict()
    
    for process in data:
        first_name = re.match(r"\b[A-Za-z]+\b", process["name"]).group()
        last_name = re.search(r"\b[A-Za-z]+$", process["name"]).group()
        year = process["year"]
        sec = (int(year) // 100) + 1

        if sec not in first_names:
            first_names[sec] = dict()

        if sec not in last_names:
            last_names[sec] = dict()
        
        if first_name not in first_names[sec]:
            first_names[sec][first_name] = 0
        
        if last_name not in last_names[sec]:
            last_names[sec][last_name] = 0

        first_names[sec][first_name] += 1
        last_names[sec][last_name] += 1

    return first_names, last_names


def relationshiop_frequency(data):
    relationship = dict()

    exp = re.compile(r"[a-zA-Z ]*,([a-zA-Z\s]*)\.[ ]*Proc\.\d+\.")

    for process in data:
        obs = process["obs"]
        matches = exp.finditer(obs)

        for match in matches:
            if match.group(1) not in relationship:
                relationship[match.group(1)] = 0
            relationship[match.group(1)] += 1
    
    return relationship


def processes_to_json(data, path):
    file = open(path + ".json", "w")
    json.dump(data[:20], file)
    file.close()


def main():
    file = open("processos.txt")
    line_exp = re.compile(r"(?P<folder>\d+)::(?P<year>\d{4})\-(?P<month>\d{2})-(?P<day>\d{2})::(?P<name>[A-Za-z ]+)::(?P<f_name>[A-Za-z ]+)::(?P<m_name>[A-Za-z ]+)::(?P<obs>.*)::")
    obs_exp = re.compile(r"Doc.danificado.")
    matches = line_exp.finditer(file.read())   

    processes = dict()
    valid_processes = list()

    # Filtra linhas iguais e documentos danificados
    for match in matches:
        if not obs_exp.search(match.group("obs")):
            if match["folder"] in processes:
                if match.groupdict() not in processes[match["folder"]]:
                    processes[match["folder"]].append(match.groupdict())
            else:
                processes[match["folder"]] = [match.groupdict()]
    
    for value in processes.values():
        valid_processes += value

    option = 0
    while option != 5:
        print("------------------------------------------")
        print("1 - Frequência de processos por ano")
        print("2 - Frequência de nomes por século")
        print("3 - Frequência de tipos de relação")
        print("4 - 20 primeiros registos para json")
        print("5 - Sair")
        print("------------------------------------------")

        option = int(input())

        match option:
            case 1:
                print_dict(processes_per_year(valid_processes))

            case 2:
                first_names, last_names = names_per_century(valid_processes)
                most_used_names_per_sec(first_names, last_names)
            case 3:
                print_dict(relationshiop_frequency(valid_processes))
            case 4:
                print("Nome do ficheiro:")
                path = input()
                processes_to_json(valid_processes, path)
            case 5:
                print("A sair...")
            case _:
                print("Opção inválida!")



if __name__ == '__main__':
    main()


import re
import json
from statistics import mean

def main():
    file_name = input("Indique o nome do ficheiro:\n")

    file = open(file_name+".csv")
    lines = file.readlines()
    file.close()

    regex_header = re.compile(r"([^,{]+)(\{(\d+)(,(\d+))?\}(::(\w+))?)?[,]?")
    header_fields = regex_header.findall(lines[0].strip())

    header = []
    lists = dict()
    aggregate = dict()
    for i in range(0, len(header_fields)):
        field_name = header_fields[i][0]
        header.append(field_name)

        if header_fields[i][6] != '':
            aggregate[field_name] = header_fields[i][6]
            lists[field_name] = (header_fields[i][2], header_fields[i][4])
        elif header_fields[i][2] != '':
            lists[field_name] = (header_fields[i][2], header_fields[i][4])


    #Construir expressão
    regex = ""
    for field_name in header:
        if field_name in lists:
            if lists[field_name][1] != '':
                str_range = f"{{{int(lists[field_name][0])},{int(lists[field_name][1])}}}"
            else:
                str_range = f"{{{int(lists[field_name][0])}}}"

            regex += rf"(?P<{field_name}>([^,]+[,]?){str_range})[,]?"
        else:
            regex += rf"(?P<{field_name}>[^,]+)[,]?"

    regex = re.compile(regex)

    # Meter a informação em dicionarios com a expressao regex
    data = list()
    lines = lines[1:]
    for line in lines:
        matches = regex.finditer(line.strip())

        for match in matches:
            data.append(match.groupdict())

    # Tratar a lista de dicionarios para inserir as listas e funcoes de agregaçao
    for elem in data:
        for field_name in header:
            if field_name in lists:
                elem[field_name] = [int(num) for num in re.findall(r"\d+", elem[field_name])]
            
            if field_name in aggregate:
                if aggregate[field_name] == "sum":
                    elem[field_name] = sum(elem[field_name])
                elif aggregate[field_name] == "media":
                    elem[field_name] = mean(elem[field_name])


    json_file = open(file_name+".csv", "w")
    json.dump(data, json_file, indent=len(header), ensure_ascii=False)
    json_file.close()   


if __name__ == '__main__':
    main()


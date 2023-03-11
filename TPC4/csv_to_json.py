import re
import json
from statistics import mean

def main():
    file = open("alunos5.csv")
    lines = file.readlines()
    file.close()


    header_re = re.compile(r"([^,{]+)(?:\{(\d+)(?:,(\d+))?\}(?:::(\w+))?)?[,]?")
    header_fields = header_re.findall(lines[0].strip())


    # Estruturas do cabeçalho
    header = []
    lists = dict()
    aggregates = dict()
    for i in range(0, len(header_fields)):
        field = header_fields[i][0]
        quantity1 = header_fields[i][1]
        quantity2 = header_fields[i][2]
        aggregate = header_fields[i][3]

        header.append(field)

        if aggregate != '':
            lists[field] = (quantity1, quantity2)
            aggregates[field] = aggregate
        elif quantity1 != '':
            lists[field] = (quantity1, quantity2)


    #Construir expressão
    body_re = ""
    for field in header:
        if field in lists:
            if lists[field][1] != '':
                quantity = f"{{{int(lists[field][0])},{int(lists[field][1])}}}"
            else:
                quantity = f"{{{int(lists[field][0])}}}"

            body_re += rf"(?P<{field}>([^,]+[,]?){quantity})[,]?"
        else:
            body_re += rf"(?P<{field}>[^,]+)[,]?"

    body_re = re.compile(body_re)


    # Meter a informação em dicionarios com a expressao regex
    data = list()
    for line in lines[1:]:
        matches = body_re.finditer(line.strip())
        data += [match.groupdict() for match in matches]
    

    # Tratar a lista de dicionarios para inserir as listas e funcões de agregaçao
    for elem in data:
        for field in header:
            if field in lists:
                elem[field] = [int(num) for num in re.findall(r"\d+", elem[field])]
            
            if field in aggregates:
                if aggregates[field] == "sum":
                    elem[field] = sum(elem[field])
                elif aggregates[field] == "media":
                    elem[field] = mean(elem[field])


    json_file = open("alunos5.json", "w")
    json.dump(data, json_file, indent=len(header), ensure_ascii=False)
    json_file.close()   


if __name__ == '__main__':
    main()


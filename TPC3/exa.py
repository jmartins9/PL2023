import re


def main():
    with open("processos.txt", "r") as file:
        lines = file.readlines()

    er = re.compile(r"\d+::(\d{4})-")
    years = {}
    for line in lines:
        result = er.match(line)
        if result:
            year = result.group(1)
            if year in years:
                years[year] += 1
            else:
                years[year] = 1
    print('-'*40)
    print('Ano' + ':' + ' '*5 + 'Numero de Processos')
    for key in years:
        print(key + ':' + ' '*4 + str(years[key]))


if __name__ == '__main__':
    main()

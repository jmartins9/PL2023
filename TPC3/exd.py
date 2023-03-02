import re


def main():
    with open("processos.txt", "r") as in_file:
        lines = in_file.readlines()

    er = re.compile(r"(?P<pasta>\d+)::(?P<data>\d{4}-\d{2}-\d{2})::(?P<nome>[A-Za-z ]+)::(?P<pai>[A-Za-z ]+)::(?P<mae>[A-Za-z ]+)::(?P<observacoes>.*)::$")

    processes = []
    for i in range(20):
        match = er.match(lines[i])
        if match:
            process = {'pasta': match.group('pasta'), 'data':match.group('data'), 'nome': match.group('nome'),
                       'pai': match.group('pai'), 'mãe': match.group('mae'),
                       'observacoes': match.group('observacoes')}
            processes.append(process)

    with open("processos.json", "w") as ou_file:
        ou_file.write("{\n\t\"processos\" : [\n")
        for i in range(len(processes)):
            ou_file.write("\t\t{\n")
            ou_file.write(f"\t\t\t\"pasta\" : \"{(processes[i])['pasta']}\",\n")
            ou_file.write(f"\t\t\t\"data\" : \"{(processes[i])['data']}\",\n")
            ou_file.write(f"\t\t\t\"nome\" : \"{(processes[i])['nome']}\",\n")
            ou_file.write(f"\t\t\t\"pai\" : \"{(processes[i])['pai']}\",\n")
            ou_file.write(f"\t\t\t\"mãe\" : \"{(processes[i])['mãe']}\",\n")
            ou_file.write(f"\t\t\t\"observações\" : \"{(processes[i])['observacoes']}\"\n")
            if i == len(processes) - 1:
                ou_file.write("\t\t}\n")
            else:
                ou_file.write("\t\t},\n")

        ou_file.write("\t]\n}")


if __name__ == '__main__':
    main()

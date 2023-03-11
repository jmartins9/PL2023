import re
import json


def main():
    header_re = re.compile(r"([\wú]+)({\d+,\d+}|{\d+})?(::\w+)?")
    body_re = re.compile(r"\s*,\s*")
    intf_re = re.compile(r"{(\d+),(\d+)}")
    nf_re = re.compile(r"{(\d+)}")

    with open("students.csv", "r", encoding="UTF-8") as file:
        header = file.readline()
        lines = list(map(lambda x: body_re.split(x[:-1]), file.readlines()))

    lines.pop()
    headers = header_re.findall(header)
    students = []
    for line in lines:
        student = {}

        for index, head in enumerate(headers):
            if head[1] == '' and head[2] == '':
                student[head[0]] = line[index]
            else:
                result = nf_re.match(head[1])
                result1 = intf_re.match(head[1])
                grades = []
                if result:
                    for i in range(int(result.group(1))):
                        grades.append(line[index + i])
                elif result1:
                    for i in range(int(result1.group(2))):
                        if line[index + i] != '':
                            grades.append(line[index + i])

                if head[2] != '':
                    func = (head[2])[2:]
                else:
                    func = ''
                    student[head[0]] = grades

                if func == 'sum' and len(grades) != 0:
                    student["Notas_sum"] = sum(map(lambda x: int(x), grades))
                elif func == 'media' and len(grades) != 0:
                    student["Notas_media"] = sum(map(lambda x: int(x), grades)) / len(grades)

        students.append(student)

    with open("students.json", "w", encoding="UTF-8") as output:
        json.dump(students, output, ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()


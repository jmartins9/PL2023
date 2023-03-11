import re
import json


def main():
    header_re = re.compile(r"(\w+)(?:{(\d+)(?:,(\d+))})?(?:::(\w+))?")
    body_re = re.compile(r"\s*,\s*")

    with open("students.csv", "r", encoding="UTF-8") as file:
        header = file.readline()
        lines = list(map(lambda x: body_re.split(x[:-1]), file.readlines()))
        lines.pop()

    headers = header_re.findall(header)
    students = []

    for line in lines:
        student = {}

        for index, head in enumerate(headers):

            if head[1] == '' and head[2] == '' and head[3] == '':
                student[head[0]] = line[index]
            else:
                grades = []
                if head[2] != '':
                    for i in range(int(head[2])):
                        if line[index + i] != '':
                            grades.append(int(line[index + i]))
                elif head[1] != '':
                    for i in range(int(head[1])):
                        grades.append(int(line[index + i]))

                match head[3]:
                    case 'sum':
                        student["Notas_sum"] = sum(grades)
                    case 'media':
                        student["Notas_media"] = sum(grades) / len(grades)
                    case 'max':
                        student["Nota_maxima"] = max(grades)
                    case 'min':
                        student["Notas_minima"] = min(grades)
                    case '':
                        student[head[0]] = grades

        students.append(student)

    with open("students.json", "w", encoding="UTF-8") as output:
        json.dump(students, output, ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()


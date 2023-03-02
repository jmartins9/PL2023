import re


def main():
    with open("processos.txt", "r") as file:
        lines = file.readlines()

    er_relationships = re.compile(r",([a-zA-Z][a-zA-Z ]*?)\.( P|:)")
    relationships = {}

    for line in lines:
        relationships_list = er_relationships.findall(line)

        for relationship in relationships_list:
            relationship = relationship[0]
            if relationship not in relationships:
                relationships[relationship] = 0
            relationships[relationship] += 1

    print(relationships)


if __name__ == '__main__':
    main()

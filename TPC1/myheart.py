import matplotlib.pyplot as plt


# Class to represent a person
class Person:
    def __init__(self, age, gender, blood_pressure, cholesterol, heartbeat, disease):
        self.age = age
        self.gender = gender
        self.blood_pressure = blood_pressure
        self.cholesterol = cholesterol
        self.heartbeat = heartbeat
        self.disease = disease


# Function to read a csv file
def read_csv_file(name):
    file = open(name)
    lines = file.readlines()
    persons = []
    lines.pop(0)
    for line in lines:
        line = line[:len(line) - 1]
        fields = line.split(',')
        persons.append(Person(fields[0], fields[1], fields[2], fields[3], fields[4], fields[5]))
    return persons


# Function that creates a distribution of the disease by gender
def disease_by_gender(persons):
    distribution = {}
    for person in persons:
        if bool(person.disease):
            if person.gender in distribution.keys():
                distribution[person.gender] += 1
            else:
                distribution[person.gender] = 1
    return distribution


# Function that creates a distribution of the disease by age groups
def disease_by_age_groups(persons):
    distribution = {}

    for person in persons:
        if bool(person.disease):
            age_group = int(person.age) // 5
            age_group *= 5
            if age_group in distribution.keys():
                distribution[age_group] += 1
            else:
                distribution[age_group] = 1

    return distribution


# Function that creates a distribution of the disease by cholesterol levels
def disease_by_cholesterol_levels(persons):
    distribution = {}
    for person in persons:
        if bool(person.disease) and int(person.cholesterol) > 0:
            cholesterol_level = int(person.cholesterol) // 10
            cholesterol_level *= 10
            if cholesterol_level in distribution.keys():
                distribution[cholesterol_level] += 1
            else:
                distribution[cholesterol_level] = 1

    return distribution


# Function that print a table of a distribution
def print_distribution(distribution_type, distribution):
    keys = list(distribution.keys())
    keys.sort()
    print(distribution_type + ": Number of persons")
    for key in keys:
        print(str(key) + ": " + str(distribution[key]))


# Function that draw's a graph of a distribution (disease by gender)
def draw_gender_distribution(distribution):
    fig = plt.figure()
    keys = list(distribution.keys())
    values = []
    for key in keys:
        values.append(distribution[key])
    plt.bar(keys, values)
    plt.xlabel("gender")
    plt.ylabel("Number of persons")
    plt.title("Distribution of the disease by gender")
    plt.show()


# Function that draw's a graph of a distribution (disease by age groups)
def draw_age_distribution(distribution):
    fig = plt.figure()
    keys = list(distribution.keys())
    values = []
    for key in keys:
        while distribution[key] > 0:
            values.append(key)
            distribution[key] -= 1
    plt.hist(values, bins=len(keys))
    plt.xlabel("Age")
    plt.ylabel("Number of persons")
    plt.title("Distribution of the disease by age")
    plt.show()


# Function that draw's a graph of a distribution (disease by cholesterol levels)
def draw_cholesterol_distribution(distribution):
    fig = plt.figure()
    keys = list(distribution.keys())
    values = []
    for key in keys:
        while distribution[key] > 0:
            values.append(key)
            distribution[key] -= 1
    plt.hist(values, bins=len(keys))
    plt.xlabel("Cholesterol")
    plt.ylabel("Number of persons")
    plt.title("Distribution of the disease by cholesterol")
    plt.show()


def main():
    print("Insert the csv file name: ", end="")
    name = input()
    persons = read_csv_file(name)
    option = -1

    while option != 0:
        print()
        print("1. Show the table of the distribution of the disease by gender")
        print("2. Show the table of the distribution of the disease by age groups")
        print("3. Show the table of the distribution of the disease by cholesterol levels")
        print("4. Draw a graph of the distribution of the disease by gender")
        print("5. Draw a graph of the distribution of the disease by age groups")
        print("6. Draw a graph of the distribution of the disease by cholesterol levels")
        print("0. Exit")
        print()
        print("Choose the option: ", end="")
        option = int(input())
        match option:
            case 1:
                print()
                print_distribution("gender", disease_by_gender(persons))
            case 2:
                print()
                print_distribution("Age group", disease_by_age_groups(persons))
            case 3:
                print()
                print_distribution("Cholesterol level", disease_by_cholesterol_levels(persons))
            case 4:
                draw_gender_distribution(disease_by_gender(persons))
            case 5:
                draw_age_distribution(disease_by_age_groups(persons))
            case 6:
                draw_cholesterol_distribution(disease_by_cholesterol_levels(persons))


if __name__ == '__main__':
    main()


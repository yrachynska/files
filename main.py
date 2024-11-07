from random import randint, choice

No = 1
languages = ["Python", "C++", "C#", "Java"]

with open("data.csv", "w") as datafile:
    datafile.write("No, Student, Age, Grade, Sex, Prog. Language\n")
    while No < 201:
        string = f"{No}, student{No}, "
        age = randint(13, 16)
        if age == 13:
            grade = randint(8, 9)
        elif age == 14:
            grade = randint(9, 10)
        elif age == 15:
            grade = randint(10, 11)
        else:
            grade = 11
        sex = choice(["m", "fm"])
        language = choice(languages)
        string += f"{age}, {grade}, {sex}, {language}\n"
        datafile.write(string)
        No += 1
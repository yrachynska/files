import pickle
groups = {}
with open("data.csv", "rt") as file:
    next(file)
    for row in file:
        a = [int(i) if i.isdigit() else i for i in row[:-1].split(", ")]
        clas = a[3]
        languge = a[5]

        if clas not in groups:
            groups[clas] = {}
        if languge not in groups[clas]:
            groups[clas][a[5]] = []
        groups[clas][languge].append([a[1],a[2],a[4]])
with open("new_dict.txt","wb") as file:
    pickle.dump(groups,file)

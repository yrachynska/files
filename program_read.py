import pickle
with open("new_dict.txt","rb") as file:
    info = pickle.load(file)

for key in info:
    print(f"{key} class:")
    for key2 in info[key]:
        print(f"  {key2}:")
        for i in info[key][key2]:
            print(f"    {i}")

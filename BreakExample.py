from utilities import dictionary
for k, v in dictionary.items():
    if k == "name" and v:
        print("The name is {0}".format(v))
        break
else:
    print("There is no name")

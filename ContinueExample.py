from utilities import dictionary

for k, v in dictionary.items():
    if k:
        print("Printing {0} value: {1}".format(k, v))
        continue
    print("There is no value")

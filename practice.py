def master_yoda(string):
    strList = string.split()
    inverselist = strList[::-1]
    return " ".join(inverselist)

print(master_yoda('I am trying to print this sentence in reverse'))
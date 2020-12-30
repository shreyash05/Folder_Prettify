import os
def soldier(path,file,formate):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    with open(file) as f:
        filelist = f.read().split("\n")

    for file in files:
        if file not in filelist:
            os.rename(file,file.capitalize())
        if os.path.splitext(file)[1] == formate:
            os.rename(file,f"{i}{format}")

soldier(r"C:\Users\shree\PycharmProjects\pythonProject\SoldierFile",r"C:\Users\shree\PycharmProjects\pythonProject\SoldierFile\New Text Document.txt",".PNG")

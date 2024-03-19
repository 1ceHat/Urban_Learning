file = open("Test.txt", mode="r", encoding="utf8")
file_cont = file.read()
file.close()

print(file_cont)
from time import sleep
filepath = r"C:\Users\Lenovo\Desktop\testCD\pythonFiles\demofile3.txt"
f = open(filepath, "a")

for i in range(10):
    f.write("Appending----\n")
    sleep(5)

f.close()
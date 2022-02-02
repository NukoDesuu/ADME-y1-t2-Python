
def yay():
    print("yayyy")

def nah():
    print("bruhh")

cmd_list = {"y" : yay, "n" : nah}

while True:
    inp = str(input())
    if inp == "exit":
        break
    elif inp in cmd_list:
        cmd_list[inp]()


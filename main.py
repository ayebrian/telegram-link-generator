from concurrent.futures import thread
import os
import random
import string
import threading

link = "https://t.me/+"
link += "".join(
    random.choice(string.ascii_letters + string.digits + "_" + "-")
    for _ in range(16))
invited1 = "You are invited to the channel"
invited2 = "You are invited to a group chat"
invited3 = "member"


def checker(link):
    # i wish it'll work
    while True:
        if invited3 in os.popen(f"curl -s '{link}'").read():
            print("Found a private group chat!" + "" + link)
        if invited2 in os.popen(f"curl -s '{link}'").read():
            print("Invalid link")
        if "You are invited to the channel" in os.popen(
                f"curl -s '{link}'").read():
            print("Found a channel link!" + "" + link)
        else:
            print("Not valid")
        try:
            threading.Event().wait(0.5)
        except KeyboardInterrupt:
            break


threads = []
for _ in range(10):
    threads.append(threading.Thread(target=checker, args=(link, )))
    threads[-1].start()
for thread in threads:
    thread.join()

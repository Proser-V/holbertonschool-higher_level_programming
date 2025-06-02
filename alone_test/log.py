from datetime import datetime

with open("log.txt", "r") as f:
    for line in f:
        if line.strip():
            print(line.strip())

with open("log.txt", "a") as f:
    now = datetime.now().strftime("%Y-%m%d %H:%M:%S")
    f.write("{}".format(now))

def getData(txt_file):
    with open("input.txt", "r") as f:
        return [line.strip() for line in f.readlines()]

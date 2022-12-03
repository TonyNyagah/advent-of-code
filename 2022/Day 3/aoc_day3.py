def getData(txt_file) -> list:
    """Get data from a text file and remove new line characters."""
    with open(txt_file, "r") as f:
        data_list = f.read().splitlines()
    return data_list


if __name__ == "__main__":
    data = getData("test.txt")

    print(data)

    print([len(x) for x in data])

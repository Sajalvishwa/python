with open("sample.txt", "r+") as file:
    content = file.read()
    print(content)

    file.write("\nThis is a new line added in read and write mode.")
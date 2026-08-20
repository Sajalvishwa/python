with open ("sample.txt", "a+") as file:
    file.write("Hello, World!")
    file.seek(0)  # Move the cursor to the beginning of the file
    content = file.read()
    print(content)
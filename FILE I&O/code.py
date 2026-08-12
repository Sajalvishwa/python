data = True
line =1
with open("sample.text", "r") as f:
    while(data):
     data = f.readline()

     if("python" in data):
        print(f"word found at line {line}")
        
        break
     line +=1
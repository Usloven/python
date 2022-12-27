with open("zip.txt",'r') as d:
    data=d.readline()
    def zip(data):
        temp = ["1"]
        temp_char=""
        temp_add="1"
        count = 1
        for i in data:
            if i == temp_char:
                count=count+1

            else:
                temp.append(str(count))
                temp.append(temp_char)
                temp_char=i
        k = [i for i in temp if i!="1"]       
        print(k)
        print (  "".join(k))

    zip(data)


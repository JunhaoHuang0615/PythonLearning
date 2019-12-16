#with statement can help to close the file

try:
    with open('data,txt','r') as f: 
        for eachline in f:
            print(eachline)
except:
    print('file not found or not readable')

#don't need finnaly to close the file
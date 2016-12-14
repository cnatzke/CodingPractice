with open('hello.txt','r') as file:
    data=file.readlines()

print(data)

data[2]='Mage\n'

with open('hello.txt','w') as output_file:
    output_file.writelines(data)
    

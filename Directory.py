import os


def readf(fil):
    #reading the file for proof of storing
    print("File content:")
    readFile = open(fil,'r')
    # with open(os.path.join(directory,filename),'r+') as readFile:
    '''
    for line in writeFile:
        print(line)
    '''
    content = readFile.readlines()
    for c in content:
        det=c.split(',')
        for d in det:
            print(d)
        
    readFile.close()

def main():
    
    #Enter Directory
    directory = input("Enter the directory that you want to save the file : ")

    #Enter Filename
    filename = input("Enter the filename : ")
    
    #Enter Your Name
    name = input("Enter your name : ")
    
    #Enter Street
    street = input("Enter your street address : ")
    
    #Enter City
    city = input("Enter your city : ")
    
    #Enter State
    state = input("Enter your state : ")
    
    #Enter Zipcode
    zipcode = input("Enter your zipcode: ")
    
    #Enter Cell Number
    number = input("Enter your phone number: ")
    
    if os.path.isdir(directory):
        
        print("Writing to :",os.path.join(directory,filename) )
        
        writeFile = open(os.path.join(directory,filename),'w')
        
        writeFile.write(name+','+street+','+city+','+state+', '+zipcode+','+number+'\n')
        
        writeFile.close()
        
        readf(os.path.join(directory,filename))
    else:
        print("The directory you entered does not exists")

main()

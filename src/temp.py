#try:
f = open("Test.txt","r")
if f.mode == "r":
    contents = f.read()
    contents = contents.split(",")
    contents = [float(i) for i in contents]
    contents = ''.join([str(contents[i]) + "," for i in range(len(contents)-1)]) + str(contents[len(contents)-1])
    print (contents)
#except:
    #f = open("Test2.txt","w+")
    #f.write("This is text2")
    #print("Exception")
        

f.close()
#print (os.path.dirname(os.path.abspath(__file__))) #Gets working directory name

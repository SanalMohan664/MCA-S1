fileobj = open("file3.txt","r")
filelist = []
condition = True

while condition:
    x = fileobj.readline()
    filelist.append(x)
    if not x:
        print("file ended")
        condition = False

fileobjnew = open("file2.txt","w")
for i in range(0,len(filelist)):
    if(i%2==0):
        fileobjnew.write(filelist[i])
fileobj.close()
fileobjnew.close()


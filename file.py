#absolute path
#relative path
"""
filen=open("/home/jana/python-playground/test1.py","a",)
filen.write("adding again the first line")
filen=open("/home/jana/python-playground/test1.py","r")
#print(filen.read())
filen.close()
import os
os.remove("/home/jana/python-playground/test1.py")    
"""
newfile=open("/home/jana/python-playground/test.py","w")
newfile.write("new file created")
newfile=open("/home/jana/python-playground/test.py","r")
print(newfile.read())
newfile.close()



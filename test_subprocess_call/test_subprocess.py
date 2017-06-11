import numpy as np
from subprocess import call

#Making the array
a=np.array([1,2,3,4,5])

#Opening a text file to write in the array values
fout = open('test_subprocess.txt', 'w')
#Reading in the values
for n in range(len(a)):
        fout.write(str(a[n])+'\n')
#Closing the file
fout.close()

print ("You input the file!")

#Using subprocess to call the C script
call(["./test_subprocess",'test_subprocess'])

print ('\n'+"Done calling the C script!")

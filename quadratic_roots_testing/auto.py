import os
command = "./root "
ls =['1' ,'2','50','99','100']
ls2 = ['0','1','2','50','99','100','101']
for i in range(0,5):
        vara = command + ls[i]
        for j in range(0,5):
                vav = vara +' '+ ls[j]                
                for k in range(0,5):
                        os.system(vav + ' ' + ls[k])
                        print ("\n")
print("\n Robustness Testing")
for i in range(0,7):
        vara = command + ls2[i]
        for j in range(0,7):
                vav = vara +' '+ ls2[j]                
                for k in range(0,7):
                        os.system(vav + ' ' + ls2[k])
                        print ("\n")

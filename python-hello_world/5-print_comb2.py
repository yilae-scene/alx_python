
#have a range between (0, 100)
for i in range(0 , 100):
   
#numbers printed should be in two digits. 
    if (i < 10):
        print("0{}".format(i), end =",")
    else:
        print("{}".format(i), end =",")

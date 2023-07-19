
#have a range between (0, 100)
for i in range(0 , 100):
   
#numbers printed should be in two digits. 

#for (0 to 9 ) we can add 0 infront
    if (i < 10):
        print("0{}".format(i), end =",")

#for rest just print
    else:
        print("{}".format(i), end =",")

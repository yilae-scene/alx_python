
#have a range between (0, 100)
for i in range(0 , 100):
    if (i < 99 ):  # print until it reaches 99 so to remove comma in the end
        print("{:02d}".format(i), end =", ")
    else:
        print("{}".format(i))


#First iterate through the first loop

for i in range (0 , 10):
    for j in range (0 , 10):
# we need to make sure we don't print identical no's and identical combination

        if (i != j) and ("{}{}".format(i,j) < "{}{}".format(j,i)) and ("{}{}".format(i,j) != '89'):
            print("{}{}".format(i,j), end= ", ")
# make sure that the last number is not printed with comma
        elif("{}{}".format(i,j) == '89'):
            print("{}{}".format(i,j))

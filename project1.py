#Created an empty list
my_list = []

#appended items to the list
my_list.extend([10,20,30,40])

#insert 15 at index1
my_list.insert(1,15)


my_list2 = [50,60,70]

#joined two lists  to one.
my_list.extend(my_list2)

#deleted the last element from the list
my_list.pop()

#sorting the list in a descending order
my_list.sort(reverse=True)

#searched for item 30 from the list and stored ina index_30 variable for printing
index_30 = my_list.index(30)

print(my_list)
print(index_30)
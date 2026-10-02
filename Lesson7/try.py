# #List - Index in a sequence
# my_list= ['abc',123,True,[0,1,2],'fff',-1,-500]

# print(my_list)
# print(my_list[0])
# print(my_list[-1])
# print(my_list[:5:2])
# print("abc" in my_list)

#List Operations
my_list = ['abc',123,True,[0,1,2],'fff',-1,-500]
# print(my_list)
# #add an element to the list but base on its sequest in []
# my_list[1] = 'efg'
# print(my_list)
# #append an element to the end of the list
# my_list.append('xyz')
# # insert an element to the list at a specific index
# my_list.insert(0,'klmn')
# print(my_list)
#delete an element from the list based on its index
del my_list[-2]
print(my_list)
#remove an element from the list based on its value
my_list.remove(True)
print(my_list)
#len function to get the length of the list
print(len(my_list))
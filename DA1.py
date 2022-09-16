import math
# the first  goal is to get the numbers to float 
n = 14
list= [2.4, 0.9, 14.1, 0.1, 11.8, 18.4, 7.3, 11.2, 4.3, 0.7, 1.8, 1.0, 11.8, 5.1]
output= sorted(list,reverse = True)
print(output)
print(list)
# list is sqeuence that can be modified 
# tuple squence that cna not be modified 
# sort is an inplace sort 
# sorted is a make a copy of list and sort and return the sorted copy 
# find the amount of numbers in the list 
length_list = len(list)
print(length_list)
# median number in the set 
if len(list) %2 == 0 : 
    index_2= len(list)//2 # this is index 2 
    index_1= len(list)//2-1 # this is index 1 
    num_1 = list[index_1] # this is 20
    num_2 = list[index_2]
    print(num_1, num_2)
    median = (num_1 + num_2) / 2
    print("this is the median", median)
else:
    index_3= len(list)//2 
    num_3 = list[index_3]
    print(num_3)
# median number use a n if else statement 
# divide number bby the middle point 
#smallest input 

print("smallest element is:", min(list))
# largest value 

print("largest value is:", max(list))
#mean = (output/n)
mean = (sum(list)/length_list) 
print("mean=", mean)
# add number to index 
print("enter an index ")
new_num = input()
# add new number to the list 
new_num = int(new_num)
list[ index_2 ]= new_num
print(list)
output_1= sorted(list,reverse = True)
print(output_1)



# solution 3
print(" ".join(input("Enter string to be reversed --> ").split(" ")[::-1]))

# solution 4
from random import randrange

def pick_all_randoms(arr): # T(n)=O(n) S(n)=O(1)
    curr_index = 0
    arr_size = len(arr)
    while curr_index < arr_size:
        random_index = randrange(curr_index, arr_size)
        random_item = arr[random_index]
        print(random_item)
        arr[curr_index], arr[random_index] = arr[random_index], arr[curr_index]
        curr_index += 1


mylist = [1, 2, 3, 4, 5, 6, 7 ,8,9,10]
pick_all_randoms(mylist)

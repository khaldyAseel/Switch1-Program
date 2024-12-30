# [3,0,1,0,4,0,2]
# water array -> [3,2,3,2]
# sum is 10 
# put water where i have the samllest length of buliding 
# how to find the minimum?? min(max_left,max_right)
# to do a new array for the water and to sum it in the end 

# brute_force
def return_possiable_water(arr):
    water_arr= []
    n = len(arr)
    max_left =[0]*n
    max_right = [0] *n
    max_left[0] = arr[0]
    for i in range(1,len(arr)):
        if arr[i]>max_left[0]:
            max_left = arr[i]

    max_right[n - 1] = arr[n - 1]
    for j in range(len(arr)-1,1):
          if arr[i]>max_right[0]:
            max_right = arr[i]

    for i in range(n):
        trapped_water = min(max_left[i], max_right[i]) - arr[i]
        if trapped_water > 0:
            water_arr.append(trapped_water)
        else:
            water_arr.append(0)            
    return water_arr

print(return_possiable_water([3,0,1,0,4,0,2]))



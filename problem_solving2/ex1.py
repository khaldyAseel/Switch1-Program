# [3,0,1,0,4,0,2]
# water array -> [3,2,3,2]
# sum is 10 
# put water where i have the samllest length of buliding 
# how to find the minimum?? min(max_left,max_right)
# to do a new array for the water and to sum it in the end 

# brute_force
def return_possible_water(arr):
    water_arr= []
    n = len(arr)
    max_left =[0]*n
    max_right = [0] *n
    max_left[0] = arr[0]
    for i in range(1,n):
        max_left[i] = max(max_left[i-1], arr[i])

    max_right[n - 1] = arr[n - 1]
    for j in range(n-2,-1,-1):
        max_right[j] = max(max_right[j+1],arr[j])

    for i in range(n):
        trapped_water = min(max_left[i], max_right[i]) - arr[i]
        if trapped_water > 0:
            water_arr.append(trapped_water)
        else:
            water_arr.append(0)            
    return sum(water_arr)

print(f"The quantity of the trapped water is:{return_possible_water([3,0,1,0,4,0,2])}")


#more efficient solution 
def return_trapped_water(arr):
    n = len(arr)   
    left, right = 0, n - 1
    max_left, max_right = arr[left], arr[right]
    water_arr = [0] * n
    
    while left <= right:
        if arr[left] < arr[right]:
            if arr[left] >= max_left:
                max_left = arr[left]
            else:
                water_arr[left] = max_left - arr[left]
            left += 1
        else:
            if arr[right] >= max_right:
                max_right = arr[right]
            else:
                water_arr[right] = max_right - arr[right]
            right -= 1
    
    return sum(water_arr)

print(f"The quantity of the trapped water is:{return_trapped_water([3,0,1,0,4,0,2])}")



def max_trapped_water(arr):
    max_water = 0

    for i in range(1,len(arr)):
        if arr[i]!=0:
            current_water =  min(arr[0], arr[i])
            max_water = max(max_water, current_water)

        if current_water > max_water:
                max_water = current_water
    return max_water

print(f"The max water between tow buildings is:{return_trapped_water([3,0,1,0,4,0,2])}")

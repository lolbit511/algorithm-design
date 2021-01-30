def search_linear(data,key):
    for i in range(len(data)):
        if data[i] == key:
            return i #
    return -1

d = [1,3,5,2,4,3,3]
k = 3 # what we want to find
print(search_linear(d,k)) # print the location of the first matching value in the list

print("--------------------------------------------------")

def search_linear_multiple(data,key):
    result = [] # initializing list
    for i in range(len(data)):
        if data[i] == key: # if current element is same with the key
            result.append(i) # put all matches in a list
    return result
d = [1,3,5,2,3,6]
k = 3
i=search_linear_multiple(d,k)
print("key was found in:" ,i)

print("--------------------------------------------------")

def search_linear_sorted(data,key):
    result=[]
    for i in range(len(data)):
        if data[i]==key:
            result.append(i)
        elif data[i]>key:
            break
    return result

d = [1,2,4,5,9,10]
k=3
i=search_linear_sorted(d,k)
print(f"key: {k} was found at index: {i}")

print("--------------------------------------------------")

def binsearch(data,key):
    a=0
    b=len(data)-1

    while a<b:
        m=(a+b)//2
        if data[m]==key:
            return m
        elif data[m]>key:
            b=m-1
        else:
            a=m+1
    return -1

print("binsearch code")

print("--------------------------------------------------")

def bubbleSort(arr):
    n=len(arr)
# traverse all the array elements
    for i in range(n-1):
        # range(n) will also work but it will loop an extra time
        # last i elements in place
        for j in range(0,n-i-1):

            # traverse array from 0 to n - i - 1
            # swap if element found is greater than the next
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
# list that needs to be sorted
arr = [64,34,25,12,22,11,90]

bubbleSort(arr)

print(arr)

print("--------------------------------------------------")

def insert(data):
    for i in range(1,len(data)):
        j=i # set j's data to match with i

# checking if j is not equal to the first value and that the
# previous element is bigger than j
        while j>0 and data[j-1]>data[j]:
            data[j-1],data[j]=data[j],data[j-1]
            j-=1

d = [3,54,1,3,4,5,6,2,5,6,2,1,9,89,2]
insert(d)
print(d)

print("--------------------------------------------------")

def selection(data):
    for i in range(len(data)-1):
        m=i
        for j in range(i+1,len(data)): # scan all the elements
            if data[j]<data[m]:
                m=j
        data[m],data[i]=data[i],data[m] # swaps the item

d=[3,54,1,3,4,5,6,2,5,6,2,1,9,89,2]
insert(d)
print(d)
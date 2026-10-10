
def summarise(num):

    total = sum(num)
    print(total)

    average = total / len(num)
    print(average)

    biggest = max(num)
    print(biggest)

summarise([100,200,300])

def count_evens(nums):
    count = 0
    for i in nums:
        if i % 2 == 0:
            count += 1
    return count

print(count_evens([2,4,5,6,8,10]))
print(count_evens([1,2,3,4,5,6,7,8,9,10]))
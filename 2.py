def insertion_sort(nums):
    for i in range(1, len(nums)):
        item_to_insert=nums[i]
        j=i-1
        while j>=0 and nums[j]>item_to_insert:
            nums[j+1]=nums[j]
            j-=1
            nums[j+1]=item_to_insert
l=[1, 23, 45342, 0, 5647, 2343213]
insertion_sort(l)
print(l)
def next_greater_element(find_nums, nums):
    return [next((n for n in nums[nums.index(f_n):] if n > f_n), -1)
            for f_n in find_nums]

assert next_greater_element([4,2],[5,4,2,7]) == [7,7]

# (n for n in nums[nums.index(f_n):] if n > f_n) is generator which is subclass of iterator having method __next__
# next returns next n to the right of f_n for which n > f_n, if it doesn't exit, it returns -1
# see next method built in method docs at https://docs.python.org/3/library/functions.html#next



# ex2 
def find_subsets(lst):
    if not lst:
        return [[]]

    return find_subsets(lst[1:]) + [[lst[0]] + subset for subset in find_subsets(lst[1:])]

print(find_subsets([1, 2]))
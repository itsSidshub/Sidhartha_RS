def deepest_nesting(lst):
    if not isinstance(lst, list):
        return 0
    if not lst:
        return 1
    return 1 + max(deepest_nesting(item) for item in lst)
print(deepest_nesting([1, [2, [3, [4]], 5]]))

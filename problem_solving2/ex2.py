#DeepClone function:
# x = {a: "b", a2: ["first", "second"]};
# y = {b: x, b3: ["firtsY", x]};
# z = deepClone(y);  

def deepClone(obj):

    if obj is None or isinstance(obj, (int, float, str, bool)):
        return obj

    # if there is an dictionaries
    if isinstance(obj, dict):
        cloned_dict = {}
        for key, value in obj.items():
            cloned_dict[deepClone(key)] = deepClone(value)
        return cloned_dict

    # if there is an lists
    if isinstance(obj, list):
        cloned_list = []
        for item in obj:
            cloned_list.append(deepClone(item))
        return cloned_list

    # if there is an tuples
    if isinstance(obj, tuple):
        cloned_tuple = tuple(deepClone(item) for item in obj)
        return cloned_tuple


# Input
x = {"a": "b", "a2": ["first", "second"]}
y = {"b": x, "b3": ["firstY", x]}
z = deepClone(y)

# Output
print(z)


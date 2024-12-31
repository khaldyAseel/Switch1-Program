#DeepClone function:
# x = {a: "b", a2: ["first", "second"]};
# y = {b: x, b3: ["firtsY", x]};
# z = deepClone(y);  

def deepClone(obj):
    return 
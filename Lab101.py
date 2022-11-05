#The authors are Maggie Dunn and Cody Brown
dict = {"tree" : "green", "car" : "crash", 2 : True, 8 : False, "smick" : 1844}
def my_get_method(dictionary, key, default):
    if key in dictionary:
        return dictionary[key]
    else:
        return default

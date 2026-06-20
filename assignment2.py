# Problem 1
def dict_list(param1):
    result = []
    for x in param1:
        if x not in result:
            result.append(x)
    list1 = {
        "original_list" : param1,
        "unique_values" : result,
        "count": len(result)
    }
    return list1
print(dict_list([10,20,10,30,40,50,40]))        
# Problem 2
def set_operations(set1={},set2={}):
    set_union = set1 | set2
    set_intersection = set1 & set2
    set_difference = set1 - set2
    return set_union, set_difference, set_intersection
print(set_operations({1,2,3,4,5},{2,3,4,5,6}))
print({1,2},{})
# Problem 3
tuple1 = (10, 3.5, "Bangladesh", 98)
class_int , cgpa , country, city = tuple1
print(class_int)
print(cgpa)
print(country)
print(city)
tuple2 = (9, 3.5, "Bangladesh", 98)
print(tuple1 == tuple2)
print(tuple1 < tuple2)
print(tuple1 > tuple2)
# The main differences between lists and tuples are:


# Lists are mutable(can be changed),while tuples are immutable (cannot be changed)
# Lists have many methods(append(), remove(), etc.),while tuples have few methods(count(), index())
# Performance of list is slightly slower than tuple
# Use Case : List:Data that may change, Tuple:Data that should remain fixed
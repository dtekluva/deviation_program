# def mean_deviation (x1, x2, x3, x4):
#     mean_deviation = sum (x1, x2, x3, x4, )/n
#     x1 = int(input("pls input number: "))
#     x2 = int(input("pls input number: "))
#     x3 = int(input("pls input number: "))
#     x4 = int(input("pls input number: "))
#     n = int(input("pls what is total number of variables: "))
# print("the sum is:  ", mean_deviation )   
# import xbar as chidi
def chidi(original_list):
    return [1,2,3,4,5]

_list = [2,4,1,6,7,8,2,7,12,5]

def mean_dev(distribution):
    xbar = chidi(distribution)
    dev = abs(sum(xbar))/len(distribution)

    return {"mean_dev": dev, "original_list": distribution, "xbar": xbar}

print(mean_dev(_list))
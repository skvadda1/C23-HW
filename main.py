print("To find the LCM of two numbers you must first find the HCF of two numbers.")

largerNum = int(input("What is the larger number for the first set of numbers?"))
smallerNum = int(input("What is the smaller number for the first set of numbers?"))
def GCF(a,b):
    numberStore = b
    b = a % b
    a = numberStore
    return a

def lcmFormula(a,b):
    formula = a * b / GCF(a,b)
    return formula

print(lcmFormula(largerNum, smallerNum))
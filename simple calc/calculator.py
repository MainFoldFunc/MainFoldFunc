import math

def add(a: int, b: int):
    return a + b

def sub(a: int, b: int):
    return a - b

def mul(a: int, b: int):
    return a * b

def div(a: int, b: int):
    return a / b
# TODO Need to implement power function.
def powl(a, b):
    return pow(a, b)

def elements(x) -> list:
    list_of_ints = []
    for i in range(x):
        list_of_ints.append(int(input(f"What is a {i + 1}th element of the equation?:  ")))
    return list_of_ints

def main():
    cur_value = 0
    how_many_elements = int(input("How many elements are there in your equation?: "))
    list_of_elements = elements(how_many_elements)
    timer = 1
    for element in list_of_elements:
        sign = input(f"What should be a sign beetewen the {timer}th element and the next one?(+, -, *, /): ")
        if sign == "+":
            cur_value = add(element, cur_value)
        elif sign == "-":
            cur_value = sub(element, cur_value)
        elif sign == "*":
            cur_value = mul(element, cur_value)
        elif sign == "/":
            cur_value = div(element, cur_value)
        else:
            print("No such eqation sign!")
            
        timer += 1

    print(f"Your equation is eaqule to: {cur_value}")

if __name__ == "__main__":
    main()

    
                             

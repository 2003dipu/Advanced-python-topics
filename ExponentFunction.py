def raise_to_power(base_num,power_num):
    
    result = base_num**power_num
    return result
base= float(input("Enter the base number : "))
power = int(input("Enter the power number : "))
answer = raise_to_power(base,power)
print(answer)
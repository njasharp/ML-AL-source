def recursive_binary(list, target):
    if len(list) == 0:
      return False
    else:
       midpoint = (len(list))//2

       if list[midpoint] == target:
        return True
       else:
          if list[midpoint] < target:
             return recursive_binary(list[midpoint+1:], target)
          else:
             return recursive_binary(list[:midpoint], target)
          
def verify(result):
   print("Target found: ", result)

numbers = [1,2,3,4,5,6,7,8]   
result = recursive_binary(numbers, 6)
verify(result)

result = result = recursive_binary(numbers, 12)
verify(result)
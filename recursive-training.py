def factorial(n):
  if(n > 1): # 루틴에서 자신을 호출하여 하위 작업을 수행하는 케이스. recursive case
    return factorial(n-1) * n
  else:
    return 1 # 재귀 작업을 하지 않아도 되는 케이스. base case

factorial(4) # 24


# 재귀호출이 항상 더 좋은 것은 아님.






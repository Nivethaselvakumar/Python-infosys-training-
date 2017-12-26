def odd_values_string(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
      rresult=''
      index = len(result)
      while index > 0:
        rresult += result[ index - 1 ]
        index = index - 1
    return rresult
print(odd_values_string('abcdef'))

def find(or_list, element2):
  for element1 in or_list:
    if element1 == element2:
      return True
  return False
  
if __name__=="__main__":
  l = [2, 4, 6, 8, 10]
  print(find(l, 5)) 
  print(find(l, 10)) 
  print(find(l, -1))
  print(find(l, 2)) 

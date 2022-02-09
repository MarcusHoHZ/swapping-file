def swapFileData() :
  filename1 = input("Name of the first file to swap")
  filename2 = input("Name of the second file to swap")
  with open(filename1,'r') as a :
      data_a = a.read()
  with open(filename2,'r') as b :
      data_b = b.read()  
  with open(filename2,'w') as b :
      b.write(data_a)
  with open(filename1,'w') as a :
      a.write(data_b)
  print(data_a)
  print(data_b)  
swapFileData()
  

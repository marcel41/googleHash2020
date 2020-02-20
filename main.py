def main():
  print ("GOOGLE HASH READING INPUT")
  userInput = input('example name (e.g: a,b ):')

  #uncomment the following two lines to open a file
  file1 = open(userInput + ".txt", "r")
  for l in file1:
    print(l)
  file1.close()
  #close file to avoid leak out

def func1():
    skip
  #To be implemented

def func2():
    skip
  #To be implemented

if __name__== "__main__":
  main()

#WordCount.py
#Name:Edip Uman
#Date: 02/28/2026
#Assignment: Lab 6


def main():
  textFile = open("gettysberg.txt", 'r')
  lineCount = 0 
  wordCount = 0
  letterCount = 0 
  
  for line in textFile:
    lineCount = lineCount + 1
    letterCount = letterCount + len(line)
    words = line.split()
    for w  in words:
      wordCount = wordCount + 1
    

  print("Words: ", wordCount)
  print("Lines: ", lineCount)
  print("Letters:", letterCount)

if __name__ == '__main__':
  main()
 

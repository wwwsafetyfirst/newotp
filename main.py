import math
import time
from datetime import datetime
while True:
  firsttimestamp = math.floor(time.time())
  sndtimestamp = firsttimestamp / 30
  if isinstance(sndtimestamp, int):
    thetimeis = sndtimestamp
    date = datetime.today()
    before1, sep1, after1 = date.partition("-")
    before2, sep2, after2 = after1.partition("-")
  else:
    thetimeis = math.floor(int(sndtimestamp))
alphabet = {
    'A': 11, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18, 
    'I': 19, 'J': 20, 'K': 21, 'L': 22, 'M': 23, 'N': 24, 'O': 25, 'P': 26, 
    'Q': 27, 'R': 28, 'S': 29, 'T': 30, 'U': 31, 'V': 32, 'W': 33, 'X': 34, 
    'Y': 35, 'Z': 36
}
# each secret key is 10 characters
def decode(key):
  char = {i + 1: key[i] for i in range(10)}
  dig = {}
  for i in key:
      if char[i].isdigit():
          if char[i] == '0':
              dig[i] = math.fsum(10,int(i)])
          else:
              dig[i] = math.fsum([int(char[i],int(i)])
      elif char[i].isalpha():
          dig[i] = alphabet[char[i]]
      else:
          return f"Character #{int(i)} is not a valid character"
  codev1 = math.prod([int(thetimeis),int(before1),int(before2),int(after3),int(dig[1]),int(dig[2]),int(dig[3]),int(dig[4]),int(dig[5]),int(dig[6]),int(dig[7]),int(dig[8]),int(dig[9]),int(dig[10])]) % 999999
  if codev1 <= 99999:
    digits = math.floor(math.fsum([int(math.log10(codev1)),1]))
    digits2 = math.fsum([6,-digits])
    code = codev1
    for _ in range(digits2):
      code = "0" + str(code)
return code

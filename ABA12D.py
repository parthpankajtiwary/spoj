import sys

def next_palindrome(number):
  number = str(number)
  number_len = len(number)
  number_len_half = number_len // 2
  
  left, middle, right = number[:number_len_half], (number[number_len_half:-number_len_half] or ''), number[-number_len_half:]
  
  if len(left) == 0 and len(middle) == 0:
    right = str(int(right) + 1)
    if right == 10:
      left = right = 1
  elif int(right) < int(left[::-1]):
    right = left[::-1]
  elif len(middle) > 0 and int(middle) < 9:
    middle = str(int(middle) + 1)
    right = left[::-1]
  else:
    left = str(int(left) + 1)
    if len(middle):
      middle = "0"
    right = left[::-1]
  
  palindrome = int(''.join((left, middle, right)))

  return palindrome

t = input()
for x in xrange(t):
  number = input()
  print(next_palindrome(number))
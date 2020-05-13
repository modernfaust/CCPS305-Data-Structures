def palindromeR (n,temp):
  try:
    if str(abs(n))[0] == str (abs(n))[-1]:
      return palindromeR(int(str(abs(n))[1:-1]),temp)
    else:
      return False
  except:
    return True

def isPalindrome(n):
  return palindromeR(n,0)

print(isPalindrome(859957))
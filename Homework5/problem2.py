 def isPalindrome(word):
  if len(word) <= 1: return True
  return (word[0] == word[-1]) and isPalindrome(word[1:-1])


if __name__ == '__main__':
    s = input()
  
    def is_true(n):
      if n:
        print("True")
      else:
        print("False")
        
    alnum=False
    for i in s:
      if i.isalnum():
        alnum=True
  
    alpha=False
    for i in s:
      if i.isalpha():
        alpha=True
  
    digit=False
    for i in s:
      if i.isdigit():
        digit=True
  
    lower=False
    for i in s:
      if i.islower():
        lower=True
  
    upper=False
    for i in s:
      if i.isupper():
        upper=True
  
    is_true(alnum)
    is_true(alpha)
    is_true(digit)
    is_true(lower)
    is_true(upper)
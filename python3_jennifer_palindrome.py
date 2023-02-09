string=input()
def palindrome(s):
    rev=s[::-1]
    if rev==s:
        print("palindrome")
    else:
        print("not palindrome")    
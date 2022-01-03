def is_palindrome_v1(s):
    return reverse(s) == s

def reverse(s):
    rev = ''
    for ch in s:
        rev = ch + rev
    return rev


print(reverse('hello'))

print(reverse('a'))

print(is_palindrome_v1('noon'))

print(is_palindrome_v1('racecar'))

print(is_palindrome_v1('dented'))
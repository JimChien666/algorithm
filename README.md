# algorithm course
1. palindrome
中文: 回文，如果單字正著看或倒著看都是長一樣的，他就是回文(algorithm)
舉例:
noon, racecar

- 方法一 確認單字正著看或倒著看都是長一樣的，他就是回文

```
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
```

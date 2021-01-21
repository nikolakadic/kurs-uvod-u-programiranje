def is_palindrome(string):
    return string == string[::-1]

def longest_palindromic_substring(string):
    i = 0
    palindrome_list = []
    while i < len(string):
        j = len(string) - 1
        while j > i:
            if string[i]==string[j]:
                if is_palindrome(string[i:j+1]):
                    palindrome_list.append(string[i:j+1])
                    break
            j -= 1
        i += 1
    return max(palindrome_list, key=len)

print(longest_palindromic_substring('asdahsanavolimmmmmmmmmmmilovanahfsh'))

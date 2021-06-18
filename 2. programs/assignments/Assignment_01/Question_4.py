# Developed By : Rishabh Gupta

# Question is- Write a Python program to find the first appearance of the substring 'not' and 'poor' from
# a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.
# Return the resulting string.
#
# Sample String : 'The lyrics is not that poor!'
# Expected Result : 'The lyrics is good!'


def replaceString(s1, s2, a):
    str1 = ''
    if (s2 > s1 and s1 > 0 and s2 > 0):
        str1 = a.replace(a[s1: s2 + 4], "good")
    return str1


if __name__ == '__main__':
    a = input("enter string-")
    s1 = a.find("not")
    print("first appearance of 'not' is-", s1)
    s2 = a.find("poor")
    print("first appearance of 'poor' is-", s2)

    print(replaceString(s1, s2, a))

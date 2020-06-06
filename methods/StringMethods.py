# # string methods
#
# # types of string--
# s = 'python'
# s2 = "python"
# s3 = '''python'''
#
# # two string literals together
# 'Hello-''World!'      # is 1 string
#
# # using parentheses
# s = ('Hello '
#       'World')
# print(s)
#
# # using triple quotes
# print('''He said, "What's there?"''')
#
# # escaping double quotes
# print("He said, \"What's there?\"")
#
# # triple quotes string used for multiple lines & doc-strings
# s4 = """Welcome to
#         the coding world"""
#
# print('last character-', s4[-1])
# print('slicing 2nd to 5th character-', s4[1:5])
# print('slicing 6th to 2nd last character-', s4[5:-2])
#
#
# print(list("string234"))     # ['s', 't', 'r', 'i', 'n', 'g', '2', '3', '4']
# print(tuple("srtingsstggnm22383329344"))
# # o/p-  ('s', 'r', 't', 'i', 'n', 'g', 's', 's', 't', 'g', 'g', 'n', 'm', '2', '2', '3', '8', '3', '3', '2', '9', '3', '4', '4')
#
#
# for i in 'it-is-string'.split('-'):
#     print(i, end=" ")
# print()
# for i in 'it-is-string':
#     print(i, end=" ")
# print()
#
#
# print('s' in "string")
# print("qwe" in "sstringqwqw")
# print("list is-", list(enumerate("string")))
#
# # capitalize-
# s = "coding WoRLd "
# print(s.capitalize())
# print("5oding WoRLd ".capitalize())
#
# # center-
# print("python".center(20, '*'))
#
# # casefold-
# print("lowercase str-", "PYTHON".casefold())
# print("lowercase str-", "PyThON".casefold())
# print("lowercase str-", "python".casefold())
#
#
# # count-
# print("no of times is-", "occurrences".count("cc", 1, 6))
#
# # endswith-
# text = "Python is easy to learn."
# print(text.endswith('to learn.'))        # True
# print(text.endswith('to learn'))         # Fakse
# print(text.endswith('Python is easy to learn.'))    # True
# print(text.endswith('easy', 7, 26))
#
# # with tuple-
# text = "programming is easy"
# print(text.endswith(('programming', 'python')))       # False
# print(text.endswith(('python', 'easy', 'java')))      # True
# # With start and end parameter
# print(text.endswith(('is', 'an'), 0, 14))          # True
#
#
# # expandtabs-
# str = 'xyz\t12345\tabc'
# print(str.expandtabs())
# print(str.expandtabs(5))
# print('Tabsize 6:', str.expandtabs(6))
#
# # find-
# s = 'Let it be, let it be, let it be'
# print(s.find('it', 6, 20))
# n = s.find('be')
# if (n != -1):
#     print("Contains substring 'be' at index-", n)
# else:
#     print("Doesn't contain substring")
#
# # index-
# print(s.find('it', 6, 20))
#
# # alphanum-
# name = "M234onica"
# print(name.isalnum())
#
# # contains whitespace so it is not alphanumeric-
# name = "M3onica Gell22er "
# print(name.isalnum())
#
# # isalpha-
# name = "Monica"
# print(name.isalpha())
#
# # contains whitespace
# name = "Monica Geller"
# print(name.isalpha())
#
#
# # isdecimal
# print('12395'.isdecimal())   # True
# print('965.5'.isdecimal())   # False
# print('12fdf395'.isdecimal())   # False
# print('@12434324'.isdecimal())   # False
#
# # s = '²3455'
# s = '\u00B23455'
# print(s.isdecimal())          # False
#
# # s = '½'
# s = '\u00BD'
# print(s.isdecimal())           # False
#
# # isdigit-
# #s = '²3455'
# # subscript is a digit
# s = '\u00B23455'
# print(s.isdigit())           # True
#
# # s = '½'
# # fraction is not a digit
# s = '\u00BD'
# print(s.isdigit())           # False
#
# isnumeric-
# #s = '²3455'
# s = '\u00B23455'
# print(s.isnumeric())            # true
#
# # s = '½'
# s = '\u00BD'
# print(s.isnumeric())            # true
#
# # below all 3 stmts are False-
# print("12.456".isnumeric())
# print("12.456".isdigit())
# print("12.456".isdecimal())
#
#
# # isidentifier-
# str = 'Python'
# print(str.isidentifier())       # true
# str = ''
# print(str.isidentifier())       # False
# str = 'root33'
# print(str.isidentifier())        # a valid identifier
# str = '33root'
# print(str.isidentifier())         # not a valid identifier
# str = 'root 33'
# print(str.isidentifier())          # not a valid identifier
#
#
# # isspace-
# s = '   \t'
# print(s.isspace())                    # true
# s = ' a '
# print(s.isspace())                  # False
# s = ''
# print(s.isspace())                 # False
# s = '\t  \n'
# print(s.isspace())                 # True
#
#
# # isTitle-
# s = 'Python Is Good.'
# print(s.istitle())               # True
# s = 'Python is good'
# print(s.istitle())                # False
# s = 'This Is @ Symbol.'
# print(s.istitle())                   # True
# s = '99 Is A Number'
# print(s.istitle())             # True
# s = 'PYTHON'
# print(s.istitle())              # False
#
#
# # isupper-
# string = "THIS IS GOOD!"
# print(string.isupper())
#
# # join-
# # ex 1-
# print(" ".join(['1', '2', '3']))
# print(type("@".join(('1', 'sss0', '3.34@#'))))
# print(("@".join(('1', 'sss0', '3.34@#'))))
#
# # ex 2-
# t = {'Python', 'Java', 'Ruby'}
# s = '->->'
# print(s.join(t))
#
# # ex 3- on dict-
# # d = {1: 'a', 2: "b", 3: 'c'}
# # sep = " -> "
# # print(sep.join(d))
# # since it joins keys only, so error is- "expected str instance, int found". So, keys must be string for concatenation.
#
# # ex 4-
# d = {'1': 'a', '2': "b", '3': 'c'}
# sep = " -> "
# print(sep.join(d))
#
#

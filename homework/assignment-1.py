# 1. For a given string, change all occurrences of its first character to '&', except the first character itself.
# Example string: 'exercise'
# Expected output: 'ex&rcis&'


eg_string = 'tentacles'
first_ch = eg_string[0]
temp_string = eg_string.replace(first_ch, '&')
final_string = first_ch + temp_string[1:]
print(final_string)


# 2. Find all occurrences of a substring in a given text by ignoring the letter case.
# text = 'We few, we happy few, we band of brothers  '
# substring = 'We'
# Expected output: 3

text = 'We few, we happy few, we band of brothers  '
substring = 'We'
counter = text.lower().count(substring.lower())
print(counter)

# 3. Find the last position (index) of a given substring. example text: 'I felt happy because I saw the others were
# happy and because I knew I should feel happy, but I wasn’t really happy.' example substring: 'happy' Expected
# output: 109
text= "I felt happy because I saw the others were happy and because I knew I should feel happy, but I wasn’t really happy. "
substring = "happy"
res = text.rfind(substring)
print(res)

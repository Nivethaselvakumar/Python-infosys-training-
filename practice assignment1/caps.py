def only_upper(s):
    upper_chars = ""
    str1="I Like C"
    str2="Mary Likes Python"
    str3=str1+str2
    for char in str3:
        if char.isupper():
            upper_chars += char
    return upper_chars

print only_upper(upper_chars)


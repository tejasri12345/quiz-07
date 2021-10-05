str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
str1_len = len(str1)
str2_len = len(str2)
count = 0
if(str1_len == str2_len):
    for i in str1:
        if i in str2:
            count += 1
            continue
        else:
            break
    if(count == str1_len or count == str2_len):
        print("It is anagram")
    else:
        print("It is not a anagram")
else:
    print("It is not a anagram because its length is different");


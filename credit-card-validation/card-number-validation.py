import re

for _ in range(int(input())):
    s=input()
    t=re.search(r"^[456]\d{15}$|^[456]\d{3}-\d{4}\d-{4}\d-{4}$",s)
    if(t):
        if(re.search(r"(\d)\1{3,}|(\d)\2{1}-(\d)\2{1}|-(\d)\4{3}-",s)):
            print("invalid")
        else:
            print("valid")
    else:
        print("invalid")           
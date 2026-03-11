s1 = "buy now"
s2 = "click this"
s3 = "make a lot of money"
s4 = "subscribe this"

comment = input("Write your comment: ").lower().strip()

# detacting the spam words

if s1 in comment or s2 in comment or s3 in comment or s4 in comment :
    print("This comment is a spam.")
else :
    print("This comment is not a spam.")

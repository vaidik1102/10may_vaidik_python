#Write a Python program to unzip a list of tuples into individual lists.
t= [(1,2), (3,4), (5,6)]
print(list(zip(*t)))
print ("hello world")
def feb(n):
    if n>2:
        return feb(n-2)+feb(n-1)
    else:
        return 1
print(feb(5))

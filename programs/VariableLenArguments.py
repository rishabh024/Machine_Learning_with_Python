# find even no and odd nos in variable length argument

def var(*arg):
    even = []
    odd = []
    for i in arg:
        if (i % 2 == 0):
            even.append(i)
        else:
            odd.append(i)
    return even, odd

ev, od = var(1, 2, 3, 4, 5, )
print("even  no-", ev)
print("odd  no-", od)

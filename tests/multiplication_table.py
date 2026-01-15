def multiplication_table(n):
    multiplestable = []

    if n < 0:
        raise ValueError("marks must be above 0")
    elif type(n) != int:
        raise TypeError("each mark must be an integer")
    else:
        for i in range(1,n+1):
            multiples = []
            for num in range(1, n+1):
                multiples.append(num*i)
            multiplestable.append(multiples)
        return multiplestable



multiplication_table(3)
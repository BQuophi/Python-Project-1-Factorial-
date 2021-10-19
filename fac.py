def factorial(n): 
    if n<=1:
        return 1
    else:
        if n> 1:
            n_fac= n* factorial(n-1)
        return n_fac
        
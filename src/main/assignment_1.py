from __init__ import *

# Function
def double_precision():
    s = 0
    exp = 10000000111
    c, i = 0, 0
    while (exp != 0):
        e = exp % 10
        c = c + e * pow(2, i)
        exp = exp // 10
        i = i + 1
    
    fraction = str(111010111001000000000000000000000000000000)
    f = 0
    i = 1
    for item in fraction:
        f = f + int(item) * (0.5**i)
        i = i + 1
    
    # Question 1:
    num = ((-1)**s)*(2**(c - 1023))*((1 + f))
    ans = num
    print("{:.4f}".format(num), '\n')
                                    
    # Question 2:
    num *= (10 ** -3)
    num = math.floor(num * 1000) / 1000
    num *= 1000
    print(num, '\n')

    # Question 3:
    num += .500
    print((round(num, ndigits = 0)), '\n')

    # Question 4:
    def absolute(precise: float, approx: float):
        return abs(precise-approx)


    def relative(precise: float, approx: float):
        return abs((absolute(precise, approx)) / abs(precise))
                             
    print(absolute(ans, round(ans, 0)))
    print(relative(ans, round(ans, 0)), '\n')

# Question 5:
def question_5():
    def series(x, k: int):
        return((-1) ** k) * ((x ** k) / ( k ** 3))
    min_error = 1e-4
    current_iteration = 1
    while(abs(series(1, current_iteration)) > min_error):
        current_iteration +=1
    print(current_iteration - 1, '\n')
    return

# Question 6:
def question_6():
    def bisection_method(f, a, b, accuracy):
        if np.sign(f(a)) == np.sign(f(b)):
            raise Exception("The scalars a and b do not bound a root")
        mid = (a + b) / 2
        if np.abs(a - b) <= accuracy:
            return 0
        elif np.sign(f(a)) == np.sign(f(mid)):
            return bisection_method(f, mid, b, accuracy) + 1
        elif np.sign(f(b)) == np.sign(f(mid)):
            return bisection_method(f, a, mid, accuracy) + 1
        
    def newton_raphson_method(f, df, start, accuracy):
        end = f(start) / df(start)
        x = start
        count = 1
        while (abs(end) >= accuracy):
            x = x - end
            count = count + 1
            end = f(x) / df(x)
        return count
    
    f_x = lambda x: (x ** 3) + (4 * (x ** 2)) - 10
    df_dx = lambda x: 3 * (x ** 2) + (8 * x)
    print(bisection_method(f_x, -4, 7, 0.0001), '\n')
    print(newton_raphson_method(f_x, df_dx, 7, 0.0001))

        
double_precision()
question_5()
question_6()
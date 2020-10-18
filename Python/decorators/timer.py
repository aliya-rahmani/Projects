import time
def timer(fun):
    """
    Print the execution time of fun.
    Use this decorator function as follows:

    @timer
    def function()

    """

    def wrapper(*args, **kwargs):
        start = time.time()
        val = fun(*args, **kwargs)
        end = time.time()
        print("*"*100,'\n\n', fun.__name__, "execution time: ", end - start," sec\n\n","*"*100,'\n')
        return val

    return wrapper

@timer
def timeCounsuingFun(to):
    for _ in range(0,to):
        pass
    
timeCounsuingFun(10000000)

def my_decorator(function_parameter):

    def function_wrapper():
        print("This will be called before the function execution.")

        function_parameter()

    return function_wrapper

@my_decorator
def hello_world():
    print("Hello, World!")

hello_world()
# This will be called before the function execution.
# Hello, World!
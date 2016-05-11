# function for call more than one function after tkinter button click
# add to the button: command=combie_funcs(funtion1, function2)
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)

    return combined_func
def combine_funcs(*funcs):
    """
    combine_funcs

    Functionality for registering more than one command on a tkinter button click event.

    :param funcs: different, comma separeted functions
    :return: returns the combined functions
    """
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)

    return combined_func
def udalyator(object):
    def new_def(*args):
        print(str(object.__name__), 'стерта, старого не вернуть')
    return new_def


@udalyator
def im_a_function():
    print('Написанное не сотрешь')

im_a_function()

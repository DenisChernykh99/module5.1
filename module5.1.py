def test_function():
    def inner_function():
        print('Я в области видимости функции test function')
    inner_function()
inner_function()

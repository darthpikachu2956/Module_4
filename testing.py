def test_function():
    def inner_function():
        print('Я в области видимости функции test_function.')
    inner_function()


test_function()
# inner_function() - За пределами внешней функции внутренняя не вызывается, так как
#                    без внешней её не существует.

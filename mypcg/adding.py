def adding_to_lib(my_lib: dict) -> None:
    while True:
        print('Return для закінчення вводу')
        big_url = input('введіть повний URL: ')
        if big_url:
            name = input('введіть короткий URL: ')
            my_lib[name] = big_url
        else:
            print('end of input!')
            break

def lib_out(my_lib: dict):
    if len(my_lib) == 0:
        print("No data")
        print()
    else:
        for key in my_lib:
            print(f'short url: {key} normal url {my_lib[key]}')
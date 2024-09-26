def search_in(my_lib: dict, search_name: str):
    found_something = False
    for key in my_lib:
        if key.lower() == search_name.lower():
            print(my_lib[key])
            input()
            found_something = True
            break
        continue
    if not found_something:
        input('nothing found')
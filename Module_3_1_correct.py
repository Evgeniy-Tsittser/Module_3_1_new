calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    my_tuple = (len(string), string.upper(), string.lower())
    count_calls()
    return my_tuple


def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        if string.lower() in i.lower():
            a = True
        else:
            a = False
    return a


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)


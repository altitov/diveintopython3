import humanize

a_string = '{0} {1} {2}'
print(a_string.format(3, 5, 6))

si_suffixes = humanize.suffixes['decimal']
print(si_suffixes)

print('1000{0[0]} = 1{0[1]}'.format(si_suffixes))

url = 'https://www.google.ru/search?newwindow=1&q=%D0%B1%D0%B0%D0%B9%D0%BA%D0%B5%D1%80%D1%81%D0%BA%D0%B0%D1%8F+%D0%BA%D1%83%D1%80%D1%82%D0%BA%D0%B0&tbm=isch&tbs=simg:CAQSlwEJjW_1wFw4PWN0aiwELEKjU2AQaBAgACAMMCxCwjKcIGmIKYAgDEii4EJwEtxDdDpgFuhC3Gd4OzQ6dBO8tyS3jOaUuoy7MK-I5xjqoLsU6GjAYWlKl9L3S_17R3YLlU1pWPyDeLNBWRHGrjDjjN_1L3TtPL8Cgsg5dg4h3eqzp8Nq28gBAwLEI6u_1ggaCgoICAESBG4JE28M&sa=X&ved=0ahUKEwjZm8TOie7PAhWoFJoKHYlhCY8Q2A4IHCgB&biw=1920&bih=964#imgrc=nGSwNKSuev3zAM%3A'
a_list = url.split('&')[1:]
print(a_list)
a_list_of_lists = [v.split('=', 1) for v in a_list]
print(a_list_of_lists)
a_dict = dict(a_list_of_lists)
print(a_dict)

by = b'abcd\x65'
by += b'\xff'
print(by)
print(type(by))
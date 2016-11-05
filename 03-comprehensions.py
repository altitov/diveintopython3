import os
import glob
import time
import humanize


dnldpathmask = 'c:/users/h8/downloads/*.*'
pathname = 'c:/users/h8/test.txt'
filename = 'foobar.py'

print(os.getcwd())
print(os.path.join(os.path.expanduser('~'), '123.txt'))
print(os.path.split(pathname))
print(os.path.splitext(filename))
curfiles = glob.glob('*.*')
for f in curfiles:
    print('%s is %i bytes : created in %i' % (f, os.stat(f).st_size, time.gmtime(os.stat(f).st_atime).tm_year))
    print(os.path.realpath(f))


a_list = [1, 2, 3, 6, 7]
print(a_list)
print([elem * 2 for elem in a_list if elem >= 2])

print([(os.stat(f).st_size, os.path.realpath(f)) for f in glob.glob('c:/users/h8/desktop/*.*')])
print({f:humanize.naturalsize(os.stat(f).st_size) for f in curfiles})

print([f for f in glob.glob(dnldpathmask) if os.stat(f).st_size < 10000])

print(humanize.naturalsize(12))

a_dict = {f:humanize.naturalsize(os.stat(f).st_size) for f in curfiles}
print(a_dict)
print({value:key for key, value in a_dict.items()})

a_set = set(range(11))
print(a_set)
print({a**2 for a in a_set if a % 2 == 0})
print({x**3 for x in range(6)})
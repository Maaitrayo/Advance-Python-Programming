import sys
import getopt

# print(sys.argv)
# print(sys.argv[1])

opts, args = getopt.getopt(sys.argv[1:], "f:m:", ['filename', 'message'])
# print(opts)
# print(args)

for opt, arg in opts:
    if opt =='-f':
        filename = arg
    if opt == '-m':
        message = arg

print(filename, message)






# Argument passing in functions
def myFunction(*args, **kwargs):
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])
    print(kwargs['KEYONE'])
    print(kwargs['KEYTWO'])

# myFunction('hey', True, 19, 'wow', KEYONE='TEST', KEYTWO=7)
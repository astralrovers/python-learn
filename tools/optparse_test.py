from optparse import OptionParser

parse = OptionParser(usage='usage: %prog [options] test usage', version='%prog v1.0')

parse.add_option('-f', '--file', action='store', dest='filename', default='test.txt',
        help='write to file', metavar='FILE')

(options, args) = parse.parse_args()

print(options)
print(options.filename)
print(args)

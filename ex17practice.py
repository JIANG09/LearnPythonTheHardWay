from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from %s to %s." % (from_file, to_file))

indata = open(from_file).read()

print('''The input file is %d bytes long.
Does the output file exists? %r ''' % (len(indata),exists(to_file)))

out_file = open(to_file, 'w').write(indata)
print("Alright, all done.")




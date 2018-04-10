from sys import argv
from os.path import exists

script, from_file, to_file = argv

out_file = open(to_file, 'w').write('%s' % open(from_file).read())
print("Alright, all done.")

# cat: concatenate and print files, writing them to the standard output.
from sys import argv
from os.path import exists

script, from_file, to_file = argv
in_data = open(from_file).read()

print(f"""The input file is {len(in_data)} bytes long.
Does the output file exist? {exists(to_file)}.
Ready, hit RETURN to continue, hit CTRL-C to abort.""")
input()

out_file = open(to_file, 'w').write(in_data)
print("Alright, all done.")

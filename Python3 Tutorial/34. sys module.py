import sys

sys.stderr.write('This is stderr text\n')
sys.stderr.flush()
sys.stdout.write('This is stdout text\n')

print(sys.argv)  # argument name in the command line you passed in

if len(sys.argv) > 1:
    print(sys.argv[1])


def main(argv):
    print(argv)


main(sys.argv[1])

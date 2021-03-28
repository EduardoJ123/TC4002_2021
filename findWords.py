import sys
file_name = sys.argv[1]
file = open(file_name, "r")
text = file.read()
for arg in range(2, len(sys.argv)):
    print(sys.argv[arg], text.count(sys.argv[arg]), sep=": ")

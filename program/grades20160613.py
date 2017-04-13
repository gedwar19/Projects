#
fname = input("Enter the name of the file: ")
fin = open(fname, "r")
# for writing  fout = open(fname, "w")

for line in fin:
    line = line.strip()
    if line != "":
        parts = line.split (" ")
        name = parts[0]
        total = 0
        for i in range (1, len(parts)):
            total = total + int(parts[i])
        avg = total / (len(parts) - 1)
        print ("%s %.2f " % (name, avg))
    

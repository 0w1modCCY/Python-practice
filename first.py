name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hours = dict()

for line in handle:
    line = line.rstrip()
    if line.startswith("From "):
        word = line.split()
        time = word[5].split(":")
        h = time[0]
        hours[h] = hours.get(h, 0) + 1

lst = list()
for key,val in hours.items():
    newtup = (key, val)
    lst.append(newtup);

lst.sort()
for k,v in lst:
    print(k, v)

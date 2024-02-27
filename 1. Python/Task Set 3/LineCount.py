#print no. of lines
fd = open('file.txt')
lst = fd.readlines()
print(f"No. of Lines = {len(lst)}")


#print no.of words
fd = open('file.txt')
lst = fd.read()
print(f"No. of Words = {len(lst.split())}")

#print no.of letters
fd = open('file.txt')
lst = fd.read()
print(f"No. of Letters = {len(lst)}")

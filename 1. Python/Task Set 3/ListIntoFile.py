ls = ['Hello', 'World']
fd = open("file2.txt",'w')
for i in ls:
    fd.write(" ".join(i))
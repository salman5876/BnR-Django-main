newf=""
with open('textScript.txt','r') as f:
    for line in f:
        newf+=line.strip()+","
    f.close()
with open('textScript.txt','w') as f:
    f.write(newf)
    f.close()
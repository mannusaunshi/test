fr = open("diploma boards",'r')
fw = open("new_diploma boards",'w')
lines = fr.readlines()
for line in lines:
	fw.write('<option value ="'+line+'">'+line+'</option>\n')
fr.close()
fw.close()

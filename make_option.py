fr = open("universities.txt",'r')
fw = open("option_output.txt",'w')
lines = fr.readlines()
for line in lines:
	line_n = line.strip().replace(" ","_")
	fw.write('<option value ="'+line_n+'">'+line+'</option>\n')
fr.close()
fw.close()
import re

#regex1 sorts input to only get Zone names
#regex2 sorts input to only get coordinates
regex1 = "(Labyrinthos|Thavnair|Garlemald|Mare Lamentorum|Elpis|Ultima Thule)"
regex2 = "\((\d|\s|\.|\,|\-)+\)"

#opens input.txt containing input data
with open('input.txt') as text:
    for line in text:
      for match1 in re.finditer(regex1, line):
        zs = match1.start()
        ze = match1.end()
        for match2 in re.finditer(regex2, line):
            cs = match2.start()
            ce = match2.end()
            #replace with output to file later
            print("/coord " + (line[cs:ce]) + " : " + (line[zs:ze]))
 
text.close()

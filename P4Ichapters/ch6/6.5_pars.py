text = "X-DSPAM-Confidence:    0.8475";

zpos = text.find('0')
print zpos

fpos = text.find('5',zpos)
print fpos

dtext = text[zpos:fpos+1]
float(dtext)

print dtext

import re

matcher = re.finditer("[A-Za-z0-9]","TCAAq32345kjdfjBTCAC54D543TCATCA")

for m in matcher:
	print(m.start(),"---",m.end(),"---",m.group())

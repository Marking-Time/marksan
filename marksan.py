import re

with open("bookmarks.html", "r") as file:
	content = file.read()

BEGIN_BIOLERPLATE = "<html><head><title>Marksan</title></head><body><h1>H1</h1><h3>H3</h3><p>paragraph</p>untagged text"
END_BIOLERPLATE = "</body></html>"

A_TAG_BEGIN = "<a href= "
A_TAG_href = ""
A_TAG_TARGET = "'_blank'"
A_TAG_text = ""
A_TAG_END = "</a>"

pat = "<A HREF=.+</A>"

res = re.findall(pat,content)
if res:
	print("yes")
else:
	print("no")

for mat in res:
	a = re.search("<A HREF=(\"\S+\")", mat)
	# print(a[1])
	A_TAG_text = re.search(">(.+)</A>", mat)

	# A_TAG_text = str(A_TAG_text)
	A_TAG_href = a[1]
	print(f"A_TAG_text = {A_TAG_text[1]}")
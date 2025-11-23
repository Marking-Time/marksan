import re

with open("bookmarks.html", "r") as file:
	content = file.read()

BEGIN_BIOLERPLATE = "<html><head><title>MarkSan</title></head><body><h1>MarkSan</h1><p>Bookmark Sanitizer</p>"
END_BIOLERPLATE = "</body></html>"

A_TAG_BEGIN = "<a href= "
A_TAG_href = ""
A_TAG_TARGET = "'_blank'>"
A_TAG_text = ""
A_TAG_END = "</a>"

pat = "<A HREF=.+</A>"

res = re.findall(pat,content)
if res:
	print("yes")
else:
	print("no")

category_list = []

for mat in res:
	a = re.search("<A HREF=(\"\S+\")", mat)
	# print(a[1])
	A_TAG_text = re.search(">(.+)</A>", mat)

	A_TAG_text = A_TAG_text[1]
	A_TAG_href = a[1]
	# print(f"A_TAG_text = {A_TAG_text[1]}")
	output_A_tag = f"{A_TAG_BEGIN}{A_TAG_href} target={A_TAG_TARGET}{A_TAG_text}{A_TAG_END}"
	# print(output_A_tag)

	category = re.search("-(.+)$", A_TAG_text)
	if category != None:
		category = category[1].strip()
	# print(type(category))
	if category not in category_list:
		# print(category[1])
		category_list.append(category)

print(category_list)
import re
# Opens and reads bookmarks.html
with open("bookmarks.html", "r") as file:
	content = file.read()

# HTML strings to build file
BEGIN_BIOLERPLATE = "<html><head><title>MarkSan</title></head><body><h1>MarkSan</h1><p>Bookmark Sanitizer</p>"
END_BIOLERPLATE = "</body></html>"

A_TAG_BEGIN = "<a href= "
A_TAG_href = ""
A_TAG_TARGET = "'_blank'>"
A_TAG_text = ""
A_TAG_END = "</a>"

pat = "<A HREF=.+</A>"

res = re.findall(pat,content)

category_list = {}

# loop to create stuff in Anchor tag using regex to parse bookmarks.html
for mat in res:
	a = re.search("<A HREF=(\"\S+\")", mat)	
	A_TAG_text = re.search(">(.+)</A>", mat)

	A_TAG_text = A_TAG_text[1]
	A_TAG_href = a[1]	
	output_A_tag = f"{A_TAG_BEGIN}{A_TAG_href} target={A_TAG_TARGET}{A_TAG_text}{A_TAG_END}"
	
	category = re.search("~(.+)$", A_TAG_text)
	if category != None:
		category = category[1].strip()
	
	if category not in category_list:
		category_list[category]=[]
		category_list[category].append(output_A_tag)
	else:
		category_list[category].append(output_A_tag)

#  building html file
HTML_output = BEGIN_BIOLERPLATE

for cat in category_list:
	if cat != None:
		HTML_output = HTML_output + f"<h3>{cat}</h3>"
		for item in category_list[cat]:
			if item != None:
				HTML_output = HTML_output + "<br>" + item

HTML_output = HTML_output + END_BIOLERPLATE

# Create marksan.html and write HTML_output
with open("marksan.html", "w") as f:
	f.write(HTML_output)

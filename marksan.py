import re

with open("bookmarks.html", "r") as file:
	content = file.read()
	# print(content)

	# for line in content:
	# 	line = content.readline()
	# 	print(line.strip())
	# 	print()

# with open("bookmarks.html", "r") as file:
# 	for line in file:
# 		line = file.readline()
# 		print(line)
# 		print()
pat = "<A HREF=.+</A>"

res = re.findall(pat,content)
if res:
	print("yes")
else:
	print("no")

for mat in res:
	a = re.search("<A HREF=(\"\S+\")", mat)
	print(a)
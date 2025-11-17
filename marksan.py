import re

with open("bookmarks.html", "r") as file:
	content = file.read()
	# print(content)

	for line in content:
		print(line)
		print()

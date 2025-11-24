# marksan
This code takes the bookmarks.html file as it is  output from firefox, removes the favicon identifier and places the clean results in marksan.html file.  
## Purpose
Firefox added tacking code to the bookmarks.html file when I used the ff utility to download it. The marksan.py (bookMARK SANitizer) code parses the bookmarks.html file and creates a new file without the tracking code. The resulting file can be used in place of ff bookmarks when accessing bookmarked sites.
## Notes
Code runs correctly, but yields a regex warning on non excaped characters. This does not affect function and it is'nt worth more of my time to find the problem.  Detail: The escaped qoutes didn't work with ".+" so I used "/s". 
## Usage
1) Create bookmarks in Firefox(ff) with a tilde(~) at the end of the description.  The text following the tilde will be used as a category heading in the output. Example: "Some website description ~ category". 
2) Use the ff html export function to create the bookmarks.html file.
3) Save the bookmarks.html file to the same direactory as the marksan.py file.
4) Run marksan.py. This creates the marksan.html file.
5) Open the marksan.html file in a browser and use the links in the file as a replacement for bookmarks in ff.
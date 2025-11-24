# marksan
This code takes the bookmarks.html file as it is  output from firefox, removes the favicon identifier and places the clean results in marksan.html file.  
## Purpose
Firefox added tacking code to the bookmarks.html file when I used the ff utility to download it. The marksan.py (bookMARK SANitizer) code parses the bookmarks.html file and creates a new file without the tracking code. The resulting file can be used in place of ff bookmarks when accessing bookmarked sites.
## Notes
Code runs correctly, but yields a regex warning on non excaped characters. This does not affect function and it is'nt worth more of my time to find the problem.  Detail: The escaped qoutes didn't work with ".+" so I used "/s". 
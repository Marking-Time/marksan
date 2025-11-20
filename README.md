# marksan
This code takes the bookmarks.html files as output from from firefox and removes the favicon identifier.  
## Purpose
Firefox added tacking code to the bookmarks.html file when I used the ff utility to download it. The marksan.py (bookMARKSANitizer) code parses the bookmarks.html file and creates a new file without the tracking code. The resulting file can be used in place of ff bookmarks when accessing bookmarked sites.
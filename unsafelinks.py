#!/usr/bin/python3
import urllib
import re
import sys
#from urllib.parse import urlparse
from urllib.parse import unquote

#deobfuscate ATP safelinks, By Ryan Coryell

#url to decode
origUrl = input ('Please enter the safelink you want to decode:  ')

#testing
#test1 = urllib.parse.unquote(orig_url)
#print (test1)

#split to list after ? and keep the second break only
urlParts = origUrl.split("?")[1]

#testing
#print (url_parts)
#print (url_parts[1].split("&"))

#split the url into parts at the ampersand
linkParams = urlParts.split("&")

#testing
#print (link_params)

#loop for listing out the three different parts remaing in the safelink.  for now the URL is all we care about, in the future I may figure out what to do with the rest.  
for links in linkParams:
    linkVal = links.split("=")
    
    if linkVal[0] == "url":
        
        encodedLink = linkVal[1]
        
        #more testing
        #print (encodedLink)
        
        break
    else :
        print ('Valid safelink not found')
        sys.exit (1)
#use the unquote function to decode the link
link = urllib.parse.unquote(encodedLink)   
print (' ')
#output yay! 
print (link)
    



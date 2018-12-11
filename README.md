# unsafelinks
deobfuscating microsoft safelinks
Microsoft Safelinks is both good and bad. The good lies in that users are provided with improved protection because Microsoft is resolving the link ahead of time and determining to the best of their ability weather it is a malicious site.

The bad is that the hyperlink is almost unreadable to the common person. The obfuscated links look something like this.

https://na01.safelinks.protection.outlook.com/url=
https%3A%2F%2Fyugecyber.com%2F&
data=02%7C01%7C****_*******%40*******.com
%7C3a2a5ba689234a5dfe6b08d65a38d61f
%7C94a74758f2ff413c9f705725701b8d02
%7C0%7C0%7C636795597490344404&s
data=QFY6Fsvgw%2FrqCB1cq%2BQPc8CYUy7t7OYNRr2lixcgKXU
%3D&reserved=0
Most of this here is junk. This junk relates to Microsoft’s classification of the hyperlink and is really only useful to them. When I first saw all of this I over complicated the whole thing. It was not until I was researching LogRhythm’s Phishing Intelligence Engine and dug into their de-obfuscation of these links that it became clear to me to just throw most of this out and to look for the encoded url. So i dug into this some more and wrote this little python script to clean up the mess for me.


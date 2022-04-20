#pip install google

from googlesearch import search

term = str(input("Enter your search:"))

for i in search(term, lang="es"):
	print(i)

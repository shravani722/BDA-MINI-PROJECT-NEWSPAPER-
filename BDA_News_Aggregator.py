import newspaper
from newspaper import Article
from newspaper import fulltext
import subprocess
import tkinter as tk
from PIL import ImageTk, Image  
import operator    

truncate_ =['on','said','their','there','in','under','between','behind','back','front','of','as','to','besides','before','after','if','because','but','and','an','a','the','is','was','were','had','have','are']

word_count={}
url = input('Enter the URL of the news article: ')
article = Article(url)
article.download()
article.parse()
f= open("article_content.txt","w+")
f.write(article.text)
f.close
f = open("keyword_count.txt","w+")
subprocess.call(['./bda_script.sh'])
article.nlp()
print('-->TITLE: ', article.title)
print('\t****\n')

if len(article.authors)>0:
	print('-->AUTHORS/ PUBLISHER: ',)
	for author in article.authors:
		print(author,'\t',) 
print('\t****\n')

print('-->PUBLISH DATE: ', article.publish_date)
print('\t****\n')

print('-->ARTICLE CONTENT: ', article.text[:250])
print('\t****\n')

if article.summary != '':
	print('-->SUMMARY: ', article.summary)
	print('\t****\n')

if len(article.keywords)>0:
	#print('-->KEYWORDS (NLP Library): ')
	#for keyword in article.keywords:
		#print(keyword,', ',end='')
	#print('\n\t****\n')
 
	print('-->KEYWORDS(NLP Library): ')

f = open("keyword_count.txt", "r")
if len(article.keywords)>0:
	for line in f:
		if line.split()[0][-1].islower == False: 
			word = line.split()[0][:-1]
		else:
			word = line.split()[0]
		if word in article.keywords: 
			print('[',word,', ',line.split()[1],']', end='')
		if word not in truncate_ and len(word)>4:
			word_count[word] = line.split()[1] 
print('\n\t****\n')


	
sorted_keys = sorted(word_count, key=word_count.get, reverse=True)

print('-->KEYWORDS (MAP REDUCE): ')

for r in sorted_keys:
	keywords_ = sorted_keys[:len(article.keywords)]

for w in keywords_:
	print('[',w,', ',word_count[w],']', end='')


print('\n\t****\n')

print ('-->SIMILARITY: ',((len(set(keywords_) & set(article.keywords))/len(article.keywords))*100)+20,'%')
print('\n\t****\n')

print('-->ARTICLE HTML: ', article.html[:250])
print('\n\t****\n')

if article.top_image != '':
	print('-->ARTICLE TOP IMAGE: ', article.top_image)
	print('\n\t****\n')

if len(article.movies)>0:
	print('-->RELEVANT VIDEOS: ')
	for movie in article.movies:
		print(movie,', ',end='')
	print('\n\t****\n')


'''window = tk.Tk()
window.title("TOP IMAGE")
window.geometry("300x300")
window.configure(background='grey')

path = article.top_image

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "bottom", fill = "both", expand = "yes")

#Start the GUI
window.mainloop()'''












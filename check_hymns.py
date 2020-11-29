NUM_HYMNS = 1348;


for i in range(1, NUM_HYMNS + 1):
	f = open('hymn' + str(i) + '.txt','r')
	filedata = f.read()
	f.close()

	newdata = filedata.replace("&mdash;","-")

	f = open('hymn' + str(i) + '.txt','w')
	f.write(newdata)
	f.close()

# &#8217;
# &mdash;

	# f = open('hymn' + str(i) + '.txt', 'r+')
	# for word in f.read().split():
	# 	if "&#8217;" in word:
	# 		f.write(word.replace("&#8217;", "HOHO"))
	# 		print("FOUND IT !!!!!!!")





# "hymn' + str(i) + '.txt"



	# words = 0
	# f = open ('hymn' + str(i) + '.txt', 'r+')
		
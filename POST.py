
import nltk

# i used all of the sentences.
#-------------------------------------------POINT 1 #Create the vocabulary, frequency, and tag information table.
def read():
	dictionary = {}
	daftarTag = []
	with open('word_tag.txt') as data:
		while True:
			s_id =data.readline()
			s_id =s_id.lower()
			if len(s_id.strip()) == 0 :
				continue
			if "#eot#" in s_id:
				break
			sentence =""
			if("#" in s_id):
				continue
			else:
				sentence = s_id
				sentence = sentence.split("\t")
				if(sentence[2] == "_"):
					tag = sentence[3]
				else:
					tag = sentence[2]
				if tag not in daftarTag:
					daftarTag.append(tag)
			if(sentence[1] in dictionary):
				if(tag in dictionary[sentence[1]]):
					dictionary[sentence[1]][tag] += 1
				else:
					dictionary[sentence[1]][tag] = 1
			else:
				dictionary[sentence[1]] = {}
				dictionary[sentence[1]][tag] = 1

	return dictionary,daftarTag 
def loadKalimat(): # load  all sentence to be train set(#eot#) and validation set(#eof#). 
    with open('word_tag.txt') as data:
        sentence = data.readline()
        while "#eot#" not in sentence:
            sentence = data.readline()
        hasil =[]
        while True:
            sentence = data.readline()
            sentence = sentence.lower()
            if "#eof#" in sentence:
                break
            if "# text = " in sentence:
                sentence = sentence.split("# text =")
                sentence = sentence[1]
                sentence = sentence.replace("\n","")
                hasil.append(sentence)
    return hasil
a = read()
# counting each tag
daftarTag = a[1]
dictionary = a[0]
count_tag = {}
for j in dictionary:
		for k in dictionary[j]:
			count_tag[k] = 0 

for i in range(len(daftarTag)):
	for j in dictionary:
		for k in dictionary[j]:
			if daftarTag[i] == k :
				
				count_tag[k] = count_tag[k] + 1 
# print(count_tag)



#------------------------------------------------------POINT 2 Create the probability of a word labeled with a tag (emission probability) table.
emission = {}
for i in (dictionary):
	for j in (dictionary[i]):
		emission[i]={}

for i in (dictionary):
	for j in (dictionary[i]):
		emission[i][j] = dictionary[i][j]/count_tag[j]

#print(emission)



#-----------------------------------------------------POINT 3 Create a POSTagger based on highest emission probability table.
h = loadKalimat()
h = nltk.word_tokenize(h[11])# this is only for the first sentence in validation set. just change the number if want to test the other sentences.
for i in emission:
	if i in h:
 		print(i, max(emission[i].items()))







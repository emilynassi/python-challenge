import re
f = open("paragraph.txt","r")
passage = f.read() 

#find approximate word count
word_count = len(re.findall('\w+', passage))
 
separators = "." or "?" or "!"
#find aproximate sentence count
sentence_count = passage.count(separators)

#split up words by spaces
words = passage.split()
#count characters in each word, add together and divide by amount of all words
character_count = sum(len(word) for word in words) / len(words)

#Calculate average sentence length
average_word_per_sentence = word_count / sentence_count


print("Paragraph Analysis")
print("-----------------------------------")
print("Approximate Word Count:",str(word_count))
print("Approximate Sentence Count:",str(sentence_count))
print("Average Letter Count:",str(character_count))
print("Average Sentence Length:",str(average_word_per_sentence))


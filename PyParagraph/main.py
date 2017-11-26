passage = "The Mirror will be moved to a new home tomorrow, Harry, and I ask you not to go looking for it again. If you ever do run across it, you will now be prepared. It does not do to dwell on dreams and forget to live, remember that. Now, why don't you put that admirable cloak back on and get off to bed."

#find approximate word count
word_count = len(passage.split())
 
 #find aproximate sentence count
sentence_count = passage.count(".")

#split up words by spaces
words = passage.split()
#count characters in each word, add together and divide by amount of all words
character_count = sum(len(word) for word in words) / len(words)

#split up sentences by periods
average_word_per_sentence = word_count / sentence_count


print("Paragraph Analysis")
print("-----------------------------------")
print("Approximate Word Count:",str(word_count))
print("Approximate Sentence Count:",str(sentence_count))
print("Average Letter Count:",str(character_count))
print("Average Sentence Count:",str(average_word_per_sentence))
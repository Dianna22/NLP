import twitter_tokenizer as tt 
from gensim.models.phrases import Phrases, Phraser
import io

x_train = tt.get_corpus().split("\n")

tokenized_train = [t.split() for t in x_train]
phrases = Phrases(tokenized_train)
bigram = Phraser(phrases)
with io.open("data/gensim_mwe.txt", "w", encoding="utf8") as f:
	for sent in x_train:
		sent = sent.split()
		f.write("%s\n" % bigram[sent])
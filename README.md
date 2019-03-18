# NLP - description of the assignments and projects in reverse chronological order
## Project
#### [Project report](https://www.overleaf.com/read/vbrhrqtwtzgp)
* [outline](https://docs.google.com/document/d/1qElk-j3W9u_FA2SbUZ4Ffjc9RLeJXBh6uTNgeCt2bJk/edit?usp=sharing)
#### Documentation
* Jupyter notebook cheatsheet:  
    * jupyter notebook --generate-config
#### [Project proposal](https://docs.google.com/document/d/1W_B9nWewimRRqxOsYwpj_8LdMqTV0jieH9v25srog-s/edit?usp=sharing)

## [Assignment 2](http://www.site.uottawa.ca/~diana/csi5386/A2_2019/A2_2019.htm)
## [Assignment 1](http://www.site.uottawa.ca/~diana/csi5386/A1_2018/A1_2018.htm)
#### [REPORT](https://docs.google.com/document/d/18pFDDHKXVCzbM22J5qirgS-TxZdazvMgooEnxDkiG50/edit?usp=sharing)
#### Documentation
#### Part 1 - Diana Lucaci
##### Files
Python files (extension _.py_) are run with Python 3.6.3: _python <file_name>.py_.
###### Code files
* twitter_tokenizer.py (a.-g.)
* mwe.py (h.)
###### Data and results files
* microblog2011_tokenized.txt - tokenized corpus
* tokens.txt - list of all tokens and their frequencies  
Aditional files:  
* data/cleaned_twitter_training_corpus.txt - corpus merged from 2 sources (SemEval task 2013 and [Kaggle dataset](https://www.kaggle.com/thoughtvector/customer-support-on-twitter#twcs.zip) of customer support twitter data) used for training the model for the multiword expression acquisition
* data/list_of_stopwords.txt
* data/list_of_contractions.txt - list of contracted words for which nltk's tokenizer splits the words, unlike the twitter tokenizer
###### External resources
Python libraries:  
* nltk - tokenizer and wordnet
* gensim.models.phrases
#### Part 2 - Mozhgan Nasr Azadani
##### Files
Java files can be added as an projects in a favourite java IDE. No external library is needed. Moreover, On mac systems, they can be run directly as ./<file_name>.java in the correct directory using terminal. 
###### Code files
* format-change.java (a.)
* accurracy.zip (b.)
* Frequency.zip (c.)
###### Data and results files
* POS_results.txt - POS tagger output for the whole corpus
###### External resources
CMU POS tagger

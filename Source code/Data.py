import numpy
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import gensim.models.keyedvectors as word2vec
from gensim.models.keyedvectors import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec
from sklearn import preprocessing

stop_words = set(stopwords.words('english'))

#Uncomment this for different pretrained models (Word2vec, fastText, GloVe)
"----------------------------------------------"
#Word2vec
model = word2vec.KeyedVectors.load_word2vec_format('/storage/GoogleNews-vectors-negative300.bin', binary=True)
#GloVe
#model = KeyedVectors.load_word2vec_format("/storage/gensim_glove_vectors.txt", binary=False)
#fastText
#model = KeyedVectors.load_word2vec_format("/storage/ilovrencic/wiki.vec",binary = False)

print("Pretrained model loaded!")
#print("+ Adding hapax_legomenom")
"----------------------------------------------"

class Data:
    def __init__(self):
        self.matrix = []
        self.truth = []
        self.tokenizer = TweetTokenizer()

    def clear(self):
        self.matrix = []
        self.truth = []

    def add_data_sample(self,sample,author):
        #Normalization



        #Stilometric features
        "----------------------------------------------------------------"
        sample = numpy.append(sample, self.hapax_legomenom_author(author))
        sample = numpy.append(sample,self.average_word_per_tweet(author))
        sample = numpy.append(sample,self.number_of_words(author))
        sample = numpy.append(sample,self.longest_word(author))
        sample = numpy.append(sample,self.average_length_of_word(author))
        sample = numpy.append(sample,self.four_letter_words(author))
        sample = numpy.append(sample,self.five_letter_words(author))
        sample = numpy.append(sample,self.six_letter_words(author))
        sample = numpy.append(sample,self.seven_letter_words(author))
        sample = numpy.append(sample,self.misspelled_words(author))
        "------------------------------------------------------------------"

        normalized_sample = preprocessing.normalize([sample])
        sample = numpy.array(normalized_sample[0])
        self.matrix.append(sample)

    def add_gender(self,sample):
        if(sample == 'F'):
            self.truth.append(0)
        else:
            self.truth.append(1)

    def add_age(self,sample):
        if(sample == "18-24"):
            self.truth.append(0)
        elif(sample == "25-34"):
            self.truth.append(1)
        elif(sample == "35-49"):
            self.truth.append(2)
        else:
            self.truth.append(3)

    def add_personality(self,sample):
        self.truth.append(sample)


    def baseline(self,authors,truth,category):
        for author in authors:
            author_id = author.attrib['id']
            author_truth = truth[author_id]
            for tweet in author:
                tokenized_tweet = self.tokenizer.tokenize(tweet.text)
                sum = numpy.zeros(300)
                for word in tokenized_tweet:
                    if(word in model.vocab and word not in stop_words):
                        sum += model[word]

                self.add_data_sample(sum,author)
                if(category == "gender"):
                    self.add_gender(author_truth)
                elif(category == "age"):
                    self.add_age(author_truth)
                else:
                    self.add_personality(author_truth)


    #author version
    def hapax_legomenom_author(self,author):
        list_of_words = []
        for tweet in author:
            tokenized_tweet = self.tokenizer.tokenize(tweet.text)
            list_of_words = list_of_words+tokenized_tweet
        return len(set(list_of_words))

    def average_word_per_tweet(self,author):
        list_of_words = []
        number_of_tweets = 0
        for tweet in author:
            tokenized_tweet = self.tokenizer.tokenize(tweet.text)
            list_of_words = list_of_words+tokenized_tweet
            number_of_tweets += 1
        return (len(list_of_words)/number_of_tweets)

    def number_of_words(self,author):
        list_of_words = []
        for tweet in author:
            tokenized_tweet = self.tokenizer.tokenize(tweet.text)
            list_of_words = list_of_words+tokenized_tweet

        return len(list_of_words)

    def longest_word(self,author):
        list_of_words = []
        for tweet in author:
            tokenized_tweet = self.tokenizer.tokenize(tweet.text)
            list_of_words = list_of_words+tokenized_tweet

        max = 0
        for word in list_of_words:
            if( len(word) > max ):
                max = len(word)
        return max

    def average_length_of_word(self,author):
        list_of_words = []
        for tweet in author:
            tokenized_tweet = self.tokenizer.tokenize(tweet.text)
            list_of_words = list_of_words+tokenized_tweet

        len_sum = 0
        for word in list_of_words:
            len_sum += len(word)

        return len_sum/len(list_of_words)

    def four_letter_words(self,author):
        list_of_words = []
        for tweet in author:
            tokenized_tweet = self.tokenizer.tokenize(tweet.text)
            list_of_words = list_of_words+tokenized_tweet

        less_then_four_letter_words = 0
        for word in list_of_words:
            if(len(word) < 4):
                less_then_four_letter_words += 1

        return less_then_four_letter_words/len(list_of_words)

    def five_letter_words(self,author):
        list_of_words = []
        for tweet in author:
            tokenized_tweet = self.tokenizer.tokenize(tweet.text)
            list_of_words = list_of_words+tokenized_tweet

        less_then_five_letter_words = 0
        for word in list_of_words:
            if(len(word) > 5):
                less_then_five_letter_words += 1

        return less_then_five_letter_words/len(list_of_words)

    def six_letter_words(self,author):
        list_of_words = []
        for tweet in author:
            tokenized_tweet = self.tokenizer.tokenize(tweet.text)
            list_of_words = list_of_words+tokenized_tweet

        less_then_six_letter_words = 0
        for word in list_of_words:
            if(len(word) > 6):
                less_then_six_letter_words += 1

        return less_then_six_letter_words/len(list_of_words)

    def seven_letter_words(self,author):
        list_of_words = []
        for tweet in author:
            tokenized_tweet = self.tokenizer.tokenize(tweet.text)
            list_of_words = list_of_words+tokenized_tweet

        less_then_seven_letter_words = 0
        for word in list_of_words:
            if(len(word) > 7):
                less_then_seven_letter_words += 1

        return less_then_seven_letter_words/len(list_of_words)

    def misspelled_words(self,author):
        list_of_words = []
        for tweet in author:
            tokenized_tweet = self.tokenizer.tokenize(tweet.text)
            list_of_words = list_of_words+tokenized_tweet

        number_of_misspelled_words = 0
        for word in list_of_words:
            if( word not in model.vocab):
                number_of_misspelled_words += 1

        return number_of_misspelled_words/len(list_of_words)


from Parser import Parser
from Truth import Truth
from Data import Data
from Model import Model
import numpy
#GloVe preloading (not neccessary anymore)
#glove2word2vec(glove_input_file="glove.txt", word2vec_output_file="glove_vectors.txt")

#Change this path to training/test files
"----------------------------------------------"
training_corpus = "/home/lovren97/ZR/Datasets/Training/english/pan/"
validation_corpus = "/home/lovren97/ZR/Datasets/Test/en/"
training_truth = "/home/lovren97/ZR/Datasets/Training/english/truth.txt"
test_truth = "/home/lovren97/ZR/Datasets/Test/en.txt"
test_corpus="/home/lovren97/ZR/Datasets/Validation/en/"
"----------------------------------------------"

#Parsing  training corpus
"----------------------------"
parser = Parser(training_corpus)
authors_training = parser.data
"----------------------------"

#Parsing validation corpus
"----------------------------"
parser.change_path(validation_corpus)
authors_validation = parser.data
"-----------------------------"

#Parsing test corpus
"-----------------------------"
parser.change_path(validation_corpus)
authors_test = parser.data
"-----------------------------"

#Parsing training truth
"-----------------------------"
training_file = open(training_truth,"r")
training_truths = []
for line in training_file:
    training_truths.append(line[:-1])

train_truth = Truth(training_truths)
"-----------------------------"

#Parsing test truth
"-----------------------------"
test_file = open(test_truth,"r")
test_truths = []
for line in test_file:
    test_truths.append(line[:-1])

test_truth = Truth(test_truths)
"-----------------------------"

#Creating data class for easy access to dataZa kvalitetnije vrednovanje modela potrebno je skupove podataka podijeliti na tri dijela u čestom omjeru od 40 (trening skup) : 30 (skup za provjeru) : 30 (skup za testiranje). Pošto preuzeti skupovi podataka nemaju skup za provjeru (eng. \textit{validation dataset}).
"-------------------------------"
training_data = Data()
validation_data = Data()
test_data = Data()
"-------------------------------"

#Creating model class for easy access to different machine learning models
"--------------------------------"
ml_model = Model()
"--------------------------------"

print("Starting...")

#Model for Gender
"---------------------------------"
#training_data.baseline(authors_training,train_truth.gender,"gender")
#test_data.baseline(authors_test,test_truth.gender,"gender")

#ml_model.svm(training_data,test_data,0.25)
#ml_model.logistic(training_data,test_data,0.5)
"----------------------------------"

#Model for Age
"----------------------------------"
#training_data.baseline(authors_training,train_truth.age,"age")
#test_data.baseline(authors_test,test_truth.age,"age")

#ml_model.svm(training_data,test_data, 4)
#ml_model.logistic_multi(training_data,test_data,1)
"-----------------------------------"

#Models for Personality
"----------------------------------"
#training_data.baseline(authors_training,train_truth.extrovertness,"personality")
#test_data.baseline(authors_test,test_truth.extrovertness,"personality")

#print("Personality trait extrovertness:")
#ml_model.svr(training_data,test_data,16)

training_data.baseline(authors_training,train_truth.stable,"personality")
test_data.baseline(authors_test,test_truth.stable,"personality")

print("Personality trait stable:")
ml_model.svr(training_data,test_data,8)

training_data.baseline(authors_training,train_truth.agreeable,"personality")
test_data.baseline(authors_test,test_truth.agreeable,"personality")

print("Personality trait agreeable:")
ml_model.svr(training_data,test_data,2)

training_data.baseline(authors_training,train_truth.consicentious,"personality")
test_data.baseline(authors_test,test_truth.consicentious,"personality")

print("Personality trait consicentious:")
ml_model.svr(training_data,test_data,8)

training_data.baseline(authors_training,train_truth.open,"personality")
test_data.baseline(authors_test,test_truth.open,"personality")

print("Personality trait open:")
ml_model.svr(training_data,test_data,4)
"-----------------------------------"



print("Finish!")

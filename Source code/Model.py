from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.svm import SVR
from sklearn.metrics import confusion_matrix
import numpy
import operator

class Model:
    def __init__(self):
        self.file = ""
        self.c_dict = dict()


    def svm(self,training,test,coef):
        h = SVC(kernel = 'linear',C = coef)
        h.fit(training.matrix,training.truth)
        print("SVM baseline:",h.score(test.matrix,test.truth))
        print("Confusion matrix:",confusion_matrix(test.truth,h.predict(test.matrix),labels=[0,1,2,3]))


    def grid_search_svm(self,training,test):
        for x in range(-5,5):
            coef = 2**x
            h = SVC(kernel = 'linear',C = coef)
            h.fit(training.matrix,training.truth)
            print("C = ",coef)
            print("SVM baseline:",h.score(test.matrix,test.truth))

    def grid_search_logistic(self,training,test):
        for x in range(-5,5):
            coef = 2**x
            h = LogisticRegression(C = coef)
            h.fit(training.matrix,training.truth)
            print("C = ",coef)
            print("LogisticRegresion baseline:",h.score(test.matrix,test.truth))

    def grid_search_logistic_multi(self,training,test):
        for x in range(-5,5):
            coef = 2**x
            h = LogisticRegression(C = coef,multi_class="multinomial",solver="lbfgs",max_iter=2000)
            h.fit(training.matrix,training.truth)
            print("C = ",coef)
            print("LogisticRegresion baseline:",h.score(test.matrix,test.truth))

    def grid_search_svr(self,training,test):
        self.c_dict = dict()
        for x in range(-5,5):
            coef = 2**x
            #print("C = ",coef)
            accuracy = self.svr(training,test,coef)
            self.c_dict[coef] = accuracy

        sorted_dict = sorted(self.c_dict.items(),key= operator.itemgetter(1))
        print(sorted_dict)

        training.clear()
        test.clear()


    def logistic(self,training,test,coef):
        h = LogisticRegression(C = coef)
        h.fit(training.matrix,training.truth)
        print("LogisticRegresion baseline:",h.score(test.matrix,test.truth))
        print("Confusion matrix:",confusion_matrix(test.truth,h.predict(test.matrix)))




    def logistic_multi(self,training,test,coef):
        h = LogisticRegression(multi_class="multinomial",solver="lbfgs",max_iter=1000, C = coef)
        h.fit(training.matrix,training.truth)
        print("LogisticRegresionMulti baseline:",h.score(test.matrix,test.truth))
        print("Confusion matrix:",confusion_matrix(test.truth,h.predict(test.matrix),labels=[0,1,2,3]))




    def svr(self,training,test,coef):
        #self.file = open("results.txt","a")

        h = SVR(kernel='linear',C = coef)
        h.fit(training.matrix,training.truth)

        predicted = h.predict(test.matrix)

        for i in range(len(predicted)):
            predicted[i] = round(predicted[i],1)
            if(predicted[i] == 0.):
                predicted[i] = 0.0

        score = 0
        for i in range(len(predicted)):
            if(float(predicted[i]) == float(test.truth[i])):
                score += 1

        print("SVR baseline:",score/len(predicted))
        #return score/len(predicted)
        #self.file.write(str(coef)+ "\n")
        #self.file.write(str(score/len(predicted))+ "\n")

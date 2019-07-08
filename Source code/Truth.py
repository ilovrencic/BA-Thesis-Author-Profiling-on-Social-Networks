# 1 - GENDER , 2 - AGE , 3 - extrovertness , 4 - STABLE , 5 - agreeable , 6 - consicentious , 7 - open

class Truth:
    def __init__(self,truths):
        self.truths = truths
        self.parse_truth()

        self.gender = self.getTruthDict(1)
        self.age = self.getTruthDict(2)
        self.extrovertness = self.getTruthDict(3)
        self.stable = self.getTruthDict(4)
        self.agreeable = self.getTruthDict(5)
        self.consicentious = self.getTruthDict(6)
        self.open = self.getTruthDict(7)

        self.baseline_age = dict()
        self.baseline_gender = dict()
        self.average_personality = dict()



    def parse_truth(self):
        for i in range(len(self.truths)):
            truths = self.truths[i].split(":::")
            self.truths[i] = truths

    def getTruthDict(self,i):
        truthDict = dict()

        for truth in self.truths:
            truthDict[truth[0]] = truth[i]

        return truthDict

    def base_age(self):
        self.baseline_age = dict()
        self.baseline_age['25-34'] = 0
        self.baseline_age['18-24'] = 0
        self.baseline_age['35-49'] = 0
        self.baseline_age['50-XX'] = 0
        for truth in self.truths:
            self.baseline_age[truth[2]] += 1
        print(self.baseline_age)

    def base_gender(self):
        self.baseline_gender = dict()
        self.baseline_gender['M'] = 0
        self.baseline_gender['F'] = 0
        for truth in self.truths:
            self.baseline_gender[truth[1]] += 1
        print(self.baseline_gender)

    def average_over_traits(self):
        self.average_personality = dict()
        self.average_personality[3] = 0
        self.average_personality[4] = 0
        self.average_personality[5] = 0
        self.average_personality[6] = 0
        self.average_personality[7] = 0

        for i in range(3,8):
            temp_dict = self.getTruthDict(i)
            suma = 0
            for value in temp_dict.values():
                suma += float(value)
            self.average_personality[i] = float(suma)/len(temp_dict.values())
        print(self.average_personality)

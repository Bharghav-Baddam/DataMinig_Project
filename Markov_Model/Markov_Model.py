from __future__ import print_function
import numpy as np
import types
import itertools
import copy
import json
import datetime

def get_key(dictionary, val): 
    for key, value in dictionary.items(): 
         if val == value: 
             return key 
    return ""

def get_all_sequences(m, n):
    i = 1
    S = []
    for j in range(n):
        S.append([j])
    while i < m:
        S1 = []
        for s in S:
            for j in range(n):
                s1 = copy.deepcopy(s)
                s1.append(j)
                S1.append(s1)
        S.extend(S1)
        i = i + 1
    S = [item for item in S if len(item) == m]
    return S


class markovmodel:
    #transmat: None
    def __init__(self, transmat = None, startprob = None):
        self.transmat = transmat
        self.startprob = startprob
    # It assumes the state number starts from 0
    def fit(self, X):
        ns = max([max(items) for items in X]) + 1
        self.transmat  = np.zeros([ns, ns])
        self.startprob = np.zeros([ns])
        for items in X:
            n = len(items)
            self.startprob[items[0]] += 1
            for i in range(n-1):
                self.transmat[items[i], items[i+1]] += 1
        self.startprob = self.startprob / sum(self.startprob)
        n = self.transmat.shape[0]
        d = np.sum(self.transmat, axis=1)
        for i in range(n):
            if d[i] == 0:
                self.transmat[i,:] = 1.0 / n
        d[d == 0] = 1
        self.transmat = self.transmat * np.transpose(np.outer(np.ones([ns,1]), 1./d))

    def predict(self, obs, steps):
        if len(obs) > 0:
            combs = get_all_sequences(steps, len(self.startprob))
            max_seq = []
            max_prob = -1
            for comb in combs:
                prob = 1.0
                prev = obs[-1]
                for i in comb:
                    prob = prob * self.transmat[prev, i]
                    prev = i
                if prob > max_prob:
                    max_seq = comb
                    max_prob = prob
            return max_seq
        else:
            combs = get_all_sequences(steps, len(self.startprob))
            max_seq = []
            max_prob = -1
            for comb in combs:
                prob = 1.0
                prev = -1
                for i in comb:
                    if prev == -1:
                        prob = prob * self.startprob[i]
                    else:
                        prob = prob * self.transmat[prev, i]
                    prev = i
                if prob > max_prob:
                    max_seq = comb
                    max_prob = prob
            return max_seq
raw_data = []

team_name = raw_input("Enter team name: ")
qtr = raw_input("Enter QTR (1-5): ")
win_lose = raw_input("Enter scenario (Winning/Losing/Tied): ")

print("Checking for when " + team_name + " is playing in Quarter " + qtr + " and is " + win_lose)
with open('../Teams/{}/{}/{}/data.json'.format(team_name, str(qtr), win_lose), 'r') as f:
    raw_data = json.load(f)
counter = int(raw_input("Enter number of consecutive plays to train model: "))
orig = int(counter)
count = 0
y = []
temp = []
receiver_number = 0
indices = dict()
for play in raw_data:
    term = play['Receiver_Name']
    if(indices.has_key(term) == False):
        indices.update({term:receiver_number})
        receiver_number = receiver_number + 1
    temp.append(indices.get(term))
    count = count+1
    if(count == orig):
        count = 0
        y.append(temp)
        temp = []

sorted_view = [ (v,k) for k,v in indices.iteritems() ]
sorted_view.sort(reverse=False)

for key,value in sorted_view:
    print(str(key) + " => " + str(value))

# train a markov model
mm = markovmodel()
mm.fit(y)
x = []

seq = raw_input("Input a sequence seperated by commas of the player ids (ex: 0,1,2,3)): ")
seq = ''.join(str(seq)).replace('(','').replace(')','')
seq = seq.split(',')
sequence = []
for i in seq:
    sequence.append(int(i))

print(sequence)
num_forward = int(raw_input("Input number of future plays to predict: "))
print('Analyzing ' + str(num_forward) + ' play(s) into the future')
pred = mm.predict(sequence, num_forward)
print("Prediction: ")
for p in pred:
    name = get_key(indices, p)
    if name == 'NA':
        name = 'Run Play'
    print(name, end='  ')
print('\n')

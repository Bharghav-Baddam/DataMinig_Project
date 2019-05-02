from __future__ import print_function
import numpy as np
from hmmlearn import hmm
import types
import json

def get_key(dictionary, val): 
    for key, value in dictionary.items(): 
         if val == value: 
             return key 
    return ""

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
        pred = []
        if len(obs) > 0:
            s = obs[-1]
        else:
            s = np.argmax(np.random.multinomial(1, self.startprob.tolist(), size = 1))
        for i in range(steps):
            s1 = np.random.multinomial(1, self.transmat[s,:].tolist(), size = 1)
            pred.append(np.argmax(s1))
            s = np.argmax(s1)
        return pred

def hmm_predict_further_states(ghmm, obs, steps):
    y = ghmm.predict(obs)
    mm = markovmodel(ghmm.transmat_, ghmm.startprob_)
    return mm.predict([y[-1]], steps)

def hmm_predict_future_features(ghmm, obs, steps):
    y = ghmm.predict(obs)
    pred = []
    mm = markovmodel(ghmm.transmat_, ghmm.startprob_)
    sts = mm.predict([], steps)
    for s in sts:
        mean = ghmm.means_[y[-1]]
        cov = ghmm.covars_[y[-1],:]
        x = np.random.multivariate_normal(mean,cov,1)
        pred.append(x[0].tolist())
    return pred

# X: sequence of observations
# y: sequence of latent states
def estimate_parameters(X, y):
    mm = markovmodel()
    mm.fit(y)
    data = dict()
    for i in range(len(y)):
        for s, x in zip(y[i], X[i]):
            if data.has_key(s):
                data[s].append(x)
            else:
                data[s] = [x]
    ns = len(data.keys())
    means = np.array([[np.mean(data[s])] for s in range(ns)])
    covars = np.tile(np.identity(1), (ns, 1, 1))
    for s in range(ns):
        covars[s, 0] = np.std(data[s])
    return mm.startprob, mm.transmat, means, covars

raw_data = []

team_name = raw_input("Enter team name: ")
qtr = raw_input("Enter QTR (1-5): ")
win_lose = raw_input("Enter scenario (Winning/Losing/Tied): ")

print("Checking for when " + team_name + " is playing in Quarter " + qtr + " and is " + win_lose)
print("This will also cross check against the yards away from scoring (our X in hidden markov model)")
with open('../Teams/{}/{}/{}/data.json'.format(team_name, str(qtr), win_lose), 'r') as f:
    raw_data = json.load(f)
counter = int(raw_input("Enter number of consecutive plays to train model: "))
orig = int(counter)
count = 0
y = []
X = []
temp_y = []
temp_x = []
receiver_number = 0
indices = dict()
for play in raw_data:
    term = play['Receiver_Name']
    if(indices.has_key(term) == False):
        indices.update({term:receiver_number})
        receiver_number = receiver_number + 1
    temp_y.append(indices.get(term))
    temp_x.append(int(play['Yards_Gained']))
    count = count+1
    if(count == orig):
        count = 0
        y.append(temp_y)
        X.append(temp_x)
        temp_y = []
        temp_x = []

sorted_view = [ (v,k) for k,v in indices.iteritems() ]
sorted_view.sort(reverse=False)

for key,value in sorted_view:
    print(str(key) + " => " + str(value))

seq = raw_input("Input a sequence of yards from previous plays (ex: 10,-1,2,7)): ")
seq = ''.join(str(seq)).replace('(','').replace(')','')
seq = seq.split(',')
sequence = []
for i in seq:
    sequence.append(int(i))

final_testing = []
for t in sequence:
    a = []
    a.append(t)
    final_testing.append(a)
num_forward = int(raw_input("Input number of future plays to predict: "))
print('Analyzing ' + str(num_forward) + ' play(s) into the future')
print(final_testing)

startprob, transmat, means, covars = estimate_parameters(X, y)
model = hmm.GaussianHMM(receiver_number, "full")
model.startprob_ = startprob
model.transmat_ = transmat
model.means_  = means

new_covars = []
for c in covars:
    outermost = []
    for i in c:
        outer = []
        for j in i:
            if j == 0:
                outer.append(0.00001) # HMM hates zeros. Replace them with a minimal value
            else:
                outer.append(j)
        outermost.append(outer)
    new_covars.append(outermost)

model.covars_ = new_covars


test = hmm_predict_further_states(model, final_testing, num_forward)
print("Prediction: ")
for p in test:
    name = get_key(indices, p)
    if name == 'NA':
        name = 'Run Play'
    print(name, end='  ')
print('\n')
cons = hmm_predict_future_features(model, final_testing, num_forward)
print([round(con[0], 2) for con in cons])
print("\n")
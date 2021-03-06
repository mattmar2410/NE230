import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy.stats import poisson
from sklearn.metrics import roc_curve, auc
plt.ylabel('Probability')
plt.xlabel('Number of Counts')
plt.title('Probability Distribution Curve - Poisson')
positive = []; FPR = []; false_positive_rate = []
TPR = []; true_positive_rate = []
rv = poisson(25)
for num in range(1,50):
    positive.append(rv.pmf(num))
plt.grid(True)
plt.plot(positive, 'bo', label = 'Positive')

negative = []
mu = poisson(15)
for num in range(1,50):
    negative.append(mu.pmf(num))

plt.grid(True)
plt.plot(negative, 'ks', label='Negative')
plt.legend()
plt.show()

for trigger in range(len(negative)):
    i = trigger
    while i < (len(negative)-trigger):
        FPR.append(negative[i]) #sum to the right of the negative values (1 - TPR)
        i += 1
    false_positive_rate.append(sum(FPR))
    FPR = []
for trigger in range(len(positive)):
    i = 0
    while i < trigger:
        TPR.append(positive[i]) #sum to the right of the negative values (1 - TPR)
        i += 1
    true_positive_rate.append(1-sum(TPR))
    TPR = []  #sum to the right of the negative values (1 - TPR)

#TPR = #sum to the left of the positive values (1 - TPR)
plt.figure(2)
plt.title('Receiver Operating Characteristic - Poisson')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.plot(false_positive_rate,true_positive_rate, 'ko')
plt.show()
for i in range(len(false_positive_rate)):
    try:
        vert_1 = np.linspace(false_positive_rate[i], false_positive_rate[i], 100)
        vert_2 = np.linspace(true_positive_rate[i], true_positive_rate[i+1], 100)
        horz_1 = np.linspace(true_positive_rate[i+1], true_positive_rate[i+1], 100)
        horz_2 = np.linspace(false_positive_rate[i], false_positive_rate[i+1], 100)
        plt.plot(vert_1, vert_2, 'b')
        plt.plot(horz_2, horz_1, 'b')
    except IndexError:
        pass
plt.title('Receiver Operating Characteristic - Poisson')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
x = auc(false_positive_rate, true_positive_rate)
red_patch = mpatches.Patch(color='blue', label='ROC curve (area = %0.2f)' % x)
plt.legend(handles=[red_patch],loc="lower right")
plt.show()

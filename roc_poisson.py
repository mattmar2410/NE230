import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy.stats import poisson
from sklearn.metrics import roc_curve, auc
def poisson_roc(x,y):
    positive = []; FPR = []; false_positive_rate = []
    TPR = []; true_positive_rate = []
    rv = poisson(x)
    for num in range(1,50):
        positive.append(rv.pmf(num))

    negative = []
    mu = poisson(y)
    for num in range(1,50):
        negative.append(mu.pmf(num))

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
    return false_positive_rate, true_positive_rate

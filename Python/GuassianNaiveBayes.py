import pandas as pd
import numpy as np
import math 

def calculate_class(X_train):
    class0 = pd.DataFrame(columns=X_train.columns)
    class1 = pd.DataFrame(columns=X_train.columns)
    
    for i in range(X_train.shape[0]):
        if y_train[i] == 0:
            class0.loc[i] = X_train.iloc[i,0:X_train.shape[1]]
        else:
            class1.loc[i] = X_train.iloc[i,0:X_train.shape[1]]
    
    return class0,class1

def calculate_mean_var(class0,class1):
    mean_0 = class0.mean(axis = 0) 
    mean_1 = class1.mean(axis = 0)
    
    var_0 = class0.var(axis = 0)
    var_1 = class1.var(axis = 0)
    
    return mean_0,mean_1,var_0,var_1

def calculate_prior(class0,class1,size):
    prior = []
    prior.append(class0.shape[0] / size)
    prior.append(class1.shape[0] / size)
    
    return prior

def prob_feature_class(x, mean_0, mean_1, var_0, var_1):
    pfc = []
    
    product = 1
    for j in range(mean_0.shape[0]):
        product = product * (1/math.sqrt(2*3.14*var_0[j])) * math.exp(-0.5
                            * pow((x[j] - mean_0[j]),2)/var_0[j])
    pfc.append(product)
    
    product = 1
    for j in range(mean_0.shape[0]):
        product = product * (1/math.sqrt(2*3.14*var_1[j])) * math.exp(-0.5
                            * pow((x[j] - mean_1[j]),2)/var_1[j])
    pfc.append(product)
    return pfc

def GNB(X_train, X_test):
    class0, class1 = calculate_class(X_train)
    mean0, mean1, var0, var1 = calculate_mean_var(class0,class1)
    pre_probab = calculate_prior(class0,class1,X_train.shape[0])
    y_pred = []
    for j in range(X_test.shape[0]): 
        pfc = prob_feature_class(X_test.iloc[j,0:X_test.shape[1]], mean0, mean1, var0, var1)
        pcf = np.ones(2)
        for i in range(0, 2):
            pcf[i] = pfc[i] * pre_probab[i]
        prediction = int(pcf.argmax())
        y_pred.append(prediction)
    return y_pred


xl = pd.ExcelFile("parktraining.xlsx")
train = xl.parse("Sheet1", header=None)

X_train = train.iloc[:,0:22]
y_train = train.iloc[:,-1]

xl = pd.ExcelFile("parktesting.xlsx")
test = xl.parse("Sheet1", header=None)
X_test = test.iloc[:,0:22]
y_test = test.iloc[:,-1]

y_pred = GNB(X_train,X_test)

TP=len([i for i in range(0,y_test.shape[0]) if y_test[i]==1 and y_pred[i]==1])
TN=len([i for i in range(0,y_test.shape[0]) if y_test[i]==0 and y_pred[i]==0])
FP=len([i for i in range(0,y_test.shape[0]) if y_test[i]==1 and y_pred[i]==0])
FN=len([i for i in range(0,y_test.shape[0]) if y_test[i]==0 and y_pred[i]==1])
confusion_matrix=np.array([[TP,TN],[FP,FN]])
print(confusion_matrix)
print("Accuracy")
print((TP + TN)/(TP + TN + FP + FN))

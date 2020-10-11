
def backwardElimination(x,y, sl,con=True):# con implies if the constent matrix is added ao not
    import matplotlib.pyplot as plt
    import numpy as np
    import statsmodels.regression.linear_model as lmd
    if con==False:
        x = np.append(arr=np.ones((len(x), 1)).astype(int), values=x, axis=1)

    numVars = len(x[0])
    r_sq=0
    for i in range(0, numVars):
        regressor_OLS = lmd.OLS(endog=y, exog=x).fit()
        if regressor_OLS.rsquared_adj>r_sq:# To see the Complete graph replace r_sq by 0
            r_sq=regressor_OLS.rsquared_adj
            maxVar = max(regressor_OLS.pvalues).astype(float)
            if maxVar > sl:
                for j in range(0, numVars - i):
                    if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                        x = np.delete(x, j, 1)
            print(regressor_OLS.rsquared_adj)
            plt.scatter(i,regressor_OLS.rsquared_adj)
            plt.draw()
            plt.pause(0.2)
    plt.show()
    print(regressor_OLS.summary())
    return x

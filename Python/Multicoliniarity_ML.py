
def VIF(X_df,sl=5,con=True):

    from statsmodels.stats.outliers_influence import variance_inflation_factor as vir
    import pandas as pd
    import numpy as np
    if sl>1:
        if con==False:
            X_df.insert(0,'Constent',1,False)
        vif = pd.DataFrame()
        print("Data input SIZE:",len(X_df.columns))
        for i in range(X_df.shape[1]-1):
            head=X_df.columns
            list=[vir(X_df.values, j) for j in range(X_df.shape[1])]
            if max(list)>sl:# 5
                X_df=X_df.drop(columns=[head[list.index(max(list))]],axis=1)


        vif["VIF Factor"] = list
        vif["features"] = X_df.columns
        print(vif)
        print(np.shape(vif))
        return X_df
    else:
        print('Value of SL should be grater than 1')

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
#----------------------------------------------------------

def Overall_Qual(x):
    if x == '1' or x=='2' or x=='3':
        return 'Low'
    elif x == '4' or x=='5' or x=='6' or x=='7':
        return 'Medium'  
    elif x =='8' or x=='9' or x=='10':
        return 'High' 
    else:
        return np.nan 
#----------------------------------------------------------
def Bsmt_Qual(x):
    if x == 'Po' or x=='Fa' or x=='TA':
        return 'Low'
    elif x == 'Gd':
        return 'Medium'  
    elif x =='Ex':
        return 'High' 
    else:
        return np.nan 
#----------------------------------------------------------
def Foundation(x):
    if x == 'PConc':
        return 'PConc'
    else:
        return 'Others'
#----------------------------------------------------------
def Bldg_Type(x):
    if x == '1Fam' or x =='TwnhsE':
        return '1Fam_TwnhsE'
    else:
        return 'Others' 
#----------------------------------------------------------
def BsmtFin_Type_1(x):
    if x == 'GLQ':
        return 'GLQ'
    else:
        return 'Others' 
#----------------------------------------------------------
def Bsmt_Cond(x):
    if x == 'Po' or x=='Fa' or x=='TA':
        return 'Low'
    elif x == 'Gd' or x=='Ex':
        return 'High'  
    else:
        return np.nan 
#----------------------------------------------------------
def Full_Bath(x):
    x=int(x)
    if x <= 1:
        return 'one_or_less'
    elif  x>=2:
        return 'two_or_more'
    else:
        return np.nan 
#----------------------------------------------------------
def Condition_2(x):
    if x == 'PosA' or x=='PosN':
        return 'Pos'
    elif x == 'Norm':
        return 'Norm' 
    elif x=='RRNn' or x=='Feedr' or x=='Artery' or x=='RRAe' or x=='RRAn':
        return 'Others'  
    else:
        return np.nan
#----------------------------------------------------------
def Condition_1(x):
    if x == 'PosA' or x=='PosN':
        return 'Pos'
    elif x == 'Norm':
        return 'Norm' 
    elif x=='RRAe' or x=='RRAn' or x=='RRNe' or x=='RRNn':
        return 'RR'  
    elif x=='Artery' or x=='Feedr':
        return 'Others'  
    else:
        return np.nan 
#----------------------------------------------------------
def Exter_Cond(x):
    if x == 'Po' or x=='Fa':
        return 'Low'
    elif  x=='TA' or x=='Gd' or x=='Ex':
        return 'Good'
    else:
        return np.nan 
#----------------------------------------------------------
def Fireplaces(x):
    x=int(x)
    if x < 1:
        return 'No'
    elif  x>=1:
        return 'Yes'
    else:
        return np.nan         
#----------------------------------------------------------
def Garage_Cars(x):
    if x!='nan':
        if x == '0.0' or x=='1.0':
            return 'one_or_less'
        elif  x == '2.0':
            return 'two'
        elif x=='3.0' or x == '4.0' or x=='5.0':
            return 'three_or_more'
        else:
            return np.nan 
    else:
        return np.nan 
#----------------------------------------------------------
def Garage_Type(x):
    if x == 'Detchd' or x=='Basment' or x=='2Types' or x=='CarPort':
        return 'others'
    elif  x=='Attchd' or x=='BuiltIn':
        return 'Attchd_BuiltIn'
    else:
        return np.nan 
#----------------------------------------------------------
def Overall_Cond(x):
    x=int(x)
    if x==1 or x==2 or x==3 or x==4:
        return '1234'
    elif  x==5 or x==9:
        return '59'
    elif  x==6 or x==7 or x==8:
        return '678'    
    else:
        return np.nan 
#----------------------------------------------------------
def Sale_Type(x):
    if x == 'New':
        return 'New'
    elif x == 'WD ':
        return 'WD'
    elif  x=='COD' or x=='VWD' or x=='CWD' or x=='ConLD' or x=='ConLI' or x=='Oth' or x=='ConLw' or x == 'Con':
        return 'others'
    else:
        return np.nan 
#----------------------------------------------------------
def TotRms_AbvGrd(x):
    x=int(x)
    if x==2:
        return 'less_than_3'
    elif x==3 or x==4 or x==5 or x==6:
        return '3_to_6'
    elif  x==7 or x==8:
        return '7_to_8'  
    elif x>=9:
        return '9_or_more'
    else:
        return np.nan 
#----------------------------------------------------------
def lr_fix(df_tr, var_feat, lot_area):
    lr_1 = LinearRegression()
    
    area = df_tr.dropna(subset=[var_feat])[lot_area].to_frame().to_numpy()
    frontage = df_tr.dropna(subset=[var_feat])[var_feat].to_frame()
    
    lr_1.fit(area, frontage)
    coeff = lr_1.coef_[0][0]
    intercept = lr_1.intercept_[0]
    return(intercept, coeff)  
#----------------------------------------------------------
def train_test_align(df_train1, df_test1, column, prefix):
    df_train1 = pd.get_dummies(df_train1, columns = [column], drop_first = True , prefix=prefix)
    df_test1 = pd.get_dummies(df_test1, columns = [column], drop_first = True , prefix=prefix)
    
    df_train1, df_test1 = df_train1.align(df_test1, join='outer', axis=1)
    
    if df_train1.filter(regex='^%s' %prefix, axis=1).isnull().sum().sum()!=0:
        columns_with_nan = df_train1.filter(regex='^%s' %prefix, axis=1).columns[df_train1.filter(\
                                            regex='^%s' %prefix, axis=1).isna().any()].tolist()
        for item in columns_with_nan:
            df_train1[item].fillna(0, inplace=True)
        
    
    if df_test1.filter(regex='^%s' %prefix, axis=1).isnull().sum().sum()!=0:
        columns_with_nan = df_test1.filter(regex='^%s' %prefix, axis=1).columns[df_test1.filter(\
                                           regex='^%s' %prefix, axis=1).isna().any()].tolist()
        for item in columns_with_nan:
            df_test1[item].fillna(0, inplace=True)  
    
    
    return(df_train1, df_test1) 
#----------------------------------------------------------




        


















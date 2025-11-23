import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler


def load_and_preprocess_data(DATAPATH):
    df = pd.read_csv(DATAPATH)

    X =  df.drop('SalePrice' , axis = 1)
    y = df['SalePrice']

    #splitting the data
    X_train , X_test , y_train , y_test = train_test_split(X , y , test_size=0.2 , random_state= 42) 



    #scaling the data
    scalar = StandardScaler()
    X_train_scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.transform(X_test) 

    return X_train_scaled, X_test_scaled, y_train, y_test, scalar

from src.data_preprocessing import load_and_preprocess_data
from src.model import build_model



DATAPATH = "house_prices.csv"

#loading data
X_train ,X_test, y_train, y_test ,scalar = load_and_preprocess_data(DATAPATH)

#train model 
model = build_model()
model.fit(X_train , y_train)
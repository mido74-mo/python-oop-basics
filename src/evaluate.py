from sklearn.metrics import mean_squared_error,r2_score
from src.visualization import plot_predictions, plot_residuals
import numpy as np


def evaluate_model(model , X_train, X_test, y_train, y_test):
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test , y_pred)
    rmse = np.sqrt(mse)
    train_score= model.score(X_train , y_train)
    test_score = model.score(X_test , y_test)
    r2 = r2_score(y_test,y_pred)

    # call visualization
    plot_predictions(y_test, y_pred)

    metrics = {
        "MSE": mse,
        "RMSE" : rmse,
        "train_score": train_score,
        "test_score": test_score,
        "r2_score" : r2
    }
    return metrics, y_pred

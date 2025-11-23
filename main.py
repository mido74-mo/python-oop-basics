from src.data_preprocessing import load_and_preprocess_data
from src.model import build_model
from src.evaluate import evaluate_model
from src.visualization import plot_predictions, plot_residuals

DATAPATH = "house_prices.csv"


def main():

    #1- load the data
    X_train , X_test , y_train , y_test ,scalar = load_and_preprocess_data(DATAPATH)


    #2- build model 
    model = build_model()

    #3- train model
    model.fit(X_train,y_train)

    #4-evaluate 
    metrics ,y_pred = evaluate_model(model, X_train,X_test, y_train,y_test)

    print("📊 Evaluation Metrics:")
    for key , value in metrics.items():
        print(f"{key}: {value:.4f}")

    #visualization
    # plot_predictions(y_pred,y_test)
    # plot_residuals(y_test,y_pred)


if __name__ == "__main__":
    main()

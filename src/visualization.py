import matplotlib.pyplot as plt
import seaborn as sns

def plot_predictions(y_test, y_pred):
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    # Flatten arrays if they are 2D
    y_test = y_test.ravel()
    y_pred = y_pred.ravel()
    
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=y_test, y=y_pred, alpha=0.6)
    plt.xlabel("Actual Prices")
    plt.ylabel("Predicted Prices")
    plt.title("Actual vs Predicted Prices")
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color="red", linestyle="--")
    plt.show()



def plot_residuals(y_test, y_pred):
    """Plot residuals to check errors distribution."""
    residuals = y_test - y_pred
    plt.figure(figsize=(8,6))
    sns.histplot(residuals, kde=True)
    plt.xlabel("Residuals")
    plt.title("Residuals Distribution")
    plt.show()


def plot_learning_curves(train_scores, test_scores):
    """Optional: Plot learning curves if you log scores during training."""
    plt.figure(figsize=(8,6))
    plt.plot(train_scores, label="Train Score")
    plt.plot(test_scores, label="Test Score")
    plt.xlabel("Epochs / Iterations")
    plt.ylabel("Score")
    plt.title("Learning Curves")
    plt.legend()
    plt.show()

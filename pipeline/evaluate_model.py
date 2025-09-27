from sklearn.metrics import classification_report

def evaluate_model(model, X_test, y_test):
    """
    Generate classification report for model predictions.
    Returns dictionary for programmatic access.
    """
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred, output_dict=True)
    return report

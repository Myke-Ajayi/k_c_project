from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from statsmodels.formula.api import ols

def evaluate (y_train, train_preds, y_test, test_preds):
    """
    Evaluate the amount of error between my model's predictions and actiual values for both train and test set
    
    Parameters:
    y_train - array like, actual values for 'price' 
    train_preds - array like predicted values for 'price'
    y_test -array like actual values for 'price'
    test_preds - array like predicted values for 'price'
    returns:
    None
    """
    print("Rsquared:")

    print(f"Train R2: {r2_score(y_train,train_preds):.4f}")
    print(f"Validation R2: {r2_score(y_test,test_preds):.4f}")

    print("-----")

    print("Root Mean squared Error:")

    print(f"Train RMSE: ${mean_squared_error(y_train,train_preds,squared = False):,.2f}")
    print(f"Validation RMSE: ${mean_squared_error(y_test,test_preds, squared = False):,.2f}")

    print("-----")

    print(" Mean absolute Error:")

    print(f"Train MAE: ${mean_absolute_error(y_train,train_preds):,.2f}")
    print(f"Validation MAE: ${mean_absolute_error(y_test,test_preds):,.2f}")
    





def evaluate_model (features,return_model = True):
    """
    evaluation of error on the target and the features 
    parameters:
    data - array like, actual values for all datasets
    model - ordinary least square method for fitting
    features - all cols without the target
    target - array like actual value for 'price'
    Returns:
    none
    """

    formula = 'price ~' + '+'.join(features)
    data = train_df
    model = ols(formula=formula, data=data).fit()
    print(f"{model.summary()}\n")


    if return_model:
        return model  
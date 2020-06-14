import warnings
warnings.filterwarnings(action='ignore')

# sklearn - scientific kit for ML

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

def get_data(file_name):
    dataframe = pd.read_csv(file_name)
    x_parameters = []
    y_parameters = []

    for single_square_feet, single_price_value in zip(dataframe['square_feet'], dataframe['price']):
        x_parameters.append([single_square_feet])
        y_parameters.append(([single_price_value]))

    return x_parameters,y_parameters


def linear_model_main(X_parameters, Y_parameters, quest_value):

    regr = LinearRegression()

    print("Area-", X_parameters)
    print("Price-", Y_parameters)

    # by fitting the training data, to train the algorithm, this fit() fnc will generate the model
    regr.fit(X_parameters, Y_parameters)
    # the o/p of this fnx is another program/model/fnc/algo/correlation


    predicted_ans = regr.predict([ [ quest_value ] ])
    predictions = {}
    predictions['coeffiecient'] = regr.coef_
    predictions['intercept'] = regr.intercept_
    predictions['predicted_ans'] = predicted_ans

    print("Output from Machine is-", predicted_ans)

    plt.scatter(X_parameters, Y_parameters, color='m', marker='o', s=20)

    all_predicted_Y = regr.predict(X_parameters)

    plt.scatter(X_parameters, all_predicted_Y, color='b')
    plt.plot(X_parameters, all_predicted_Y, color='r')

    plt.scatter(quest_value, predicted_ans, color='g')

    plt.show()

    return predictions



if __name__ == '__main__':

    x, y =get_data("LR_House_price.csv")

    question_value = 700
    result = linear_model_main(x, y, question_value)

    print(" coefficient/parameter m-", result['coeffiecient'])
    print(" intercept c-", result['intercept'])

    print("predicted house price value:", result['predicted_ans'])

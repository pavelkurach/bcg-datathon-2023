import pandas as pd
import numpy as np
from sklearn.model_selection import TimeSeriesSplit
from loss import compute_one_target_loss


def divide_by_targets(data):
    """Returns two copies with separated targets"""
    return data.iloc[:, :-1], data.loc[:, data.columns != data.columns[-2]]

def train_test_split(x, y, test_size):
    """
    Returns a tuple of train and test
    """
    assert x.shape[0] == y.shape[0]

    train_size = int(x.shape[0] * (1 - test_size))
    train_x, test_x = x[:train_size], x[train_size:]
    train_y, test_y = y[:train_size], y[train_size:]

    return train_x, train_y, test_x, test_y

def cross_val(model, x, y, n_splits = 5):
    """Computes split cross validation for a model with RMSE loss and returns the average loss"""
    tscv = TimeSeriesSplit(n_splits)
    results = np.array([])

    for train_index, val_index in tscv.split(x):
        model.fit(x[train_index], y[train_index])
        results.append(compute_one_target_loss(model.predict(x[val_index]), y[val_index]))

    return results.mean()





if __name__ == "__main__":
    d1 = {'col1': [1, 2, 3, 4, 3], 'col2': [5, 6, 7, 8, 3], 'col3': [55, 66, 77, 88, 33], 'col4': [5555, 66666, 777777, 88888, 3]}
    df1 = pd.DataFrame(data=d1)

    d2 = {'col1': [11, 21, 31, 41, 3]}
    df2 = pd.DataFrame(data=d2)
    #train_x, train_y, test_x, test_y = train_test_split(df1, df2, 0.2)
    #print(test_y)
    print(divide_by_targets(df1)[0])


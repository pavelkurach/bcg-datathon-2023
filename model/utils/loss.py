from sklearn.metrics import mean_squared_error
import numpy as np


def compute_one_target_loss(predictions, targets):
    """Computes standard RMSE loss for 1d arrays"""
    return mean_squared_error(targets, predictions, squared=False)

def compute_dual_target_loss(predictions, targets, mode):
    """
    Computes RMSE loss for a tuple of 1d arrays
    mode = "max", "min", "sum", "average", "separate"
    """
    assert predictions.shape[1] == targets.shape[1] == 2
    assert predictions.shape[0] == targets.shape[0]

    print(compute_one_target_loss(predictions[:, 0], targets[:, 0]))
    print(compute_one_target_loss(predictions[:, 1], targets[:, 1]))

    if mode == "max":
        return max(compute_one_target_loss(predictions[:, 0], targets[:, 0]),
                      compute_one_target_loss(predictions[:, 1], targets[:, 1]))

    elif mode == "min":
        return min(compute_one_target_loss(predictions[:, 0], targets[:, 0]),
                      compute_one_target_loss(predictions[:, 1], targets[:, 1]))

    elif mode == "sum":
        return compute_one_target_loss(predictions[:, 0], targets[:, 0]) + compute_one_target_loss(predictions[:, 1], targets[:, 1])

    elif mode == "average":
        return (compute_one_target_loss(predictions[:, 0], targets[:, 0]) + compute_one_target_loss(predictions[:, 1], targets[:, 1])) / 2

    elif mode == "separate":
        return (compute_one_target_loss(predictions[:, 0], targets[:, 0]),
                    compute_one_target_loss(predictions[:, 1], targets[:, 1]))
    else:
        print("Wrong mode value :(")





if __name__ == "__main__":
    target1 = [2, 2, 1]
    preds1 = [0, 0, 0]

    print("One target loss:", compute_one_target_loss(target1, preds1))

    target2 = np.array([[1,1],
                        [1,1],
                        [1,1]])
    preds2 = np.array([[0,3],
                        [0,3],
                        [0,3]])

    print("Two target loss max", compute_dual_target_loss(target2, preds2, "max"))
    print("Two target loss min", compute_dual_target_loss(target2, preds2, "min"))
    print("Two target loss sum", compute_dual_target_loss(target2, preds2, "sum"))
    print("Two target loss average", compute_dual_target_loss(target2, preds2, "average"))
    print("Two target loss separate", compute_dual_target_loss(target2, preds2, "separate"))
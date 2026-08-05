# Generated on 2026-08-05T19:01:55.319101

def calculate_loss(y_true, y_pred):
    import numpy as np
    return np.mean((y_true - y_pred)**2)

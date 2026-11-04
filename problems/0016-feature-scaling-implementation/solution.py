import numpy as np
def feature_scaling(data : np.ndarray):
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    standardized_data = (data-mean)/std
    min = np.min(data, axis=0)
    max = np.max(data, axis=0)
    normalized_data = (data - min)/(max - min)
    return np.round(standardized_data, 4), np.round(normalized_data, 4)
data = np.array([[1, 2], [3, 4], [5, 6]])
print(feature_scaling(data))
import numpy as np


def find_percentile(data, percentile):
    """
    Finds the specified percentile of the given data.

    Parameters:
    - data (list or array): The data for which to compute the percentile.
    - percentile (float): The percentile to compute (between 0 and 100).

    Returns:
    - float: The computed percentile value.
    """
    # return np.percentile(data, percentile, interpolation='midpoint')
    # default interpolation is linear
    return np.percentile(data, percentile)


def print_25_50_75_percentiles(data):
    percentile_75 = find_percentile(data, 75)
    percentile_50 = find_percentile(data, 50)
    percentile_25 = find_percentile(data, 25)
    print(f'75 percentile: {percentile_75}')
    print(f'50 percentile: {percentile_50}')
    print(f'25 percentile: {percentile_25}')




# # Example usage
# data = [1, 2, 5, 7, 8, 9, 10, 10, 11, 12, 13, 14, 15]
# percentile_50 = find_percentile(data, 50)  # 50th percentile (median)
# percentile_90 = find_percentile(data, 90)  # 90th percentile
#
# print(f"50th percentile (median): {percentile_50}")
# print(f"90th percentile: {percentile_90}")

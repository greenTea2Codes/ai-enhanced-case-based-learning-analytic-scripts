import matplotlib.pyplot as plt
import re


def draw_and_save_box_plot(data, title='Box Plot', x_label='X-axis', y_label='Y-axis', showfliers=True,
                           save_plot=False, labels=None):
    """
    Draws a box plot for the given data and optionally saves it with the title name.

    Parameters:
    - data (list or DataFrame): The data to plot. Can be a list of values or a pandas DataFrame.
    - title (str): The title of the plot.
    - x_label (str): The label for the x-axis.
    - y_label (str): The label for the y-axis.
    - showfliers (bool): Whether to show outliers (default is True).
    - save_plot (bool): Whether to save the plot with the title name (default is False).
    - labels (list): The labels for the groups.

    Returns:
    - None
    """
    plt.figure(figsize=(10, 6))
    plt.boxplot(data, showfliers=showfliers, labels=labels)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)

    if save_plot:
        # Create a valid filename from the title
        filename = re.sub(r'[^\w\s-]', '', title).strip().lower()
        filename = re.sub(r'[-\s]+', '_', filename) + '.png'
        filename = f'./output/{filename}'
        plt.savefig(filename)
        print(f"Plot saved as {filename}")
    else:
        plt.show()
    plt.close()

# # Example usage with a list of values
# data = [1, 2, 5, 7, 8, 9, 10, 10, 11, 12, 13, 14, 15]
# draw_and_save_box_plot(data, title='Sample Box Plot 1', x_label='Data Points', y_label='Value', save_plot=True)
#
# # Example usage with a pandas DataFrame
# import pandas as pd
# df = pd.DataFrame({
#     'Category 1': [1, 2, 5, 7, 8, 9, 10, 10, 11, 12, 13, 14, 15],
#     'Category 2': [2, 3, 6, 8, 9, 10, 11, 11, 12, 13, 14, 15, 16]
# })
# draw_and_save_box_plot([df['Category 1'], df['Category 2']], title='Sample Box Plot 2', x_label='Categories', y_label='Value', save_plot=True)

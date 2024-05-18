import string


def excel_column_to_index(column_name):
    """
    Convert an Excel-style column name (e.g., 'A', 'B', ..., 'Z', 'AA', etc.) to a zero-based DataFrame column index.
    """
    column_name = column_name.upper()  # Ensure the column name is in uppercase
    index = 0
    for char in column_name:
        index = index * 26 + (ord(char) - ord('A') + 1)
    return index - 1  # Convert to zero-based index


def index_to_excel_column(index):
    """
    Convert a zero-based index to an Excel-style column name (e.g., 0 -> 'A', 1 -> 'B', ..., 26 -> 'AA').
    """
    result = []
    while index >= 0:
        index, remainder = divmod(index, 26)
        result.append(string.ascii_uppercase[remainder])
        index -= 1
    return ''.join(result[::-1])


def generate_excel_column_range(start, end):
    """
    Generate a list of Excel-style column names from start to end (inclusive).
    """
    start_index = excel_column_to_index(start)
    end_index = excel_column_to_index(end)
    return [index_to_excel_column(i) for i in range(start_index, end_index + 1)]

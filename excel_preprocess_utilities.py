def excel_column_to_index(column_name):
    """
    Convert an Excel-style column name (e.g., 'A', 'B', ..., 'Z', 'AA', etc.) to a zero-based DataFrame column index.
    """
    column_name = column_name.upper()  # Ensure the column name is in uppercase
    index = 0
    for char in column_name:
        index = index * 26 + (ord(char) - ord('A') + 1)
    return index - 1  # Convert to zero-based index

def calculate_determinant(matrix):
    """
    Function to calculate the determinant of a matrix using recursion.
    :param matrix: 2D list representing the matrix
    :return: determinant of the matrix
    """
    # Check if the matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise ValueError("Input must be a 2D list representing the matrix.")
    
    # Check if the matrix is square
    rows = len(matrix)
    if not all(len(row) == rows for row in matrix):
        raise ValueError("Matrix must be square (same number of rows and columns).")
    
    # Base case for 1x1 matrix
    if rows == 1:
        return matrix[0][0]

    # Base case for 2x2 matrix
    if rows == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Recursive case for larger matrices
    determinant = 0
    for col in range(rows):
        # Minor matrix excluding the first row and current column
        minor = [row[:col] + row[col + 1:] for row in matrix[1:]]
        # Recursively calculate the determinant of the minor matrix
        determinant += ((-1) ** col) * matrix[0][col] * calculate_determinant(minor)
    
    return determinant


def get_user_matrix():
    """
    Function to take matrix input from the user.
    :return: 2D list representing the matrix
    """
    try:
        n = int(input("Enter the order of the square matrix (e.g., 3 for 3x3): "))
        if n <= 0:
            raise ValueError("Matrix order must be a positive integer.")

        print(f"Enter the matrix row by row (separate elements with spaces):")
        matrix = []
        for i in range(n):
            row = list(map(float, input(f"Row {i + 1}: ").split()))
            if len(row) != n:
                raise ValueError(f"Each row must have exactly {n} elements.")
            matrix.append(row)
        return matrix
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None


# Main Program for the code
if __name__ == "__main__":
    user_matrix = get_user_matrix()
    if user_matrix:
        try:
            det = calculate_determinant(user_matrix)
            print(f"The determinant of the matrix is: {det}")
        except ValueError as e:
            print(f"Error: {e}")

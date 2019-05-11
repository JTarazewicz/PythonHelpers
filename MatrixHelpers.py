def matrix_multiplication(matrix_1, matrix_2):
    """
    Multiplicate two matrices.
    """
    for row in matrix_1:
        if len(row) != len(matrix_2):
            return "You can't multiplicate those matrices."
        else:
            result = [
                [sum(elem_m_1 * elem_m_2 for elem_m_1, elem_m_2 in zip(row_m_1, col_m_2)) for col_m_2 in zip(*matrix_2)]
                for row_m_1 in matrix_1]
    return result


def sum_matrix(matrix_1, matrix_2):
    """
    Add two matrices.
    """
    for r_1 in matrix_1:
        for r_2 in matrix_2:
            if len(matrix_1) != len(matrix_2) and len(r_1) != len(r_2):
                result = "You can't add those matrices"
                break
            else:
                result = [[matrix_1[i][j] + matrix_2[i][j] for j in range(len(matrix_1[0]))] for i in range(len(X))]
    return result


def matrix_to_list(matrix):
    """
    Flatten matrix into a list.
    """
    result = [elem for row in matrix for elem in row]
    return result

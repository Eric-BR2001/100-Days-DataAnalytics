def exist(board, word):
    rows, cols = len(board), len(board[0])

    def dfs(r, c, idx):
        if idx == len(word):
            return True  # palavra completa encontrada
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return False  # fora da matriz
        if board[r][c] != word[idx]:
            return False  # letra errada

        temp = board[r][c]
        board[r][c] = '#'  # marca como visitado

        # busca em 4 direções: cima, baixo, esquerda, direita
        found = (
            dfs(r + 1, c, idx + 1) or
            dfs(r - 1, c, idx + 1) or
            dfs(r, c + 1, idx + 1) or
            dfs(r, c - 1, idx + 1)
        )

        board[r][c] = temp  # desfaz a marcação
        return found

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == word[0] and dfs(i, j, 0):
                return True

    return False

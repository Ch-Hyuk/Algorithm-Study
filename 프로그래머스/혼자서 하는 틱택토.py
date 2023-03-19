def solution(board):
    O_cnt, X_cnt = 0, 0
    first = [0 for _ in range(8)]
    second = [0 for _ in range(8)]
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                O_cnt +=1
                first[i] += 1
                first[j+3] += 1

                if i+j == 2:
                    first[6] += 1
                if i == j:
                    first[7] += 1

            elif board[i][j] == 'X':
                X_cnt +=1
                second[i] += 1
                second[j+3] += 1

                if i+j == 2:
                    second[6] += 1
                if i == j:
                    second[7] += 1

    if O_cnt < X_cnt or abs(O_cnt - X_cnt) > 1:
        return 0

    if O_cnt == X_cnt and 3 in first:
        return 0 

    if O_cnt > X_cnt and 3 in second:
        return 0

    return 1
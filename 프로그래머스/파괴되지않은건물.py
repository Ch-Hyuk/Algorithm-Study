def solution(board, skill):
    answer = 0
    dmg_board = [[0]*(len(board[0])+2) for _ in range(len(board)+2)]
    sum_board = [[0]*(len(board[0])+2) for _ in range(len(board)+2)]
    for sk in skill:
        damage = sk[5]
        if sk[0] == 1: damage*=(-1)
        dmg_board[sk[1]+1][sk[2]+1] += damage
        dmg_board[sk[1]+1][sk[4]+2] -= damage
        dmg_board[sk[3]+2][sk[2]+1] -= damage
        dmg_board[sk[3]+2][sk[4]+2] += damage

    for N in range(len(dmg_board)):
        dmg_board[N][0] += dmg_board[N-1][0]
    
    for M in range(len(dmg_board[0])):
        dmg_board[0][M] += dmg_board[0][M]

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += sum_board[i+1][j+1]
            if board[i][j] > 0:
                answer += 1

    return answer

board = [[1,2,3],[4,5,6],[7,8,9]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
print(solution(board, skill))
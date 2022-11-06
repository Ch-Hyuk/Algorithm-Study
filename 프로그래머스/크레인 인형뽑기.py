#pprint는 확인용 import 실제로는 필요없음
from pprint import pprint

def solution(board, moves):
    answer = 0
    basket = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] == 0:
                continue
            else:
                basket.append(board[j][i-1])
                print("\nbasket: ",basket)
                print("index: ",basket.index(board[j][i-1]),"\n")
                if len(basket) == 1:
                    board[j][i-1] = 0
                    break

                elif basket[-2] == basket[-1]:
                    print("조건문 통과")
                    del basket[-2:]
                    answer+=2
                    print("결과값: ", answer)
                board[j][i-1] = 0
                break
    pprint(board)
    return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
pprint(board)
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))
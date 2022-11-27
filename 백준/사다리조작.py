#N: 세로선, M: 실제로 놓여있는 선, H: 가로선
N, M, H = map(int,input().split())
answer = 0
ladder_list = [[0] * (N+2)  for _ in range(H+1)]
ladder_dic ={} #행: 열 두개
for i in range(H+1):
    ladder_list[i][0] = 9
    ladder_list[i][-1] = 9
    ladder_dic[i+1] = list()

for ladder in range(M):
    a,b = map(int,input().split())
    ladder_list[a][b] = 1
    ladder_list[a][b+1] = 1
    ladder_dic[a] += [(b, b+1)]

print(ladder_dic)
print(ladder_list)

def dfs(row, col, start_col):
    print("현재노드", row, col)
    cnt = 0
    if row == H+1 and col != start_col:
        print("마지막에서 돌아가기")
        return -1
    
    elif row == H+1 and col == start_col:
        print("마지막 일치")
        return 0
    
    if ladder_list[row][col] == 1:
        if ladder_list[row][col+1] == 1 and ladder_list[row][col-1] == 0 or ladder_list[row][col+1] == 1 and ladder_list[row][col-1] == 9:
            return dfs(row+1, col+1, start_col)

        elif ladder_list[row][col-1] == 1 and ladder_list[row][col+1] == 0 or ladder_list[row][col-1] == 1 and ladder_list[row][col+1] == 9:
            return dfs(row+1, col-1, start_col)

        elif ladder_list[row][col-1] == 1 and ladder_list[row][col+1] == 1:
            print("양쪽 1")
            print(ladder_dic)
            for data in ladder_dic[row]:
                print(data)
                if col in data:
                    if data[0] == col:
                        return dfs(row+1, col+1, start_col)
                    else:
                        return dfs(row+1, col-1, start_col)

    if ladder_list[row][col] == 0:
        data = dfs(row+1, col, start_col)
        if data != -1:
            return data
        elif data == -1:
            if ladder_list[row][col+1] == 1 and ladder_list[row][col-1] == 1 or ladder_list[row][col+1] == 1 and ladder_list[row][col-1] == 9 or ladder_list[row][col+1] == 9 and ladder_list[row][col-1] == 9:
                print("양쪽1이라 위로이동")
                return data

            elif ladder_list[row][col+1] == 0 and ladder_list[row][col-1] == 1:
                print("오른쪽으로 선긋기")
                cnt = dfs(row+1,col+1,start_col)
                if cnt != -1:
                    ladder_list[row][col] = 1
                    ladder_list[row][col+1] = 1
                    ladder_dic[row] += [(col,col+1)]
                    print(ladder_list)
                    print(ladder_dic)
                    return cnt+1
                else:
                    return -1

            elif ladder_list[row][col-1] == 1 and ladder_list[row][col-1] == 0:
                if ladder_list[row][col-1] != 1:
                    print("왼쪽으로 선긋기")
                    cnt = dfs(row+1,col-1,start_col)
                    if cnt != -1:
                        ladder_list[row][col] = 1
                        ladder_list[row][col-1] = 1
                        ladder_dic[row] += [(col-1,col)]
                        print(ladder_list)
                        print(ladder_dic)
                        return cnt+1
                    else:
                        return -1

            else:
                if (start_col - col) < 0:
                    print("왼쪽으로 선긋기")
                    cnt = dfs(row+1,col-1,start_col)
                    if cnt != -1:
                        ladder_list[row][col] = 1
                        ladder_list[row][col-1] = 1
                        ladder_dic[row] += [(col-1,col)]
                        print(ladder_list)
                        return cnt+1
                    else:
                        return -1

                else:
                    print("오른쪽으로 선긋기")
                    cnt = dfs(row+1,col+1,start_col)
                    if cnt != -1:
                        ladder_list[row][col] = 1
                        ladder_list[row][col+1] = 1
                        ladder_dic[row] += [(col,col+1)]
                        print(ladder_list)
                        return cnt+1
                    else:
                        return -1
print(ladder_list)

for col in range(1,H):
    print(col,"번째 열")
    print(ladder_list)
    cnt = dfs(1, col, col)
    print(cnt)
    if cnt == -1:
        print(-1)
        break
    else:
        answer += cnt
        if answer > 3:
            print(-1)

print(answer)
    
        
FF, FS, SF ,SS = map(int,input().split())

answer = FF

def choice(FS, SF, SS):
    global answer
    if FS == 0:
        if answer != 0:
            return 
        if SF != 0:
            answer = SS + 1
        else:
            answer = SS

    else:
        if FS > SF:
            answer = answer + SF*2 +1 + SS

        elif FS <= SF:
            answer = answer + FS*2+ SS


choice(FS, SF, SS)
print(answer)
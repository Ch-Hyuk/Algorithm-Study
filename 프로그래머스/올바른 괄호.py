def solution(s):
    answer = True
    in_stack = []
    for data in s:

        if data == '(':
            in_stack.append(data)
            
        if data == ')' and len(in_stack) == 0:
            return False
        
        elif data == ')' and len(in_stack) > 0:
            in_stack.pop()
    
    if len(in_stack) > 0:
        return False
    else:
        return True
    
    
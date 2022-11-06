new_id ="123_.def"
answer=''
table = new_id.maketrans({
    '~':'',
    '!':'',
    '@':'',
    '#':'',
    '$':'',
    '%':'',
    '^':'',
    '&':'',
    '*':'',
    '(':'',
    ')':'',
    '=':'',
    '+':'',
    '[':'',
    '{':'',
    ']':'',
    '}':'',
    ':':'',
    '?':'',
    ',':'',
    '<':'',
    '>':'',
    '/':''
})
st = new_id.lower().translate(table)
print(st)
for i in range(0,len(st)):
    if i == len(st)-1:
        answer += st[i]
        break
    if st[i] == '.' and st[i+1] == '.':
        answer+=''
    else:
        answer += st[i]
print(answer)
answer = answer.strip('.')
print(answer)
if answer == '':
    answer +='a'

if len(answer) >= 16:
    answer = answer[:15].strip('.')
elif len(answer) == 2:
    answer = answer + answer[-1]
elif len(answer) == 1:
    answer = answer + answer[-1] + answer[-1]
print(answer)
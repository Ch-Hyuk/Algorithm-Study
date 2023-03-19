def solution(n, words):
    word_set = set()
    last_word = words[0][0]
    person, cnt = 1, 1
    for i in range(len(words)):
        if words[i] in word_set or words[i][0] != last_word:
            return [person, cnt]

        word_set.add(words[i])
        last_word = words[i][-1]

        if (i+1)%n == 0:
            person = 1
            cnt += 1
        else:
            person += 1

    return [0,0]
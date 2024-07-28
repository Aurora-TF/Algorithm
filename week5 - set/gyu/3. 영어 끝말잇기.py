
def solution(n, words):
    dictionary = {}
    answer = [0, 0]
    prev = None
    for i in range(len(words)):
        index = (i % n) + 1
        turn = i // n + 1
        
        word = words[i] 
        
        if word not in dictionary:
            dictionary[word] = True
        else:
          answer = [index, turn]
          break
        
        if prev is None:
            prev = word
        elif prev[-1] != word[0]:
            answer = [index, turn]
            break
        
        prev = word
    
    return answer
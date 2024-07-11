def solution(want, number, discount):
    answer = 0
    wishlist = {}
    
    for i in range(len(want)):
        wishlist[want[i]] = number[i]
    
    for i in range(len(discount) - 9):
        wishlist_copy = wishlist.copy()
        
        for j in range(i, i + 10):
            if discount[j] in wishlist_copy and wishlist_copy[discount[j]] != 0:
                wishlist_copy[discount[j]] -= 1
            else:
                break
                
        if sum(wishlist_copy.values()) == 0:
            answer += 1    
    
    return answer
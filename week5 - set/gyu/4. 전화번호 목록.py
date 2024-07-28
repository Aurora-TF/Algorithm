def solution(phone_book: list):
    data_map = {}
    answer = True
    phone_book.sort(key= lambda x: len(x))
    for phone_number in phone_book:
        for i in range(1, len(phone_number)+1):
            if data_map.get(phone_number[:i], False):
                return False
        data_map[phone_number] = True
    return answer
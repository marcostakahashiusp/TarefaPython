def search_value(key, list):
    i = 0
    while key >= list[i]:
        if key == list[i]:
            return True
            break
        i = i+1
    return False

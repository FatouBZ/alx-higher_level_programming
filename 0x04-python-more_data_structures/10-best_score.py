def best_score(a_dictionary):
    if a_dictionary:
        i = a_dictionary.items()
        sort = (sorted(i, key=lambda i: i[1], reverse=True))
        return sort[0][0]

def merge_dicts(dict1, dict2):
    merged = dict1.copy()

    for key, value in dict2.items():
        
        if (existing := merged.get(key)) is not None:
           
            if isinstance(existing, (int, float)) and isinstance(value, (int, float)):
                merged[key] = existing + value
            else:
                merged[key] = value
        else:
            merged[key] = value

    return merged


dict_a = {
    'apple': 3,
    'banana': 5,
    'cherry': 'sweet'
}

dict_b = {
    'banana': 2,
    'cherry': 'sour',
    'date': 10
}


result = merge_dicts(dict_a, dict_b)


print("Merged dictionary:")
print(result)

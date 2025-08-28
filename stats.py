def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    counts = {}
    for char in text.lower():
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
    return counts

def sort_char_counts(counts):
    order = []
    for char, count in counts.items():
        new_char_data = {"char": char, "num": count}
        order.append(new_char_data)
    order.sort(key=lambda x: x["num"], reverse=True)
    return order


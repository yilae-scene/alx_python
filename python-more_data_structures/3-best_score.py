
# a function that returns the biggest value of dict.

def best_score(a_dictionary):
    try:
        new_value = list(a_dictionary.values())
        max = new_value[0]
        for n in range(len(new_value)):
            if max < new_value[n]:
                max = new_value[n]
        for k, v in a_dictionary.items():
            if max == v:
                return k
    except (ValueError, TypeError, AttributeError):
        return None


a_dictionary = {'John': 14, 'Bob': 25, 'Mike': 10, 'Molly': 9, 'Adam': 112}
print(best_score(a_dictionary))

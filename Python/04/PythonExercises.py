# Day 4: Python Function Exercises - Data Structures

# 1. Add an element to a list
def add_to_list(lst, element):
    lst.append(element)
    return lst

# 2. Remove duplicates from a list
def remove_duplicates(lst):
    return list(set(lst))

# 3. Merge two dictionaries
def merge_dicts(d1, d2):
    return {**d1, **d2}

# 4. Count frequency of elements in a list using dictionary
def count_frequency(lst):
    from collections import Counter
    return dict(Counter(lst))

# 5. Check if key exists in dictionary
def key_exists(d, key):
    return key in d

# 6. Push and pop from stack
def stack_operations():
    stack = []
    stack.append(10)
    stack.append(20)
    popped = stack.pop()
    return stack, popped

# 7. Enqueue and dequeue in queue
def queue_operations():
    from collections import deque
    queue = deque()
    queue.append('a')
    queue.append('b')
    dequeued = queue.popleft()
    return list(queue), dequeued

# 8. Create a set and perform union, intersection
def set_operations(a, b):
    set_a, set_b = set(a), set(b)
    return {
        'union': set_a | set_b,
        'intersection': set_a & set_b
    }

# 9. Get keys and values from dictionary
def keys_values(d):
    return list(d.keys()), list(d.values())

# 10. Sort a list of tuples by second value
def sort_by_second(tuples):
    return sorted(tuples, key=lambda x: x[1])


# Example Tests
if __name__ == "__main__":
    print("Add to list:", add_to_list([1, 2], 3))
    print("Remove duplicates:", remove_duplicates([1, 2, 2, 3]))
    print("Merge dicts:", merge_dicts({'a': 1}, {'b': 2}))
    print("Frequency count:", count_frequency(['a', 'b', 'a', 'c', 'b']))
    print("Key exists:", key_exists({'x': 1}, 'x'))
    print("Stack operations:", stack_operations())
    print("Queue operations:", queue_operations())
    print("Set operations:", set_operations([1, 2, 3], [2, 3, 4]))
    print("Keys and values:", keys_values({'name': 'Alice', 'age': 30}))
    print("Sort by second:", sort_by_second([('a', 3), ('b', 1), ('c', 2)]))

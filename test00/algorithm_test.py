# bubble sort with optimization
def bubble_sort_v1(array):
    # Record the position of the last exchange
    last_exchange_index = 0
    # Boundaries of unordered series, each comparison only needs to compare up to here
    sort_border = len(array) - 1
    for i in range(len(array) - 1):
        is_sorted = True
        for j in range(sort_border):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                is_sorted = False
                last_exchange_index = j
        sort_border = last_exchange_index
        if is_sorted:
            break


# cocktail sort without optimization
def cock_tail_sort(array):
    for i in range(len(array) // 2):
        # Odd number of cycles
        is_sorted = True
        for j in range(i, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                is_sorted = False
        if is_sorted:
            break
        # Even number of cycles
        is_sorted = True
        for j in range(len(array) - i - 1, i, -1):
            if array[j] < array[j - 1]:
                temp = array[j]
                array[j] = array[j - 1]
                array[j - 1] = temp
                is_sorted = False
        if is_sorted:
            break


# quick sort with single_side
# Defect: the second element is less than the first element, there will be a error
def quick_sort(start_index, end_index, array):
    # recursive condition
    if start_index >= end_index:
        return
    pivot_index = single_side(start_index, end_index, array)
    # split to two sort parts according to pivot
    quick_sort(start_index, pivot_index - 1, array)
    quick_sort(pivot_index + 1, end_index, array)


def single_side(start_index, end_index, array):
    pivot = array[start_index]
    mark = start_index
    for i in range(start_index + 1, end_index + 1):
        if array[i] < pivot:
            mark = mark + 1
            temp = array[i]
            array[i] = array[mark]
            array[mark] = temp
    array[start_index] = array[mark]
    array[mark] = pivot
    return mark


# quick sort with stack
def quick_sort_stack(start_index, end_index, array):
    sort_stack = []
    root_param = {"startIndex": start_index, "endIndex": end_index}
    sort_stack.append(root_param)
    while len(sort_stack) > 0:
        param = sort_stack.pop()
        pivot_index = single_side(param.get("startIndex"), param.get("endIndex"), array)
        if param.get("startIndex") < pivot_index - 1:
            left_root_param = {"startIndex": param.get("startIndex"), "endIndex": pivot_index - 1}
            sort_stack.append(left_root_param)
        if param.get("endIndex") > pivot_index + 1:
            right_root_param = {"startIndex": pivot_index + 1, "endIndex": param.get("endIndex")}
            sort_stack.append(right_root_param)


# heap sort
def heap_sort(array):
    # Turn the unordered array into the largest heap
    for i in range((len(array) - 2) // 2, -1, -1):
        down_adjust(i, len(array), array)
    for j in range(len(array) - 1, 0, -1):
        temp = array[j]
        array[j] = array[0]
        array[0] = temp
        down_adjust(0, j, array)


def down_adjust(parent_index, length, array):
    temp = array[parent_index]
    child_index = parent_index * 2 + 1
    while child_index < length:
        if child_index + 1 < length and array[child_index + 1] > array[child_index]:
            child_index += 1
        if array[parent_index] > array[child_index]:
            break
        array[parent_index] = array[child_index]
        parent_index = child_index
        child_index = parent_index * 2 + 1
        array[parent_index] = temp


# count sort with optimization
# defect:1. The algorithm is not suitable when the difference between the maximum and minimum values is large
#        2. This algorithm is not suitable to use when the array elements are not integers
def count_sort(array):
    max_value = array[0]
    min_array = array[0]
    new_array = [0] * len(array)
    for i in range(1, len(array)):
        if array[i] > max_value:
            max_value = array[i]
        if array[i] < min_array:
            min_array = array[i]
    d = max_value - min_array
    count_array = [0] * (d + 1)
    for i in range(len(array)):
        count_array[array[i] - min_array] += 1
    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]
    for i in range(len(array) - 1, -1, -1):
        new_array[count_array[array[i] - min_array] - 1] = array[i]
        count_array[array[i] - min_array] -= 1
    return new_array


# bucket sort
def bucket_sort(array):
    max_value = array[0]
    min_array = array[0]
    for i in range(1, len(array)):
        if array[i] > max_value:
            max_value = array[i]
        if array[i] < min_array:
            min_array = array[i]
    d = max_value - min_array
    # initialize bucket
    bucket_list = []
    bucket_num = len(array)
    for i in range(0, bucket_num):
        bucket_list.append([])
    # Iterate over the original array and place the elements into the corresponding buckets
    for i in range(len(array)):
        num = int((array[i] - min_array) * (bucket_num - 1) / d)
        bucket = bucket_list[num]
        bucket.append(array[i])
    # Sorting the elements inside each bucket
    for i in range(0, len(bucket_list)):
        bucket_list[i].sort()
    # output
    sorted_array = []
    for sub_list in bucket_list:
        for element in sub_list:
            sorted_array.append(element)
    return sorted_array


# my_array = [5, 11, 2, 8, 1, 10, 6, 5]
# heap_sort(my_array)
# print(bucket_sort(my_array))


# Question: How to judge linked list has a circle or not

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def is_circle(head):
    p1 = head
    p2 = head
    while p2 is not None and p2.next is not None:
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:
            return True
    return False


node1 = Node(5)
node2 = Node(2)
node3 = Node(1)
node4 = Node(2)
node5 = Node(8)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2


# print(is_circle(node1))


# Find the greatest common divisor of two integers
# Euclidean algorithm
def get_greatest_common_divisor(a, b):
    while True:
        if a > b:
            c = a % b
            if c == 0:
                return b
            a = c
        else:
            c = b % a
            if c == 0:
                return a
            b = c


# print(get_greatest_common_divisor(20, 112))


# Bitmap algorithm
class MyBitmap:
    def __init__(self, size):
        self.words = [0] * (self.get_word_index(size - 1) + 1)
        self.size = size

    def get_bit(self, bit_index):
        if bit_index < 0 or bit_index > self.size - 1:
            raise Exception("over Bitmap valid range!")
        word_index = self.get_word_index(bit_index)
        return (self.words[word_index] & 1 << bit_index) != 0

    def set_bit(self, bit_index):
        if bit_index < 0 or bit_index > self.size - 1:
            raise Exception("over Bitmap valid range!")
        word_index = self.get_word_index(bit_index)
        self.words[word_index] |= (1 << bit_index)

    def get_word_index(self, bit_index):
        return bit_index >> 6


# LRU algorithm
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRUCache:
    def __init__(self, limit):
        self.hash = {}
        self.head = None
        self.end = None
        self.limit = limit

    def get(self, key):
        node = self.hash.get(key)
        if node is None:
            return None
        self.refresh_node(node)
        return node.value

    def put(self, key, value):
        node = self.hash.get(key)
        if node is None:
            if len(self.hash) >= self.limit:
                old_key = self.remove_node(self.head)
                self.hash.pop(old_key)
            node = Node(key, value)
            self.add_node(node)
            self.hash[key] = node
        else:
            node.value = value
            self.refresh_node(node)

    def refresh_node(self, node):
        if node == self.end:
            return
        self.remove_node(node)
        self.add_node(node)

    def remove_node(self, node):
        if node == self.head and node == self.end:
            self.head = None
            self.end = None
        elif node == self.head:
            self.head = self.head.next
            self.head.pre = None
        elif node == self.end:
            self.end = self.end.pre
            self.end.next = None
        else:
            node.pre.next = node.next
            node.next.pre = node.pre
        return node.key

    def add_node(self, node):
        if self.end is not None:
            self.end.next = node
            node.pre = self.end
            node.next = None
        self.end = node
        if self.head is None:
            self.head = node

    def remove(self, key):
        node = self.hash.get(key)
        self.remove_node(node)
        self.hash.pop(key)


# Divide red package algorithm
import random


def divide_red_package(amount, num):
    amount_list = []
    rest_amount = amount
    rest_num = num
    for i in range(0, num - 1):
        random_amount = random.randint(1, int(rest_amount / rest_num * 2) - 1)
        rest_amount -= random_amount
        rest_num -= 1
        amount_list.append(random_amount)
    amount_list.append(rest_amount)
    return amount_list

# my_red_package = divide_red_package(100, 5)
# for i in my_red_package:
#     print(i)
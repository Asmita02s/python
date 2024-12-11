#Write Python program to merge two sorted lists into a single sorted list#

def merge_sorted_lists(list1, list2):
    """
    Merge two sorted lists into a single sorted list.

    :param list1: First sorted list
    :param list2: Second sorted list
    :return: Merged sorted list
    """
    merged_list = []
    i, j = 0, 0

    # Traverse both lists and append smaller element to merged_list
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Append remaining elements of list1, if any
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    # Append remaining elements of list2, if any
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list

# Test the function
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
result = merge_sorted_lists(list1, list2)
print("Merged Sorted List:",result)

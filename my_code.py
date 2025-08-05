def split_words(text):

    cleaned_text = ""
    for char in text:
        if ('A' <= char <= 'Z') or ('a' <= char <= 'z') or ('0' <= char <= '9') or char == ' ':
            cleaned_text += char

    new_list = []
    for word in cleaned_text.split():
        new_list.append(word)

    return new_list

print(split_words("Happy birthday!!! to you @123"))

def search(nums, target):
    nums.sort()
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
print(search([-1, 0, 2, 3, 9, 8], 9))
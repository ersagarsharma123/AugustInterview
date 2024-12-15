lst = [100, 4, 200, 1, 3, 2, 5, 8, 7, 6]


def get_longest_streak(lst):
    longest_streak = 0
    for i in lst:
        if i - 1 is not lst:
            current_num = i
            current_streak = 0
            while current_num in lst:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)
    return longest_streak


result = get_longest_streak(lst)
print('longest_streak=', result)

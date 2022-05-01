import cProfile


MIN_DIV = 2
MAX_DIV = 9


def div_count(max_number):
    div_dict = dict()

    for div in range(MIN_DIV, MAX_DIV + 1):
        div_dict[div] = max_number // div

    return div_dict

# py -m timeit -n 100 -s "import Lesson_4_Task_1" "Lesson_4_Task_1.div_count(99)"
# "Lesson_4_Task_1.div_count(99)"
# 100 loops, best of 5: 795 nsec per loop
# "Lesson_4_Task_1.div_count(999)"
# 100 loops, best of 5: 809 nsec per loop
# "Lesson_4_Task_1.div_count(9999)"
# 100 loops, best of 5: 853 nsec per loop
# "Lesson_4_Task_1.div_count(99999)"
# 100 loops, best of 5: 858 nsec per loop
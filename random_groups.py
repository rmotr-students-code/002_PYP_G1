import random
from pprint import pprint


students = [
    'Will Hoback',
    'Brendan Emery',
    'Nino Mollaneda',
    'Alan Johnson',
    'Paulo Daniel Gonzalez',
    'Martin Latremouille',
    'Michael Azar',
    'Charles Lee',
]

def get_random_groups(students_list, group_size=2):
    def _get_random_student(students_copy):
        return students_copy.pop(random.randint(0, len(students_copy)-1))

    students_copy = students_list[:]
    groups = []
    current_group = []
    for _ in range(len(students_copy)):
         student = _get_random_student(students_copy)
         current_group.append(student)
         if len(current_group) == group_size:
              groups.append(current_group)
              current_group = []
    if len(current_group):
        groups.append(current_group)
    return groups

groups = get_random_groups(students)
for i, group in enumerate(groups):
    print 'Group {}: {}'.format(
        i + 1, ', '.join([s.split(' ')[0] for s in group]))

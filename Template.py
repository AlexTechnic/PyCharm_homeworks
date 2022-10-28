# Template.py
# Prog Academy python developer course (22.10.2022)
# part I - python start - imperative programing
# teacher - Oleh Tymchuk

# written on pycharm v.2022.1.3
# tested on python v.3.10.8

homework_num = 1
student_name = ''
homework_date = ''  # in format dd.mm.yyyy

# information about homework #, author and date
print('\n' 'Homework #' + str(homework_num) + ' ' + student_name + ' '
      + homework_date, '\n\n***********************\n')

# list of tasks
task_1 = ''

task_2 = ''

task_3 = ''

task_4 = ''

task_5 = ''

task_list = (task_1, task_2, task_3, task_4, task_5)

task_counter = 0


def task_brief():  # function to print task brief text
    print('Task ' + str(task_counter + 1) + '. ' + str(task_list[0 + task_counter])
          + '\n\nResult:\n')


def task_divider():  # function of divider between tasks
    input('\n*** Press Enter key to execute next task ***\n')


# start of task #1
task_brief()  # call brief func

print('Hello World 1')  # solution 1

task_counter += 1  # increment of task counter

task_divider()

# start of task #2
task_brief()  # call brief func

print('Hello World 2')  # solution 2

task_counter += 1  # increment of task counter

task_divider()

# start of task #3
task_brief()  # call brief func

print('Hello World 3')  # solution 3

task_counter += 1  # increment of task counter

task_divider()

# start of task #4
task_brief()  # call brief func

print('Hello World 4')  # solution 4

task_counter += 1  # increment of task counter

task_divider()

# start of task #5
task_brief()  # call brief func

print('Hello World 5')  # solution 5

task_counter += 1  # increment of task counter

# end of tasks
print('\n*** End of tasks list ***')

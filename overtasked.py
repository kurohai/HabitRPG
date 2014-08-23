#!/usr/bin/env python3
import habitrpg

MAX_TODOS = 20
CLEAR_THRESHOLD = 15
TASK_NAME = 'Cut the todo list down to ≤{} tasks'.format(CLEAR_THRESHOLD)

if __name__ == '__main__':
    hrpg = habitrpg.HabitRPG.login_from_file()
    tasks = hrpg.tasks()

    incomplete_todos = sum(1 for task in tasks if
            isinstance(task, habitrpg.Todo) and not task.completed)
    reduce_task = next((task for task in tasks if task.text == TASK_NAME and
                            not task.completed),
                       None)

    if incomplete_todos > MAX_TODOS and reduce_task is None:
        Todo.create(text=TASK_NAME)
    if incomplete_todos <= (CLEAR_THRESHOLD + 1) and reduce_task is not None:
        reduce_task.complete()

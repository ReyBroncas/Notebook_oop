from notebook import Notebook, Note
from menu import Menu


def display():
    obj_list = [Notebook, Note, Menu]
    for obj in obj_list:
        print('─' * 40 + f'\nAn object "{obj}" has:')
        for k, v in vars(obj).items():
            if callable(v):
                print(f'──> a method "{k}", which: {v.__doc__}')


if __name__ == '__main__':
    display()

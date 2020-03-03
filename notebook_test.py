from notebook import Notebook, Note
from menu import Menu
import pprint


def display():
    obj_list = [Notebook, Note, Menu]
    for obj in obj_list:
        print('─' * 40 + f'\nAn object "{obj}" has:')
        for k, v in vars(obj).items():
            if callable(v):
                print(f'──> a method "{k}", which: {v.__doc__}')
    for obj in obj_list:
        print('─' * 40 + f'\n\nPlain list of methods an attributes of\
 an object {obj} :')
        pprint.pprint(sorted(dir(obj)))


if __name__ == '__main__':
    display()

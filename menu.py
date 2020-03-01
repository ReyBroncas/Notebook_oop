from notebook import Notebook, Note
import sys
import os.path
import json
import glob


class Menu:
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            '1': self.show_notes,
            '2': self.search_notes,
            '3': self.add_note,
            '4': self.modify_note,
            '5': self.remove_note,
            '6': self.backup,
            '7': self.restore,
            '8': self.quit
        }

    def display_menu(self):
        print("""
        Notebook menu:
        1. Show notes
        2. Search notes
        3. Add a note
        4. Modify a note
        5. Remove a note
        6. Save notes localy
        7. Load local saved notes
        6. Quit
        """)

    def run(self):
        while True:
            self.display_menu()
            choice = input('Enter an option: ')
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f'{choice} is not valid.')

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.note_list
        for note in notes:
            print(note.last_id, note.tags, note.memo,
                  '\n-----------------------')

    def search_notes(self):
        filter = input('Search for: ')
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        memo = input("Enter a memo: ")
        self.notebook.add_note(memo)
        print('Your note has benn added.')

    def modify_note(self):
        id = input('Enter a note id: ')
        memo = input('Enter a memo: ')
        tags = input('Eneter a tags: ')
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def remove_note(self):
        id = input('Enter a note id: ')
        self.notebook.remove_note(id)
        print('Your note has been deleted.')

    def restore(self):
        if not os.path.isdir('notes'):
            print('No backups found.')
        else:
            local_files = glob.glob('notes/*_note.json')
            for each in local_files:
                with open(each, 'r') as file:
                    note = json.load(file)
                    self.notebook.recover_note(note)

    def backup(self):
        if not os.path.isdir('notes'):
            os.makedirs('notes')
        notes = self.notebook.note_list
        for each in notes:
            with open(f'notes/{each.last_id}_{each.date}_note.json', 'w') as file:
                print(vars(each))
                json.dump(vars(each), file)

    def quit(self):
        print('Thanks for using notebook')
        sys.exit(0)


if __name__ == '__main__':
    Menu().run()

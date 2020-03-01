import datetime

last_id = 0


class Notebook:
    def __init__(self):
        self.note_list = []

    def add_note(self, memo, tags=''):
        self.note_list.append(Note(memo, tags))

    def _find_note(self, id):
        for note in self.note_list:
            if note.last_id == int(id):
                return note

    def search(self, filter):
        return [x for x in self.note_list if x.match(filter)]

    def modify_memo(self, id, memo):
        self._find_note(id).memo = memo

    def modify_tags(self, id, tags):
        self._find_note(id).tags = tags

    def remove_note(self, id):
        self.note_list.remove(self._find_note(id))

    def recover_note(self, note):
        self.note_list.append(Note(note.get('memo'),
                                   note.get('tags'),
                                   note.get('date'),
                                   note.get('last_id')))


class Note:

    def __init__(self, memo, tags, date=None, id=None):
        self.memo = memo
        self.tags = tags
        now = datetime.datetime.now()
        if date and id:
            self.date = date
            self.last_id = id
        else:
            self.date = now.strftime("%Y-%m-%d-%H:%M")
            global last_id
            self.last_id = last_id
            last_id += 1

    def match(self, filter):
        return filter in self.tags or filter in self.memo

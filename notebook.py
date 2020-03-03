import datetime

last_id = 0


class Notebook:
    def __init__(self):
        """
        An initiaton of class attributes.
        """
        self.note_list = []

    def add_note(self, memo, tags=''):
        """
        (str,str) -> None
        Adds notes to Note object.
        """
        self.note_list.append(Note(memo, tags))

    def _find_note(self, id):
        """
        (str) -> Note()
        An internal method to search for a note by id.
        """
        for note in self.note_list:
            if note.last_id == int(id):
                return note

    def search(self, filter):
        """
        (str) -> Note()
        Finds notes by specific filter.
        """
        return [x for x in self.note_list if x.match(filter)]

    def modify_memo(self, id, memo):
        """
        (str, str) -> None
        Modifies a Note object memo property.
        """
        self._find_note(id).memo = memo

    def modify_tags(self, id, tags):
        """
        (str, str) -> None
        Modifies a Note object tags property.
        """
        self._find_note(id).tags = tags

    def remove_note(self, id):
        """
        (str) -> None
        Removes a Note obect from note_list property of Notebook object.
        """
        self.note_list.remove(self._find_note(id))

    def recover_note(self, note):
        """
        (dict) -> None
        Recovers a Note object from dictionary
        """
        self.note_list.append(Note(note.get('memo'),
                                   note.get('tags'),
                                   note.get('date'),
                                   note.get('last_id')))


class Note:

    def __init__(self, memo, tags, date=None, id=None):
        """
        (str, str, str, int) -> None
        An initiaton of object attributes.
        """
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
        """
        (str) -> Note()
        Returns a note corespondig to inserted filter.
        """
        return filter in self.tags or filter in self.memo

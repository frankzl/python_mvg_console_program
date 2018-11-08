import os

def get_content(read_file):
    recents_file_path = os.path.join(os.getcwd(), read_file)
    with open(recents_file_path, "r") as recent:
        return toList(recent.read())
    return []


def toList( text ):
    return text.split("\n")


class HistoryManager:

    RECENT_FILE = "recent.txt"

    def get_entry( self, idx ):
        return get_content(self.RECENT_FILE)[idx]
    
    def get_latest(self):
        return self.get_entry(0)

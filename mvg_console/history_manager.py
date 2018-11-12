import os

def get_content(recents_file_path):
    if os.path.isfile(recents_file_path):
        with open(recents_file_path, "r") as recent:
            return toList(recent.read())
    return []


def toList( text ):
    ls = text.split("\n")
    return list(filter( ("").__ne__, ls ))


class HistoryManager:

    RECENT_FILE = "recent.txt"

    def __init__(self, recents_file_path):
        self.recents_file_path = recents_file_path

    def get_entry( self, idx ):
        departure_list = get_content(self.recents_file_path)
        if not departure_list:
            return None
        else:
            return departure_list[idx]

    def get_all(self):
        return get_content(self.recents_file_path)
    
    def get_top( self, limit ):
        return self.get_all()[:limit]
    
    def get_latest(self):
        latest = self.get_entry(0)
        if latest is not None:
            return True, self.get_entry(0)
        return False, 'No Recent Station searches.'

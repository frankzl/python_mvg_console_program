import os

def get_content(read_file):
    recents_file_path = os.path.join(os.getcwd(), read_file)
    with open(recents_file_path, "r") as recent:
        return toList(recent.read())
    return []


def toList( text ):
    ls = text.split("\n")
    return list(filter( ("").__ne__, ls ))


class HistoryManager:

    RECENT_FILE = "recent.txt"

    def get_entry( self, idx ):
        departure_list = get_content(self.RECENT_FILE)
        if not departure_list:
            return None
        else:
            return departure_list[idx]

    def get_all(self):
        return get_content(self.RECENT_FILE)
    
    def get_top( self, limit ):
        return self.get_all()[:limit]
    
    def get_latest(self):
        return self.get_entry(0)

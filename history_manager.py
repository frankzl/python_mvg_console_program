import os

RECENT_FILE = "recent.txt"

def get_content( read_file=RECENT_FILE ):
    recents_file_path = os.path.join(os.getcwd(), read_file)
    with open(recents_file_path, "r") as recent:
        return recent.read()

    return "lol"


# content = (get_content())

from pathlib import Path


def check_path(path_string):
    if not path_string:
        return False
    path = Path(path_string)
    return path.exists()


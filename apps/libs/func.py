from pathlib import Path


def cur_abs_path(name):
    p = Path(name)
    if p.is_dir():
        return str(p.absolute())
    elif p.is_file():
        return str(p.parent.absolute())
    else:
        raise FileExistsError(name)
import re
import sys
import pkgutil
from pathlib import Path


def import_string(import_name):
    if import_name not in sys.modules:
        __import__(import_name)
    return sys.modules[import_name]


def find_modules_vars(root, var):
    module = import_string(root)
    path = getattr(module, '__path__', None)
    if path is None:
        raise ValueError('%r is not a package' % root)
    basename = module.__name__ + '.'
    res = []
    # 非递归find
    for importer, modname, ispkg in pkgutil.iter_modules(path):
        modname = basename + modname
        if ispkg:
            mod = import_string(modname)
            if hasattr(mod, var):
                res.append((mod, getattr(mod, var)))
    return res


def cur_abs_path(name):
    p = Path(name)
    if p.is_dir():
        return str(p.absolute())
    elif p.is_file():
        return str(p.parent.absolute())
    else:
        raise FileExistsError(name)

try:
    from .c.c_pyzstd import *
except ImportError:
    try:
        from .cffi.cffi_pyzstd import *
    except ImportError:
        msg = ("pyzstd module: Neither C implementation nor CFFI "
               "implementation can be imported.")
        raise ImportError(msg)

__version__ = '0.14.4'

__doc__ = '''\
Python bindings to Zstandard (zstd) compression library, the API is similar to
Python's bz2/lzma/zlib module.

Documentation: https://pyzstd.readthedocs.io
GitHub: https://github.com/animalize/pyzstd
PyPI: https://pypi.org/project/pyzstd'''
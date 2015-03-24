import pkg_resources

from static.apps import (
    BaseMagic,
    cling_wrap,
    Cling,
    MagicError,
    MoustacheMagic,
    Shock,
    StatusApp,
    StringMagic)


version_file = pkg_resources.resource_filename(__name__, 'VERSION')
with open(version_file) as vf:
    __version__ = vf.read()
del version_file


__all__ = ['__version__',
           'BaseMagic',
           'cling_wrap',
           'Cling',
           'MagicError',
           'MoustacheMagic',
           'Shock',
           'StatusApp',
           'StringMagic']

import py_generic_utils.timedelta_py26_patch
from datetime import timedelta

t = timedelta(days=1)
print t.total_seconds()

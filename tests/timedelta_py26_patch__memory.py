import gc
import resource
from datetime import timedelta


if __name__=='__main__':
    COUNT = 1000000
    init = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    without_patch = 0
    x = [timedelta(days=10) for i in xrange(COUNT)]
    without_patch = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    del x
    gc.collect()


    import py_generic_utils.timedelta_py26_patch
    with_patch = 0
    x1 = [timedelta(days=10) for i in xrange(COUNT)]
    with_patch = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    del x1
    gc.collect()


    print "initial: %d\nwithout_patch: %d\nwith_patch: %d\n" % \
        (init, without_patch, with_patch)
    print "difference: %d - not so much" % (with_patch-without_patch)

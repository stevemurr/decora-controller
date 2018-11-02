import time


def get_timestring():
    t = time.gmtime(time.time())
    return "[{0}-{1}-{2} {3}:{4}:{5}]".format(t[0], t[1], t[2], t[3], t[4], t[5])

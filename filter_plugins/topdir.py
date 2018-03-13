def topdir(dir):
    return dir.split('/')[0]


class FilterModule(object):
    def filters(self):
        return {'topdir': topdir}

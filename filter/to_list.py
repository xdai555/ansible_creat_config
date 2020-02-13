
def to_list(a):
    lis = a.split(',')
    return lis

class FilterModule(object):
    def filters(self):
        return {
            'to_list': to_list
            }


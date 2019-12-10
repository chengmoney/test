class SetInfo(object):
    def __init__(self, set):
        self.set = set

    def add_setinfo(self, item):
        self.set.add(item)

    def get_intersection(self, set):
        new_set = self.set.intersection(set)
        return new_set

    def get_union(self, set):
        new_set = self.set.union(set)
        return new_set

    def get_difference(self, set):
        new_set = self.set.difference(set)
        return new_set


st = set([x for x in range(0, 10)])
new_st = SetInfo(st)
new_st.add_setinfo(10)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


    def __repr__(self):
        if self:
            return "{} - {}".format(self.val, self.next)

class DogAttributes:

    count = 0
    day = 0

    def __init__(self, day):
        self.count += 1
        self.day = day
        print "The day is %d" % self.day

    def bart(self):
        print "The dog is Barting"
        self.count += 1
        print "The Count is %d" % self.count

    def chewing(self):
        print "The dog is chewing"
        self.count += 1
        print "The Count is %d" % self.count


obj = DogAttributes(7)

obj.bart()
obj.bart()
obj.chewing()
obj.bart()





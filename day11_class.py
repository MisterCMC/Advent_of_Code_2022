import queue as q
class Monkey:

    def __init__(self, name):
        self.name = name
        self.item_list = q.Queue()
        self.op = None
        self.op_num = None
        self.tester = None
        self.passed = None
        self.failed = None
        self.inspections = 0
    
    def get_name(self):
        return self.name

    def queue_item(self,item):
        self.item_list.put(item)
    
    def get_queue(self):
        return list(self.item_list.queue)

    def queue_size(self):
        return self.item_list.qsize()

    def get_item(self):
        return self.item_list.get()

    def set_operation(self, op, number):
        self.op = op
        if number == 'old':
            self.op_num = 'old'
        else:
            self.op_num = int(number)
    
    def operate(self, worry):
        self.inspections += 1
        operator = {
            '+': lambda x, y: x + y,
            '*': lambda x, y: x * y
            }
        if self.op_num == 'old':
            return operator[self.op] (worry, worry)
        else:
            return operator[self.op] (worry, self.op_num)     

    def set_test(self, number, pass_num, fail_num):
        self.tester = number
        self.passed = pass_num
        self.failed = fail_num
    
    def testing(self, worry):
        if worry % self.tester == 0:
            new_monk = 'Monkey' + self.passed
            return new_monk.replace(' ', '')
        else:
            new_monk = 'Monkey' + self.failed
            return new_monk.replace(' ', '')
    
    def get_inspections(self):
        return self.inspections    

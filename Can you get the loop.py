class Node(object): ##Класс определяем NODE а так же меотды для него

    def __init__(self, next_node=None):
        self.next_node = next_node

   ##Свойства для объекта
    def next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next
        return new_next

def loop_size(node):
    onestep = node
    twostep = node.next
    while(onestep != twostep):
        twostep = twostep.next.next
        onestep = onestep.next
    onestep = onestep.next
    size = 1
    while(onestep != twostep):
        size += 1
        onestep = onestep.next
    return size

def test_ll(tail, loop):
    head = Node()
    nodes = [head]
    for i in range(2, tail+loop+1):
        head = head.set_next(Node())
        nodes.append(head)
    nodes[-1].set_next(nodes[tail])
    size = loop_size(nodes[0])
    print ("Tail: {}, Loop: {}, Size: {}".format(tail, loop, size))


'''
def loop_size(node):
    turtle, rabbit = node.next, node.next.next

    # Find a point in the loop.  Any point will do!
    # Since the rabbit moves faster than the turtle
    # and the kata guarantees a loop, the rabbit will
    # eventually catch up with the turtle.
    while turtle != rabbit:
        turtle = turtle.next
        rabbit = rabbit.next.next

    # The turtle and rabbit are now on the same node,
    # but we know that node is in a loop.  So now we
    # keep the turtle motionless and move the rabbit
    # until it finds the turtle again, counting the
    # nodes the rabbit visits in the mean time.
    count = 1
    rabbit = rabbit.next
    while turtle != rabbit:
        count += 1
        rabbit = rabbit.next

    # voila
    return count  '''
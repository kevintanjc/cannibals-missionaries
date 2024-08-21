def mnc_tree_search(m: int, c: int):
    class Node:

        def __init__(self, cl: int, ml: int, cr: int, mr: int, car: str, parent):
            self.cl = cl # Spies on left side
            self.ml = ml # Targets on left side
            self.cr = cr # Spies on right side
            self.mr = mr # Targets on right side
            self.car = car # Car on Left or Right
            self.parent = parent

        def solved(self):
            return self.cl == c and self.ml == m and self.cr == 0 and self.mr == 0 and self.car == "left"
    
    def getCarValues(child: Node, parent: Node):
        mOnCar = abs(child.mr - parent.mr)
        cOnCar = abs(child.cr - parent.cr)
        move = (mOnCar, cOnCar)
        return move
    
    def getNextState(node: Node):
        possibleCarCombinations = []
        output = []

        if node.Car == "left":
            for i in range(node.ml + 1):
                for j in range(node.cl + 1):
                    #Car must have at most 2 people and at least 1 person
                    if i + j <= 2 and i + j > 0:
                        possibleCarCombinations.append((i, j))
            for k in range(len(possibleCarCombinations)):
                #check to ensure invariant constraint is satisfied
                nextML = node.ml - possibleCarCombinations[k][0]
                nextCL = node.cl - possibleCarCombinations[k][1]
                nextMR = node.mr + possibleCarCombinations[k][0]
                nextCR = node.cr + possibleCarCombinations[k][1]
                if (nextML >= nextCL or nextML == 0) and (nextMR >= nextCR or nextMR == 0):
                    output.append(Node(nextCL, nextML, nextCR, nextMR, "right", node))
        else:
            for i in range(node.mr + 1):
                for j in range(node.cr + 1):
                    #car must have at most 2 people and at least 1 person
                    if i + j <= 2 and i + j > 0:
                        possibleCarCombinations.append((i, j))
            for k in range(len(possibleCarCombinations)):
                #check to ensure invariant constraint is satisfied
                nextML = node.ml + possibleCarCombinations[k][0]
                nextCL = node.cl + possibleCarCombinations[k][1]
                nextMR = node.mr - possibleCarCombinations[k][0]
                nextCR = node.cr - possibleCarCombinations[k][1]
                if (nextML >= nextCL or nextML == 0) and (nextMR >= nextCR or nextMR == 0):
                    output.append(Node(nextCL, nextML, nextCR, nextMR, "left", node))
        
        return output


        

    
    #if more spies than targets and that number of targets is non-zero
    if c > m and m != 0:
        return ()
    
    #Everyone starts on the right side
    root = Node(0, 0, c, m, "right", None)

    #Breadth First Search implementation
    queue = []
    queue.append(root)

    while len(queue) != 0:
        
        # First In, First Out
        state = queue.pop(0)

        if state.solved():
            path = []
            node = state
            while node != root:
                move = getCarValues(node, node.parent)
                path.insert(0, move)
                node = node.parent
            return tuple(path)
        
        else:
            nextStates = getNextState(state)
            queue.extend(nextStates)
    
    return ()

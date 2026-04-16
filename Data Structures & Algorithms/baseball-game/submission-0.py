class Solution:
    def calPoints(self, operations: List[str]) -> int:
        operation = []
        for i in range(len(operations)):
            if operations[i] == 'C':
                operation.pop()
            elif operations[i] == 'D':
                operation.append(2*operation[-1])
            elif operations[i] == '+':
                operation.append(operation[-2]+operation[-1])
            else:
                operation.append(int(operations[i]))

        sums = 0
        for j in operation:
            sums = sums + j
        return sums
                

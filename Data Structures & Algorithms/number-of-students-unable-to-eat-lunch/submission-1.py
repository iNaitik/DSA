class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        hashmap = {}
        res = len(students)
        for i in students:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        for i in sandwiches:
            if i in hashmap and hashmap[i] > 0:
                res -= 1
                hashmap[i] -= 1
            else:
                return res
        return res
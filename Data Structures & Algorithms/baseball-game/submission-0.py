class Solution:
    def calPoints(self, operations: List[str]) -> int:
        point = 0
        point_list = []
        for op in operations:
            if op == "+":
                if len(point_list) >= 2:
                    point_list.append(point_list[-1]+point_list[-2])
                elif len(point_list) == 1:
                    point_list.append(point_list[0])
                else:
                    point_list.append(0)
            elif op == "C":
                point_list = point_list[0:len(point_list)-1]
            elif op == "D":
                point_list.append(point_list[-1]*2)
            else:
                point_list.append(int(op))
        print(point_list)
        for p in point_list:
            point += p
        return point
        
class Vertex:
    def __init__(self, name):
        self.name = name


graph = {
    # 有向无环图
    # 'A': ['B', 'C'],
    # 'B': ['E'],
    # 'C': ['D'],
    # 'D': ['B'],
    # 'E': [],

    # 有向有环图
    # 'A': ['B'],
    # 'B': ['D', 'E'],
    # 'C': ['A'],
    # 'D': ['C'],
    # 'E': [],

    'A': ['B', 'C', 'D'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['C', 'F', 'G'],
    'E': ['D', 'G'],
    'F': [],
    'G': ['F']
}


def top_sort():
    '''
    简单的拓扑排序
    :return: 打印节点名和顺序
    '''
    for counter in range(0, len(graph)):
        # 查找入度为0的顶点
        v = findNewVertexOfIndegreeZero()
        # 如果查找不到，说明存在环
        if v is None:
            raise Exception('存在环')
        print('{}的顺序是{}'.format(v, counter))
        # 删除该顶点以及其边
        del graph[v]


def findNewVertexOfIndegreeZero():
    '''
    查找入度为0的节点
    :return:
    '''
    # 外层循环，遍历所有的节点
    for v in graph.keys():
        # 内层循环，遍历每个节点的邻接节点列表
        for l in graph.values():
            # 如果发现当前节点出现在某节点的邻接列表里，说明它的入度不为0，跳出循环
            if v in l:
                break
        # 如果未出现在所有的邻接列表里，则说明入度为0，return它
        else:
            return v


def top_sort2():
    # 将所有的节点入度初始化为0
    in_degrees = dict((u, 0) for u in graph.keys())
    # 计算所有节点的入度，访问所有顶点的邻接表，出现的次数就是入度
    for v in graph.keys():
        for w in graph[v]:
            in_degrees[w] += 1
    # 筛选入度为0的顶点
    q = [u for u in in_degrees if in_degrees[u] == 0]
    seq = []
    #使用列表的append和pop实现栈，保存入度为0的顶点
    while q:
        u = q.pop()
        seq.append(u)
        # 获取与u邻接的顶点并将其入度-1
        for v in graph[u]:
            in_degrees[v] -= 1
            if in_degrees[v] == 0:
                q.append(v)
    #如果排序后的顶点数和图中的顶点数相同
    if len(seq) == len(in_degrees):
        print(seq)
        return seq
    else:
        return None



if __name__ == '__main__':
    # top_sort()
    # top_sort2()
    q = []
    q.append(1)
    q.append(2)
    q.append(3)
    print(q)
    a = q.pop()
    print(a)
    print(q)
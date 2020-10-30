from optical.utils import data2neo4j


class CreateGraph:
    # 该类用于将数据绘制成知识图谱
    def __init__(self):
        self.graph = data2neo4j()



if __name__ == '__main__':
    print(CreateGraph().graph)

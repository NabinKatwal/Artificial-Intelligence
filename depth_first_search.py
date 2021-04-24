class DFS:
    def __init__(self, graph):
        self.graph = graph
        self.visited = []
        self.stack = []
        self.top = -1
        self.bottom = -1

    def push(self, item):
        if -1< self.top <len(self.graph):
            self.stack.append(item)
            self.top+=1
            return self.stack
        else:
            return "Stack overflow"

    def pop(self, item):
        if self.top == -1:
            return "Stack empty"
        else:
            self.stack.remove(self.stack[self.top])
            self.top -= 1
            return "popped"

    def search(self):
        pass

if __name__ == "__main__":
    graph = [0,1,2,3,4]

    dfs = DFS(graph)
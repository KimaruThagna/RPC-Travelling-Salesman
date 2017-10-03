import rpyc
from rpyc.utils.server import ThreadedServer
# It is a directed graph
graph = {'A': ['B', 'C'], 'B': ['C', 'D'], 'C': ['D','A'], 'D': ['C','F'], 'E': ['F'], 'F': ['G','A'],'G':['B','C','E']}


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph.keys():
        return "No path found with the given starting Node"
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph.keys():
        return "No path found with the given starting Node"
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            paths.append(newpaths)
    return paths


class MyService(rpyc.Service):
    def  exposed_line_counter(self,sp,des):
        sp=str(sp)
        des=str(des)
        generalPath=find_path(graph,sp,des)
        all=find_all_paths(graph,sp,des)
        return 'YOUR GENERAL PATH:',generalPath, "ALL AVAILABLE ROUTES:",all

t = ThreadedServer(MyService, port = 7001)# handles each request using a new thread as opposed to handling requests with a new process
t.start()

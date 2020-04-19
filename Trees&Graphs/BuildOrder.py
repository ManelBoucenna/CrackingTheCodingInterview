class ProjectsGraph:
    def __init__(self, projects, dependancies):
        self.projects = projects
        self.dependancies = dependancies
        self.buildOrderList = []
        
    def BuildOrder(self):
        independantNodes = self.getIndependandNodes()
        pass
            
    def getIndependandNodes(self):
        independantNodes = []
        for project in self.projects:
            isIndependant = True
            for dependancy in self.dependancies.values():
                if (project in dependancy):
                    isIndependant = False
            if (isIndependant == True) :
                independantNodes.append(project)
        return independantNodes

projects = ['a','b', 'c', 'd', 'e', 'f']
dependancies = {
    'a': ['d'],
    'b': ['d'],
    'c': [],
    'd': ['c'],
    'e': [],
    'f': ['a','b']
    }

ProjectsGraph(projects, dependancies).BuildOrder()

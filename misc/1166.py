class FileSystem:

    def __init__(self):
        self.paths = defaultdict() 

    def createPath(self, path: str, value: int) -> bool:
        # path validation
        if path == "/" or len(path) == 0 or path in self.paths:
            return False 
        
        # find parent => split paths and exclude file which is the last item 
        directories = path.split('/')
        parent = '/'.join(directories[:-1])
        if len(parent) > 1 and parent not in self.paths:
            return False 
        
        # add new path 
        self.paths[path] = value 
        return True 

    def get(self, path: str) -> int:
        return self.paths.get(path, -1)


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
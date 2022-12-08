class Directory:

    def __init__(self, name):
        self.name = name
        self.total_size = 0
        self.sub_dir = []
        self.files = []

    def add_file(self, file_name, size):
        self.files.append(file_name)
        self.total_size += size

    def add_dir(self, name):
        self.sub_dir.append(name)

    def add_size(self, extra):
        self.total_size += extra

    def get_name(self):
        return self.name

    def get_subdir(self):
        return self.sub_dir

    def get_files(self):
        return self.files

    def get_size(self):
        return self.total_size

class File:

    def __init__(self, name):
        self.name = name
        self.size = 0

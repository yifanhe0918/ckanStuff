class CkanPackage():

    def __init__(self,name,title):
        self.name = name
        self.title = title
        self.tags = ''
        self.owner_org = ''
        self.groups = ''
        self.license_id = ''



class CkanFile():

    def __init__(self,package_id,name,description,format,url):
        self.package_id = package_id
        self.name = name
        self.description = description
        self.format = format
        self.url = url



from extension import api
from apps.libs.func import find_modules_vars


class AddResource():
    def __init__(self, version, prefix):
        self.version = version
        self.prefix = prefix

    def add_resource(self, func, *urls):
        fin_urls = []
        for url in urls:
            url = "/{}/api/{}/{}".format(self.prefix, self.version, url.lstrip('/'))
            fin_urls.append(url)
        api.add_resource(func, *fin_urls)


for mod, resource_map in find_modules_vars(root='apps.api', var='resource_map'):
    for version_var in resource_map:
        resource = AddResource(version=version_var['version'], prefix=version_var['prefix'])
        for func, *urls in version_var['resources']:
            resource.add_resource(func, *urls)
import flask_restful
from apps.libs.func import find_modules_vars

from apps.libs.register_blueprint import NestableBlueprint
blueprint = bp = NestableBlueprint(cur_name=__name__, cur_file=__file__)
api = flask_restful.Api(bp)


class AddResource():
    def __init__(self, version, name):
        self.version = version
        self.name = name

    def add_resource(self, func, *urls):
        fin_urls = set([])
        for url in urls:
            if url.startswith('/api'):
                url = url[4:]

            if url.startswith('/') and url[:2]!='//':
                fin_urls.add(url)
            else:
                if self.name:
                    url = "/{}/{}/{}".format(self.version, self.name, url.lstrip('/'))
                else:
                    url = "/{}/{}".format(self.version, url.lstrip('/'))
            fin_urls.add(url)
        api.add_resource(func, *fin_urls)


for mod, resource_map in find_modules_vars(root='apps.api', var='resource_map'):
    for version_var in resource_map:
        resource = AddResource(version=version_var['version'], name=version_var['name'])
        for cls in version_var['resources']:
            resource.add_resource(cls, *getattr(cls, 'urls', []))


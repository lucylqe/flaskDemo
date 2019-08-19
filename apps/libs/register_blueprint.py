from flask import Blueprint

from apps.libs.func import cur_abs_path


class NestableBlueprint(Blueprint):
    def __init__(self, name=None, import_name=None, static_folder=None,
                 static_url_path=None, template_folder=None,
                 url_prefix=None, subdomain=None, url_defaults=None,
                 root_path=None, cur_name=None, cur_file=None):
        if name is None and cur_name:
            name = cur_name
            if name.startswith('apps'):
                name = name[5:]
        if import_name is None and cur_name:
            import_name = cur_name
        if template_folder is None and cur_file:
            template_folder = cur_abs_path(cur_file).rstrip('/') + '/templates/'

        super(NestableBlueprint, self).__init__(name, import_name,
                                                static_folder, static_url_path,
                                                template_folder, url_prefix, subdomain,
                                                url_defaults, root_path)

    def register_blueprint(self, blueprint, **options):
        def deferred(state):
            url_prefix = (state.url_prefix or u"") + \
                         (options.get('url_prefix', blueprint.url_prefix) or u"")
            if 'url_prefix' in options:
                del options['url_prefix']

            state.app.register_blueprint(blueprint, url_prefix=url_prefix, **options)

        self.record(deferred)
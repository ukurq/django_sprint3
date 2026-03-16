import os
import sys
project_root = r'c:\Users\ukur\Desktop\Yandex_Practicum V2\django_sprint3\blogicum'
if sys.path[0] != project_root:
    if project_root in sys.path:
        sys.path.remove(project_root)
    sys.path.insert(0, project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogicum.settings')
import django
django.setup()
from django.test.utils import setup_test_environment, teardown_test_environment
setup_test_environment()
from django.template import loader
from django.test.signals import template_rendered

def receiver(sender, template, context, **kwargs):
    print('signal', getattr(template, 'name', str(template)), context)

template_rendered.connect(receiver)
content = loader.render_to_string('blog/index.html', {'post_list': []})
print('rendered snippet', content[:120])
template_rendered.disconnect(receiver)
teardown_test_environment()

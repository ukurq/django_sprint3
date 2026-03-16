import os
import sys
print('sys.executable', sys.executable)
project_root = r'c:\Users\ukur\Desktop\Yandex_Practicum V2\django_sprint3\blogicum'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogicum.settings')
if sys.path[0] != project_root:
    if project_root in sys.path:
        sys.path.remove(project_root)
    sys.path.insert(0, project_root)
print('sys.path first 4', sys.path[:4])
print('DJANGO_SETTINGS_MODULE', os.environ.get('DJANGO_SETTINGS_MODULE'))
import importlib.util
spec = importlib.util.find_spec('blogicum.settings')
print('spec', spec)
import django
django.setup()
from django.test import Client
from django.test.signals import template_rendered

c = Client()
events = []

def rec(sender, template, context, **kwargs):
    events.append((template, context))

template_rendered.connect(rec)
r = c.get('/')
template_rendered.disconnect(rec)
_ = r.content
print('status', r.status_code)
print('events', events)
print('content snippet', r.content[:160])
print('templates', getattr(r, 'templates', None))
print('context', getattr(r, 'context', None))
print('type context', type(getattr(r, 'context', None)))
if r.context is not None:
    print('dict:', dict(r.context))
else:
    print('no context')

Static Pages ONI plugin
===

Provides the ability to drop HTML files into a special directory and have ONI
serve them up at an arbitrary URL

Usage
---

Download the repository into the Open ONI's `onisite/plugins` directory as `staticpages`:

    git clone https://github.com/open-oni/plugin_staticpages.git onisite/plugins/staticpages

Add the plugin to your `INSTALLED_APPS` list:

```python
# onisite/settings_local.py

INSTALLED_APPS = (
    'django.contrib.humanize',
    'django.contrib.staticfiles',

    'onisite.plugins.staticpages',
    'themes.default',
    'core',
)

```

And add the plugin's URLs to your urlpatterns.  You can choose any prefix you
like, but we use `static/` below:

```python
# onisite/urls.py

from django.conf.urls import url, include

urlpatterns = [
  url(r'^static/', include("onisite.plugins.staticpages.urls")),

  # keep this last or else urls from core may override custom urls
  url('', include("core.urls")),
]
```

Drop static HTML into staticpages/pages, formatted similarly to [pages/example.html](pages/example.html).

You can add links to any page in your templates with this named path:

```python
<a href="{% url 'static_pages_page' 'example' %}">Example Static Page</a>
```

Settings
---

If you need your HTML files to come from a different location, you can alter
your settings file (`onisite/settings_local.py`) to include a path to the new
location, e.g.:

    STATIC_PAGES_PATH="/opt/openoni/themes/oregon/staticpages"

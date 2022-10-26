from django.apps import apps
from django.conf import settings
from model_mommy import mommy


for app in settings.INSTALLED_APPS:
    try:
        app_models = apps.get_app_config(app).get_models()
    except:
        continue
    for model in app_models:
        try:
            mommy.make(model, _quantity=100)
        except:
            print('error')
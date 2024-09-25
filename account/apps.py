from importlib import import_module

from django.apps import AppConfig
from django.utils.module_loading import module_has_submodule

MODELS_MODULE_NAME = "models"
MODELS_MODULE_LAYER = "domain"


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "account"

    def import_models(self) -> None:
        # Dictionary of models for this app, primarily maintained in the
        # 'all_models' attribute of the Apps this AppConfig is attached to.
        self.models = self.apps.all_models[self.label]  # type: ignore

        if module_has_submodule(self.module, MODELS_MODULE_LAYER):
            models_module_name = "%s.%s.%s" % (
                self.name,
                MODELS_MODULE_LAYER,
                MODELS_MODULE_NAME,
            )
            self.models_module = import_module(models_module_name)

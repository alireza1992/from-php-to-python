import importlib
import pkgutil
import infrastructure.models as models_package

for _, module_name, _ in pkgutil.iter_modules(models_package.__path__):
    importlib.import_module(f"infrastructure.models.{module_name}")
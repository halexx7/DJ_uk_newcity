import json
import os

from django.conf import settings
from django.core.management import BaseCommand

from apps.authnapp.admin import UserResource, GroupResource, PermissionResource
from apps.directory.admin import (AppartamentResource, CityResource, HouseResource, MetricsResource, 
                             PostNewsResource, PrivilegesResource, ServicesResource, 
                             ServicesCategoryResource, StreetResource, SubsidiesResource, UserProfileResource)
from apps.mainapp.admin import (AverageСalculationBufferResource, ConstantPaymentsResource, CurrentCounterResource,
                           HeaderDataResource, HistoryCounterResource, HouseCurrentResource, HouseHistoryResource,
                           MainBookResource, PaymentOrderResource, PersonalAccountStatusResource, RecalculationsResource,
                           StandartResource, VariablePaymentsResource)
from apps.personalacc.admin import SiteConfigurationResource


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-m', '--models', nargs='+', type=str, default=[])

    def handle(self, *args, **options):
        resource = [CityResource, UserResource, AppartamentResource, UserProfileResource, GroupResource, PermissionResource]
        resource += [HouseResource, MetricsResource, PostNewsResource, PrivilegesResource, ServicesResource]
        resource += [ServicesCategoryResource, StreetResource, SubsidiesResource]
        
        resource += [AverageСalculationBufferResource, ConstantPaymentsResource, CurrentCounterResource]
        resource += [HeaderDataResource, HistoryCounterResource, HouseCurrentResource, HouseHistoryResource]
        resource += [MainBookResource, PaymentOrderResource, PersonalAccountStatusResource, RecalculationsResource]
        resource += [StandartResource, VariablePaymentsResource, SiteConfigurationResource]

        for i in resource:
            self.export_model(i, options)

    @staticmethod
    def export_model(resource_class, options):
        assert resource_class.__name__[-8:] == 'Resource'
        name = resource_class.__name__[:-8]
        full_file_name = os.path.join(settings.BASE_DIR, 'apps', 'mainapp', 'management', 'json', f'{name}.json')
        if options.get('models') and name.lower() not in options.get('models', []):
            return

        dataset = resource_class().export()
        data = json.loads(dataset.json)
        print(f'export {name}... ', end='', flush=True)
        with open(full_file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print('OK', f'exported {len(data)} rows')

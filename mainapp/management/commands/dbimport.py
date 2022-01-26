import json
import os

import tablib
from django.conf import settings
from django.core.management import BaseCommand
from import_export import resources

from django.contrib.auth.models import Group, Permission
from authnapp.models import User
from directory.models import (Appartament, City, House, Metrics, PostNews, Privileges, Services,
                              ServicesCategory, Street, Subsidies, UserProfile)
from mainapp.models import (AverageСalculationBuffer, ConstantPayments, CurrentCounter, HeaderData,
                            HistoryCounter, HouseCurrent, HouseHistory, MainBook, PaymentOrder,
                            PersonalAccountStatus, Recalculations, Standart, VariablePayments)
from personalacc.models import SiteConfiguration


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-m', '--models', nargs='+', type=str, default=[])

    def handle(self, *args, **options):
        models = [Group, Permission, User, PostNews, Metrics, ServicesCategory, Services]
        models += [City, Street, House, UserProfile, Appartament]
        models += [Subsidies,  Privileges]
        
        models += [HouseCurrent, HouseHistory, Standart, CurrentCounter, HistoryCounter,  Recalculations]
        models += [ConstantPayments, VariablePayments, HeaderData, MainBook, PaymentOrder]
        models += [PersonalAccountStatus, AverageСalculationBuffer]
        
        models += [SiteConfiguration]

        for i in models:
            self.import_model(i, options)

    @staticmethod
    def import_model(model, options):
        name = model.__name__
        full_file_name = os.path.join(settings.BASE_DIR, 'mainapp', 'management', 'json', f'{name}.json')
        if options.get('models') and name.lower() not in options.get('models', []):
            return

        print(f'import {name}... ', end='', flush=True)
        with open(full_file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for i in data:
                resource = resources.modelresource_factory(model=model)()
                dataset = tablib.Dataset(list(i.values()), headers=list(i.keys()))
                result = resource.import_data(dataset, dry_run=True)
                if not result.has_errors():
                    resource.import_data(dataset, dry_run=False)
                else:
                    print(f'error import model: {name}')
                    return
            print('OK', f'exported {len(data)} rows')

        if model.__name__ == User.__name__:
            for user in User.objects.all():
                user.set_password('1')
                user.save()

from newcity.celery import app
from .views import starter, get_last_date
from datetime import timezone


@app.task()
def invoice_simulation():
    # print(get_last_date())
    if timezone.now().day == get_last_date():
        starter()

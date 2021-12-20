import os
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE','project_one.settings')

import django
django.setup()

from app_one.models import Topic, web, AccessRecord
from faker import Faker

fakegen =Faker( )
topics =['social', 'news', 'games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics) )[0]
    t.save()
    return t 

def populate(N=2):
    for entry in range(N):
        top = add_topic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fakename = fakegen.company()

        webpage = web.objects.get_or_create(topic= top , url= fake_url, name= fakename)[0]
        acc_rec = AccessRecord.objects.get_or_create(name=webpage, date= fake_date)[0]

if __name__ == "__main__":
    print("populating script!")
    populate(20)
    print("completed!!")



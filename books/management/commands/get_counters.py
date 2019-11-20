from django.core.management.base import BaseCommand, CommandError
from django_redis import get_redis_connection

# https://docs.djangoproject.com/en/2.2/howto/custom-management-commands/

class Command(BaseCommand):
    help = "Getting counters from site"

    def handle(self, *args, **kwargs):
        con = get_redis_connection()
        keys = con.keys()

        print("Counters:")
        for k in keys:
            print(f"{k.decode()}: {con.get(k).decode()}") # has to decode, because initially it returns a binary format (b'SOME_DATA')
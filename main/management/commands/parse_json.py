from django.core.management.base import BaseCommand, CommandError
from parser.parser import parse


class Command(BaseCommand):
    def handle(self, *args, **options):
        parse()
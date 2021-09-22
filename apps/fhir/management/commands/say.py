from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Simple say command"

    def add_arguments(self, parser):
        parser.add_argument('word', nargs='+', type=str)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS(f"You said: {options['word']}"))

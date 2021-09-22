from django.core.management.commands.makemigrations import Command as BaseMigrateCommand

class Command(BaseMigrateCommand):
    help = "Generates migration files"

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING(f"Start generating migrations..."))
        super(Command, self).handle(*args, **options)
        self.stdout.write(self.style.SUCCESS(f"makemigrations task is completed!!!"))

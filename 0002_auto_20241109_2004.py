# Generated by Django 5.1.2 on 2024-11-09 10:34

from django.db import migrations

def populate_status(apps, schemaeditor):
    entries = {
        "published": "Apost for all to see",
        "draft": "Apost only visible to the author",
        "archived": "Older posts"
    }
    Status = apps.get_model("posts", "Status")
    for key, value in entries.items():
        status = Status(name=key, description=value)
        status.save()

class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_status)
    ]

# Generated by Django 3.2.3 on 2021-05-24 08:15

from django.db import migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='deck_object',
            field=picklefield.fields.PickledObjectField(blank=True, editable=False, null=True),
        ),
    ]

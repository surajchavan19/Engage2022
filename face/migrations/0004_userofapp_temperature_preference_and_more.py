# Generated by Django 4.0.4 on 2022-05-29 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0003_alter_userofapp_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userofapp',
            name='temperature_preference',
            field=models.CharField(default='22', max_length=500),
        ),
        migrations.AlterField(
            model_name='userofapp',
            name='photo',
            field=models.CharField(default='face_db/12selfie.png', max_length=500),
        ),
        migrations.AlterField(
            model_name='userofapp',
            name='spotify_uid',
            field=models.CharField(default='joab4qf54hmmc19t23jmj7i1h', max_length=500),
        ),
    ]

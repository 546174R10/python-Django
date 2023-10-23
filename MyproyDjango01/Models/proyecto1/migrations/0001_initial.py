
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='proyecto1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=75)),
                ('apellido', models.CharField(max_length=75)),
                ('telefono', models.CharField(max_length=75)),
                ('fecha_nacimiento', models.DateField()),
                ('codigo', models.IntegerField()),
            ],
        ),
    ]

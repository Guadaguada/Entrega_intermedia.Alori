# Generated by Django 4.1.3 on 2022-12-03 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBiblioteca', '0002_afiliado_retiro_libro_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='afiliado',
            name='apellido',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='retiros',
            name='fechaRetiro',
            field=models.DateField(auto_now=True),
        ),
    ]
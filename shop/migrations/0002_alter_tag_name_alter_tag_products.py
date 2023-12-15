from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Тег'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='products',
            field=models.ManyToManyField(related_name='tags', to='shop.product'),
        ),
    ]

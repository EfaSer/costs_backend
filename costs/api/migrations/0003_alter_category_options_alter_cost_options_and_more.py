# Generated by Django 4.2.5 on 2023-10-03 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_alter_category_options_alter_cost_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Категорию", "verbose_name_plural": "Категории"},
        ),
        migrations.AlterModelOptions(
            name="cost",
            options={"verbose_name": "Расход", "verbose_name_plural": "Расходы"},
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=30, verbose_name="Название категории"),
        ),
        migrations.AlterField(
            model_name="cost",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="category",
                to="api.category",
                verbose_name="Категория",
            ),
        ),
        migrations.AlterField(
            model_name="cost",
            name="date",
            field=models.DateField(verbose_name="Дата"),
        ),
    ]

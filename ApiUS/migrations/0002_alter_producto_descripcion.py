from django.db import migrations, models

class Migration(migrations.Migration):
    
    dependencies = [
        ('ApiUS', '0001_initial'),
    ]
    operations = [
        migrations.AlterField(
            model_name = 'Producto',
            name = 'descripcion',
            field = models.TextField(),
            ),
    ]
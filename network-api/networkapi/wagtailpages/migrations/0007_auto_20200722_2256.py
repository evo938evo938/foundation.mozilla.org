# Generated by Django 2.2.14 on 2020-07-22 22:56

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('wagtailpages', '0006_homepagenewsyoucanuse'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='spotlight_headline',
            field=models.CharField(blank=True, help_text='Spotlight headline', max_length=140),
        ),
        migrations.AddField(
            model_name='homepage',
            name='spotlight_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='spotlight_image', to='wagtailimages.Image'),
        ),
        migrations.CreateModel(
            name='HomepageSpotlightPosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailpages.BlogPage')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='spotlight_posts', to='wagtailpages.Homepage')),
            ],
            options={
                'verbose_name': 'blog',
                'verbose_name_plural': 'blogs',
                'ordering': ['sort_order'],
            },
        ),
    ]

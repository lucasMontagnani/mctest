# Generated by Django 3.1.4 on 2020-12-18 18:44

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_text', models.CharField(help_text='Tip: Include a prefix in the topic, such as discipline code.', max_length=50, verbose_name='Topic')),
                ('topic_description', models.TextField(blank=True, default='', max_length=200, verbose_name='Description')),
                ('discipline', models.ManyToManyField(help_text='Choose a discipline for this topic.', related_name='topics2', to='course.Discipline', verbose_name='Disciplines')),
            ],
            options={
                'ordering': ['discipline__discipline_code', 'topic_text'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_group', models.CharField(blank=True, default='', help_text='Only one question per group will be sorted for each exam (student)', max_length=50, verbose_name='Question Group')),
                ('question_short_description', models.CharField(help_text='Enter a short description', max_length=50, verbose_name='Short Description')),
                ('question_text', models.TextField(blank=True, default='', help_text='Accepts LaTeX description and parameterization using the Python language (see publications).', verbose_name='Description')),
                ('question_type', models.CharField(choices=[('QM', 'Multiple-Choice Question'), ('QT', 'Text Question')], default='', max_length=2, verbose_name='Type')),
                ('question_difficulty', models.CharField(choices=[('1', 'Very easy level question'), ('2', 'Easy level question'), ('3', 'Mid-level question'), ('4', 'Difficult level question'), ('5', 'Very Difficult level question')], default='', max_length=2, verbose_name='Difficulty')),
                ('question_bloom_taxonomy', models.CharField(choices=[('remember', 'remember: recognizing, recalling'), ('understand', 'understand: interpreting, exemplifying, classifying, comparing'), ('apply', 'apply: executing, implementing'), ('analyze', 'analyze: differentiating, organizing, attibuting'), ('evaluate', 'evaluate: checking, critiquing'), ('create', 'create: generating, planning, producing')], default='', max_length=10, verbose_name='Bloom Taxonomy')),
                ('question_parametric', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', help_text='Question with some randomly chosen values', max_length=3, verbose_name='Parametric question')),
                ('question_last_update', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Last Update')),
                ('question_who_created', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Who Created')),
                ('topic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions2', to='topic.topic', verbose_name='Topic')),
            ],
            options={
                'ordering': ['topic__discipline__discipline_code', 'topic__topic_text', 'question_type', 'question_difficulty', 'question_group', 'question_short_description'],
                'permissions': (('can_mark_update', 'Set question as validated'),),
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField(default='', max_length=200, verbose_name='Answer Text')),
                ('answer_feedback', models.TextField(blank=True, default='', max_length=200, verbose_name='Answer Feedback')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers2', to='topic.question')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]

# Generated by Django 3.1.4 on 2020-12-18 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(help_text='Course name - does not include the institute code', max_length=100, verbose_name='Course name')),
                ('course_code', models.CharField(max_length=20, verbose_name='Course code')),
                ('course_coords', models.ManyToManyField(blank=True, related_name='course2', to=settings.AUTH_USER_MODEL, verbose_name='Course coordinators')),
                ('course_profs', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Course professors')),
            ],
            options={
                'ordering': ['institutes__institute_code', 'course_name'],
            },
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute_name', models.CharField(max_length=50, verbose_name='Institute name')),
                ('institute_code', models.CharField(max_length=20, verbose_name='Institute code')),
                ('institute_logo', models.CharField(max_length=20, verbose_name='Institute logo')),
                ('institute_url', models.CharField(help_text='All teachers must register institutional email', max_length=20, verbose_name='Institute url')),
                ('institute_exams_generated', models.IntegerField(default=0, help_text='Total of exams generated per student. Remember, when creating an exam, it can be applied across multiple classrooms and to multiple students.', verbose_name='Exams generated by the Institute')),
                ('institute_exams_corrected', models.IntegerField(default=0, help_text='Total of corrected exams. Remember, some students may be absent.', verbose_name='Exams corrected by the Institute')),
                ('institute_questions_corrected', models.IntegerField(default=0, help_text='Total of corrected question.', verbose_name='Questions corrected by the Institute')),
                ('institute_coords', models.ManyToManyField(blank=True, related_name='institute2', to=settings.AUTH_USER_MODEL, verbose_name='Institute coordinators')),
                ('institute_profs', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Institute professors')),
            ],
            options={
                'ordering': ['institute_code', 'institute_name'],
            },
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discipline_name', models.CharField(max_length=100, verbose_name='Discipline name')),
                ('discipline_code', models.CharField(max_length=20, verbose_name='Discipline code')),
                ('discipline_objective', models.TextField(blank=True, default='', verbose_name='Discipline objective')),
                ('courses', models.ManyToManyField(blank=True, related_name='disciples2', to='course.Course', verbose_name='Discipline course')),
                ('discipline_coords', models.ManyToManyField(blank=True, related_name='disciples2', to=settings.AUTH_USER_MODEL, verbose_name='Discipline coordinators')),
                ('discipline_profs', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Discipline professors')),
            ],
            options={
                'ordering': ['courses__institutes__institute_code', 'courses__course_code', 'discipline_name'],
            },
        ),
        migrations.AddField(
            model_name='course',
            name='institutes',
            field=models.ManyToManyField(blank=True, related_name='courses2', to='course.Institute'),
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom_code', models.CharField(max_length=20, verbose_name='Classroom code')),
                ('classroom_room', models.CharField(max_length=20, verbose_name='Classroom room')),
                ('classroom_days', models.CharField(blank=True, max_length=20, verbose_name='Classroom days')),
                ('classroom_type', models.CharField(choices=[('PClass', 'Practical Class'), ('TClass', 'Theoretical Class')], default='', max_length=6, verbose_name='Classroom type')),
                ('classroom_profs', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Classroom professors')),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classrooms2', to='course.discipline', verbose_name='Classroom discipline')),
                ('students', models.ManyToManyField(blank=True, related_name='classrooms2', to='student.Student', verbose_name='Classroom students')),
            ],
            options={
                'ordering': ['discipline__courses__institutes__institute_code', 'discipline__discipline_code', 'classroom_code'],
            },
        ),
    ]

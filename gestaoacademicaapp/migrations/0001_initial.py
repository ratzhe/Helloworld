# Generated by Django 2.2.19 on 2021-04-10 20:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('datacriacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=255, null=True)),
                ('turno', models.CharField(blank=True, max_length=10, null=True)),
                ('diadasemana', models.CharField(blank=True, max_length=20, null=True)),
                ('local', models.CharField(blank=True, max_length=20, null=True)),
                ('descricao', models.TextField()),
                ('status', models.CharField(choices=[('ativa', 'Ativa'), ('desativada', 'Desativada')], max_length=11)),
                ('datacriacao', models.DateTimeField(auto_now_add=True)),
                ('curso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestaoacademicaapp.Curso', verbose_name='Cursos')),
                ('estudante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semestre', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('matriculado', 'Em andamento'), ('prevista', 'Prevista'), ('aprovado', 'Aprovado'), ('dependencia', 'Dependência')], max_length=12)),
                ('datacriacao', models.DateTimeField(auto_now_add=True)),
                ('disciplina', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='disciplinafk', to='gestaoacademicaapp.Disciplina', verbose_name='Disciplinas')),
                ('estudante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

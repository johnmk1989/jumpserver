# Generated by Django 2.1.7 on 2019-04-12 09:17

from django.db import migrations, models


def set_default_action_to_existing_perms(apps, schema_editor):
    from orgs.utils import set_to_root_org
    from ..models import Action
    set_to_root_org()
    perm_model = apps.get_model('perms', 'AssetPermission')
    db_alias = schema_editor.connection.alias
    perms = perm_model.objects.using(db_alias).all()
    default_action = Action.get_action_all()
    for perm in perms:
        perm.actions.add(default_action.id)


class Migration(migrations.Migration):

    dependencies = [
        ('perms', '0003_action'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetpermission',
            name='actions',
            field=models.ManyToManyField(blank=True, related_name='permissions', to='perms.Action', verbose_name='Action'),
        ),
        migrations.RunPython(set_default_action_to_existing_perms)
    ]

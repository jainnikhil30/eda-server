# Generated by Django 4.1.5 on 2023-02-02 15:51

from django.db import migrations, models

import aap_eda.core.enums


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_remove_activationinstance_ix_act_inst_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="activation",
            name="restart_policy",
            field=models.TextField(
                choices=[
                    ("always", "always"),
                    ("on-failure", "on-failure"),
                    ("never", "never"),
                ],
                default=aap_eda.core.enums.RestartPolicy["ON_FAILURE"],
            ),
        ),
        migrations.AlterField(
            model_name="activationinstance",
            name="status",
            field=models.TextField(
                choices=[
                    ("running", "running"),
                    ("pending", "pending"),
                    ("failed", "failed"),
                    ("stopped", "stopped"),
                    ("completed", "completed"),
                ],
                default=aap_eda.core.enums.ActivationStatus["PENDING"],
            ),
        ),
        migrations.AlterField(
            model_name="inventory",
            name="inventory_source",
            field=models.TextField(
                choices=[
                    ("project", "project"),
                    ("collection", "collection"),
                    ("user_defined", "user_defined"),
                    ("execution_env", "execution_env"),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="rolepermission",
            name="action",
            field=models.TextField(
                choices=[
                    ("create", "create"),
                    ("read", "read"),
                    ("update", "update"),
                    ("delete", "delete"),
                ],
                db_column="action_enum",
            ),
        ),
        migrations.AlterField(
            model_name="rolepermission",
            name="resource_type",
            field=models.TextField(
                choices=[
                    ("activation", "activation"),
                    ("activation_instance", "activation_instance"),
                    ("audit_rule", "audit_rule"),
                    ("job", "job"),
                    ("task", "task"),
                    ("user", "user"),
                    ("project", "project"),
                    ("inventory", "inventory"),
                    ("extra_var", "extra_var"),
                    ("playbook", "playbook"),
                    ("rulebook", "rulebook"),
                    ("execution_env", "execution_env"),
                    ("role", "role"),
                ],
                db_column="resource_type_enum",
            ),
        ),
    ]

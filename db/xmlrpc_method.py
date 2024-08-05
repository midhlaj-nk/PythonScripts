import xmlrpc.client

# Odoo 16 configuration
url_db1 = "http://localhost:8016"
db_1 = 'odoo_16_data'
username_db_1 = 'admin'
password_db_1 = 'admin'

# Odoo 17 configuration
url_db2 = "http://localhost:8017"
db_2 = 'odoo_17_community'
username_db_2 = 'admin'
password_db_2 = 'admin'

def authenticate(url, db, username, password):
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    uid = common.authenticate(db, username, password, {})
    return uid, common

def get_models(url, db, uid, password):
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    available_models = models.execute_kw(db, uid, password,
                                         'ir.model', 'search_read',
                                         [[('model', '!=', 'ir.ui.view'), ('model', 'not like', 'ir.%')]],
                                         {'fields': ['model']})
    return [model['model'] for model in available_models]

def create_model(models_proxy, db, uid, password, model_name):
    return models_proxy.execute_kw(db, uid, password, 'ir.model', 'create', [{
        'name': model_name.capitalize(),
        'model': model_name,
        'state': 'manual',
        'access_ids': [(6, 0, [])],
    }])

def create_field(models_proxy, db, uid, password, model_id, field_name):
    return models_proxy.execute_kw(db, uid, password, 'ir.model.fields', 'create', [{
        'model_id': model_id,
        'name': field_name,
        'field_description': field_name.capitalize(),
        'ttype': 'char',
        'state': 'manual',
    }])

def migrate_records(source_url, source_db, source_uid, source_password, target_url, target_db, target_uid, target_password, models):
    source_models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(source_url))
    target_models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(target_url))

    for model in models:
        if model.startswith('ir.'):
            print(f"Skipping model {model} as it starts with 'ir.'")
            continue

        try:
            # Check if model exists in target, if not create it
            target_model_ids = target_models.execute_kw(target_db, target_uid, target_password, 'ir.model', 'search', [[('model', '=', model)]])
            if not target_model_ids:
                target_model_id = create_model(target_models, target_db, target_uid, target_password, model)
            else:
                target_model_id = target_model_ids[0]

            source_records = source_models.execute_kw(source_db, source_uid, source_password, model, 'search_read', [[]], {})
            total_count = 0
            failed_count = 0

            for record in source_records:
                try:
                    # Try to migrate record, if field doesn't exist, create it
                    new_record_id = target_models.execute_kw(target_db, target_uid, target_password, model, 'create', [record])
                    print("Record migrated:", new_record_id)
                    total_count += 1
                except Exception as e:
                    print(f"Failed to migrate record from model {model}: {e}")
                    failed_count += 1

            print(f"Total records migrated for model {model}:", total_count)
            print(f"Failed records for model {model}:", failed_count)
        except Exception as e:
            print(f"Error while migrating model {model}: {e}")

if __name__ == "__main__":
    # Authenticate with both Odoo instances
    uid_db1, common_1 = authenticate(url_db1, db_1, username_db_1, password_db_1)
    uid_db2, common_2 = authenticate(url_db2, db_2, username_db_2, password_db_2)

    # Get all models from Odoo 16
    models_db1 = get_models(url_db1, db_1, uid_db1, password_db_1)

    # Migrate records from Odoo 16 to Odoo 17 for all models
    migrate_records(url_db1, db_1, uid_db1, password_db_1, url_db2, db_2, uid_db2, password_db_2, models_db1)

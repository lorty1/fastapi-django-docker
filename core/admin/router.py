class MasterRouter:
    ROUTE_PRODUCT_LABEL = ['product', 'category']
    ROUTE_AUTH_LABEL = ['auth', 'admin','contenttypes']
    def db_for_read(self,model,**hints):
        print('read',model._meta.app_label)
        if model._meta.app_label in self.ROUTE_PRODUCT_LABEL:
            return 'products_db'
        elif model._meta.app_label in self.ROUTE_AUTH_LABEL:
            print('read users_sb')
            return 'users_db'
        return None

    def db_for_write(self,model,**hints):
        print('write',model)
        if model._meta.app_label in self.ROUTE_PRODUCT_LABEL:
            return 'products_db'
        elif model._meta.app_label in self.ROUTE_AUTH_LABEL:
            print('write user')
            return 'users_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.ROUTE_AUTH_LABEL or
            obj2._meta.app_label in self.ROUTE_AUTH_LABEL
        ):
           return True
        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """
        print('test migrate =>',app_label, model_name)
        if app_label in self.ROUTE_PRODUCT_LABEL:
            return db == 'products_db'
        elif app_label in self.ROUTE_AUTH_LABEL:
            print('users =>', app_label)
            return 'users_db'
        return None       
        

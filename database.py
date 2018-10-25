from pydal import DAL, Field
from pydal.migrator import InDBMigrator

from configutils.configuration import Configuration
from utils.singelton import Singleton


@Singleton
class Database:

    def __init__(self):
        self.config = Configuration().get_db_params()
        self.db = DAL(self.config.uri,
                      pool_size=self.config.pool_size,
                      migrate_enabled=self.config.migrate,
                      check_reserved=['all'],
                      folder=self.config.folder if self.config.folder else 'database',
                      # adapter_args=dict(migrator=InDBMigrator)
                      )
        self.define_tables()

    def define_tables(self):
        self.db.define_table('notification',
                             Field('launched_on', 'date'),
                             Field('event_date', 'date'))

import mongoengine

alias_core = 'core'
db = 'snake_bnb'


def global_init():
    mongoengine.register_connection(alias_core, db)

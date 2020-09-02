import os, sys
import configparser

ENV_CONFIG = {
    'dev': 'dev',
    'prod': 'prod',
    'staging': 'staging'
}
ENV = os.environ.get('ENV', 'dev')


def load_env_configuration(env):
    if not env:
        print('Please define the ENV')
        sys.exit(1)
    config = configparser.RawConfigParser()
    print(env)
    config.read((os.path.join(os.getcwd(), '%s.cfg' % ENV_CONFIG[env])))
    return config


global configp

configp = load_env_configuration(ENV)
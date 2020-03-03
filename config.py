import yaml as ym 
import os
import sys

class config():

    #loading configuration file
    def expose_config(self, gen_conf):
        config = self.load_config('config.yaml')
        return config[gen_conf]

    #function to load configuration file
    def load_config(self, config_file):

        #base path to file configutation
        base_path = os.path.join(sys.path[0], config_file)

        with open(base_path, "r") as stream:
            try:
                return ym.safe_load(stream)
            except ym.YAMLError as exc:
                print(exc)




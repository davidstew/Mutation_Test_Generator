import sys
import copy
from shutil import copyfile
import yaml
#import ruamel

mutations1 = ['strelka', 'mutect', 'somaticsniper', 'muse', 'radia']
mutations2 = ['mutect', 'somaticsniper', 'muse', 'radia', 'strelka']
mutations3 = ['somaticsniper', 'muse', 'radia', 'strelka', 'mutect']
mutations4 = ['muse', 'radia', 'strelka', 'mutect', 'somaticsniper']
mutations5 = ['radia','strelka', 'mutect', 'somaticsniper', 'muse']

def pimp_out_dictionary(input_config, mutation_order):
    for x in range(0,5):
        current_file = "yaml_test_" + mutation_order[0] + "_" + str(x + 1) + ".yaml"
        copied_dict = copy.deepcopy(input_config)  # deep copy of dictionary, used to be loaded into yaml file
        if x == 0:
            for mut in mutation_order:
                copied_dict['mutation_calling'][mut]['run'] = True
                with open(current_file, 'w+') as conf:
                    yaml.dump(copied_dict, conf, default_flow_style = False)
                    break
        elif x == 1:
            counter = 0
            for mut in mutation_order:
                copied_dict['mutation_calling'][mut]['run'] = True
                counter += 1
                if counter == 2:
                    with open(current_file, 'w+') as conf:
                        yaml.dump(copied_dict, conf, default_flow_style = False)
                        break
        elif x == 2:
            counter = 0
            for mut in mutation_order:
                copied_dict['mutation_calling'][mut]['run'] = True
                counter += 1
                if counter == 3:
                    with open(current_file, 'w+') as conf:
                        yaml.dump(copied_dict, conf, default_flow_style = False)
                        break
        elif x == 3:
            counter = 0
            for mut in mutation_order:
                copied_dict['mutation_calling'][mut]['run'] = True
                counter += 1
                if counter == 4:
                    with open(current_file, 'w+') as conf:
                        yaml.dump(copied_dict, conf, default_flow_style = False)
                        break
        elif x == 4:
            counter = 0
            for mut in mutation_order:
                copied_dict['mutation_calling'][mut]['run'] = True
                counter += 1
                if counter == 5:
                    with open(current_file, 'w+') as conf:
                        yaml.dump(copied_dict, conf, default_flow_style = False)
                        break
def main():
    yaml_file = sys.argv[1:]
    with open(yaml_file[0], 'r') as conf:
        input_config = yaml.load(conf.read())
    for caller in mutations1:
        pimp_out_dictionary(input_config, mutations1)
    for caller in mutations2:
        pimp_out_dictionary(input_config, mutations2)
    for caller in mutations3:
        pimp_out_dictionary(input_config, mutations3)
    for caller in mutations4:
        pimp_out_dictionary(input_config, mutations4)
    for caller in mutations5:
        pimp_out_dictionary(input_config, mutations5)

if __name__ == "__main__":
    main()


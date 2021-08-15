import os


def create_new_file(*args, **kwargs):
    # todo: ask where it should be save
    complete_name = os.path.join(kwargs['folder'], kwargs['name'])
    with open(complete_name+".txt", 'w') as f:
        f.write(kwargs['text'])

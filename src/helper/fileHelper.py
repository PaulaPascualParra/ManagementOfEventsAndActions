import os


def create_new_file(*args, **kwargs):
    try:
        complete_name = os.path.join(kwargs['folder'], kwargs['name'])
        with open(complete_name+".txt", 'w') as f:
            f.write(kwargs['text'])
    except Exception as e:
        print("Something went wrong" + str(e))
        raise 

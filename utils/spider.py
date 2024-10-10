import os

def get_all_spiders():
    # Specify the directory
    directory = '../spiderapp/spiderapp/spiders'

    # Get the .py files except __init__
    file_list = [f for f in os.listdir(directory) if f.endswith('.py') and f != '__init__.py']

    # Remove the .py extension
    file_list = [os.path.splitext(f)[0] for f in file_list]

    return file_list

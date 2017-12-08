import subprocess
import json
import yaml


# Function for Python 2
def python2(source, name):

    path_python = subprocess.check_output(source+'[ -L $(which python) ] && readlink -f $(which python) || which python', shell=True)
    path_pip = str(subprocess.check_output(source+'pip -V', shell=True)).split(' ')
    pythonpath = subprocess.check_output(source+'echo $PYTHONPATH', shell=True)

    modules = subprocess.check_output(source+'pip freeze', shell=True)
    modules_list = modules.split('\n')
    modules_list.remove('')

    modules_names = []
    modules_versions = []

    for i in range(len(modules_list)):
        a = modules_list[i].split('==')
        modules_names.append(a[0])
        modules_versions.append(a[1])

    global json_output
    json_pip = {'version': path_pip[1], 'path': path_pip[3]}
    json_path = {'bin_path': path_python.split('\n')[0], 'pythonpath': pythonpath.split('\n')[0]}
    json_modules = {}

    for i in range(len(modules_versions)):
        json_modules.update({modules_names[i]: modules_versions[i]})

    json_output.update({name: {'path': json_path, 'pip': json_pip, 'modules': json_modules}})
    return json_output


# Function for Python 3
def python3(source, name):
    path_python = subprocess.getoutput(source+'[ -L $(which python) ] && readlink -f $(which python) || which python')
    path_pip = str(subprocess.getoutput(source+'pip -V')).split(' ')
    pythonpath = subprocess.getoutput(source+'echo $PYTHONPATH')

    modules = subprocess.getoutput(source+'pip freeze')
    modules_list = modules.split('\n')

    modules_names = []
    modules_versions = []
    if len(modules_list) > 1:
        for i in range(len(modules_list)):
            a = modules_list[i].split('==')
            modules_names.append(a[0])
            modules_versions.append(a[1])

    global json_output
    json_pip = {'version': path_pip[1], 'path': path_pip[3]}
    json_path = {'bin_path': path_python.split('\n')[0], 'pythonpath': pythonpath.split('\n')[0]}
    json_modules = {}

    for i in range(len(modules_versions)):
        json_modules.update({modules_names[i]: modules_versions[i]})

    json_output.update({name: {'path': json_path, 'pip': json_pip, 'modules': json_modules}})

    return json_output

# Start of the script
a = 0

# Check for current Python version
try:
    python_ran = subprocess.getoutput('python -V')
except AttributeError:
    python_ran = subprocess.check_output('python -V', shell=True)
    a += 1


# If Python 2
if a == 1:
    source2 = ''
    json_output = {}

    python2(source2, 'current')

    # print (json_output)
    ##################################################################
    ##################################################################

    list_pyenvs = (subprocess.check_output('pyenv virtualenvs', shell=True)).split('\n')
    list_pyenvs3 = []
    for x in list_pyenvs:
        list_pyenvs2 = []
        list_pyenvs2 = x.split(' ')
        if len(list_pyenvs2) > 1:
            list_pyenvs3.append(list_pyenvs2[2])

    ##################################################################
    ##################################################################

    for x in list_pyenvs3:
        source2 = 'source ~/.pyenv/versions/'+x+'/bin/activate;'

        python2(source2, x)


    with open('output.json', 'w') as fp:
        json.dump(json_output, fp)
    with open('output.yaml', 'w') as fp:
        yaml.dump(json_output, fp)


# If Python 3
else:
    source2 = ''
    json_output = {}

    python3(source2, 'current')

    ##################################################################
    ##################################################################

    list_pyenvs = (subprocess.getoutput('pyenv virtualenvs')).split('\n')
    list_pyenvs3 = []
    for x in list_pyenvs:
        list_pyenvs2 = []
        list_pyenvs2 = x.split(' ')
        if len(list_pyenvs2) > 1:
            list_pyenvs3.append(list_pyenvs2[2])

    ##################################################################
    ##################################################################

    for x in list_pyenvs3:
        source2 = 'source ~/.pyenv/versions/'+x+'/bin/activate;'

        python3(source2, x)

    with open('output.json', 'w') as fp:
        json.dump(json_output, fp)
    with open('output.yaml', 'w') as fp:
        yaml.dump(json_output, fp)

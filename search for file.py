import os
for root, dirs, files in os.walk(os.getcwd()):
        if 'facto.py' in files:
            print os.path.join(root, 'facto.py')

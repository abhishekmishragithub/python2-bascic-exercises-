import subprocess as sub

a = sub.Popen('python D:\SJCET\Workshops\Python\Exercises\class\stdin.py',\
              stdin=sub.PIPE)

print a.communicate('hello?')

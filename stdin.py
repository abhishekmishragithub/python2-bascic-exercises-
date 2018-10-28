# write_to_stdin.py
import sys
inp = sys.stdin.read()
sys.stdout.write('Received: %s'%inp)

import os
os.chdir(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))))

lines = [line.strip() for line in open('x.input.ref')]
f=open('tasks.txt','w')
f.write('''
hello This is file writing program
I write the text into file''')
f.close()

f=open('tasks.txt','a')
f.write('''\nTask Complted!''')
f.close()

with open('tasks.txt','r') as f:
    for line in f.readlines():
        print(line) 
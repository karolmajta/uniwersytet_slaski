from fabric import task

@task
def clone_and_restart(c):
    result = c.run('lsof -i :8080')
    lines = result.stdout.strip().split('\n')[1:]
    pids = []
    for line in lines:
       chunks = line.split(' ')
       pid = [c for c in line.split(' ') if c.strip()][1]
       pids.append(pid)
    for pid in set(pids):
       print(f'kill -9 {pid}')     
       c.run(f'kill -9 {pid}')

    result = c.run('cd ~/uniwersytet_slaski && ./virtualenv/bin/python main.py')
    print(result.stdout)


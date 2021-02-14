from fabric import task


# This comment was added by Wiktor

@task
def clone_and_restart(c):
    result = c.run('lsof -i :8080')
    lines = result.stdout.strip().split('\n')[1:]
    pids = []
    for line in lines:
        pid = [c for c in line.split(' ') if c.strip()][1]
        pids.append(pid)
    for pid in set(pids):
        print(f'kill -9 {pid}')
        c.run(f'kill -9 {pid}')

    c.run('cd ~/uniwersytet_slaski && git pull')

    result = c.run('cd ~/uniwersytet_slaski '
                   '&& ./virtualenv/bin/gunicorn '
                   '-b 0.0.0.0:8080 main:app --daemon')

from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/game/gamewindow.py")

@task
def pylint(ctx):
    ctx.run("pylint src")

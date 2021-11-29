from invoke import task

@task
def start(ctx):
    ctx.run("python src/game/gamewindow.py")

@task
def pylint(ctx):
    ctx.run("pylint src")

@task
def test(ctx):
    ctx.run("pytest src")

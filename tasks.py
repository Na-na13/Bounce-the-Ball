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

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task
def coverage_report(ctx):
    ctx.run("coverage html")



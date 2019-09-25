from invoke import Collection, Context, task

ns = Collection()

@ns.task
def lint(c: Context) -> None:
    """
    Formats code
    """
    c.run("black --exclude=venv .")

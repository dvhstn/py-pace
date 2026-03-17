import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def hello():
    console.print("🏃 Welcome to py-pace!")


@app.command()
def stats():
    console.print("📊 No runs yet. Import data first.")


if __name__ == "__main__":
    app()
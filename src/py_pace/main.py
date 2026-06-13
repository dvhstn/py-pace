import typer
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box

app = typer.Typer(add_completion=False)
console = Console()


@app.callback(invoke_without_command=True)
def main():
    content = Text("🏃 py-pace", style="bold #FC4C02", justify="center")
    console.print(Panel(content, box=box.ROUNDED, border_style="#FC4C02", padding=(1, 4)))


if __name__ == "__main__":
    app()

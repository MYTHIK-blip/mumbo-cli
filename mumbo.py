# mumbo.py
import typer
from rich import print
from rich.console import Console
from datetime import datetime

app = typer.Typer()
console = Console()

@app.callback()
def main():
    console.rule("[bold cyan]☼ MUMBO CLI - RITUAL SHELL ☼[/]")
    print(f"[bold magenta]Invocation Time:[/] {datetime.now().isoformat()}")
    print("[green]Welcome, Scrollwalker. The glyphshell is live.[/]\n")

@app.command()
def cast(spell: str = typer.Argument(..., help="Name of the glyph or spell to cast")):
    """
    Execute a named glyph ritual.
    """
    print(f"[bold cyan]Casting spell:[/] {spell}")
    # TODO: Load from glyph registry
    # Placeholder logic
    if spell.lower() == "fraxtint":
        print("[bold green]>> Vision alignment with Fraxtint complete.")
    else:
        print("[red]>> Unknown glyph. Ritual incomplete.[/]")

if __name__ == "__main__":
    app()

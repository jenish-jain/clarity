from pathlib import Path
import typer
from activityParser import parse_html_to_json

def load_html_data(path):
    with open(path, "r") as file:
        data = file.read()
    return data


def main(filename: Path):
    if not filename.is_file():
        print(f"incorrect file path: {filename}")
    else:
        html_data = load_html_data(filename)
        json_data = parse_html_to_json(html_data)
        print(json_data)


if __name__ == "__main__":
    typer.run(main)
import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="AI Media Filter (demo CLI)")
    parser.add_argument(
        "--input",
        required=True,
        help="Folder path to scan"
    )
    args = parser.parse_args()

    input_path = Path(args.input).resolve()

    if not input_path.exists():
        print(f"Path not found: {input_path}")
        return

    files = [p for p in input_path.rglob("*") if p.is_file()]

    print(f"Scanned folder: {input_path}")
    print(f"Total files found: {len(files)}")


if __name__ == "__main__":
    main()

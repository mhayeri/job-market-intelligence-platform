import argparse
from datetime import datetime
from pathlib import Path
import pandas as pd


def handle_args():
    """
    Handle command line arguments
    """
    parser = argparse.ArgumentParser(description="Ingest job postings data")
    parser.add_argument("--source", type=str, required=True, help="Dataset name (e.g. job_market)")
    args = parser.parse_args()
    return args

def main():
    """
    Ingest job postings data from a CSV file and write it to an immutable,
    partitioned raw data lake path.
    """
    args = handle_args()
    if not args.source:
        raise ValueError("Source argument is required")

    dataset_name = args.source  # e.g. job_market
    ingestion_date = datetime.now().strftime("%Y-%m-%d")

    # Resolve source path
    source_csv_path = Path("data/source") / f"{dataset_name}.csv"

    if not source_csv_path.exists():
        raise FileNotFoundError(f"Source file not found: {source_csv_path}")

    # Resolve raw output directory
    output_dir_path = Path("data/raw/jobs") / f"ingestion_date={ingestion_date}"

    # Enforce immutability
    if output_dir_path.exists():
        raise FileExistsError(f"Ingestion partition already exists: {output_dir_path}")

    # Read source data
    df = pd.read_csv(source_csv_path)

    # Create output directory
    output_dir_path.mkdir(parents=True)

    # Write raw data
    output_path = output_dir_path / source_csv_path.name
    df.to_csv(output_path, index=False)

    print(f"Ingested {len(df)} rows to {output_path}")


if __name__ == "__main__":
    main()

# Job Market Intelligence Platform

An end-to-end data platform designed to analyze job market trends, skill demand, and salary distributions using modern data engineering tools.

This project is built incrementally to mirror real-world data platforms, covering the full lifecycle from raw data ingestion to analytics-ready datasets and business intelligence dashboards.

## 🎯 Project Goals
- Build a production-style data ingestion pipeline
- Learn end-to-end ETL/ELT workflows
- Work with large-scale datasets (~1M+ records)
- Apply modern tools used in industry

## 🧱 Current Phase
- **Phase 1**: Raw data ingestion (batch processing)
- Immutable, partitioned data lake layout
- Python-based ingestion logic

**Future phases** will introduce Spark, Airflow, Snowflake, dbt, and BI tooling.

### Directory Details

- **`data/`**: Contains all data files, organized by source. This directory is gitignored to avoid committing large datasets.
  - `source/`: Raw, unprocessed data files as received from external sources

- **`ingestion/`**: Python scripts for data ingestion and processing
  - `ingest_jobs.py`: Main ingestion pipeline for job market data

- **`tools/`**: Helper scripts for data generation, testing, and utilities (gitignored)

### Current Implementation
- **Ingestion**: Batch processing of job market data
- **Storage**: CSV-based source data in `data/source/`
- **Processing**: Python-based transformation scripts

### Planned Enhancements
- Apache Spark for distributed processing
- Apache Airflow for workflow orchestration
- Snowflake for cloud data warehousing
- dbt for data transformation
- BI dashboards (Tableau/PowerBI/Looker)

### Running the Ingestion Pipeline

```bash
python ingestion/ingest_jobs.py
```

## 📈 Project Roadmap

- [x] Initial project structure
- [x] Raw data ingestion setup
- [ ] Implement partitioned data lake
- [ ] Add data validation
- [ ] Integrate Apache Spark
- [ ] Set up Airflow DAGs
- [ ] Connect to Snowflake
- [ ] Build dbt models
- [ ] Create BI dashboards

## 🤝 Contributing

This is a personal learning project, but suggestions and feedback are welcome!

## 📝 License

This project is for educational purposes.
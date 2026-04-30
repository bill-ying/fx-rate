# FX Rate Retriever — Bank of Canada

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Docker](https://img.shields.io/badge/Docker-Supported-blue.svg)
![Architectures](https://img.shields.io/badge/Architectures-amd64%20%7C%20arm64-orange.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

---

## 📌 Overview

This tool retrieves the exchange rate between the **Canadian dollar (CAD)** and the **US dollar (USD)** using data published by the **Bank of Canada**.

The exchange rates can be retrieved in two modes:

- **Specific date** (e.g., `20210331`)
- **Last Bank of Canada business day of each month** for a given year (e.g., `2020`)

---

## ⚙️ Usage

### Required Argument

`start_currency` — direction of conversion:

- `c` → CAD to USD  
- `u` → USD to CAD  

### Date Selection (One Required)

- `-d <yyyymmdd>` — retrieve rate for a specific date  
- `-m <yyyy>` — retrieve rates for the last business day of each month in a year  


## 📘 Examples

### CAD → USD on March 31, 2021
```bash
python fx_rate.py c -d 20210331
```

### USD → CAD for the last business day of each month in 2020
```bash
python fx_rate.py u -m 2020
```

## 🐳 Docker Support

The repository includes all components needed to build and package the application as a Docker image.

GitHub Actions automatically builds multi‑architecture images (amd64 and arm64) and publishes them to Docker Hub:

🔗 Docker Hub: https://hub.docker.com/r/billying/fx-rate

### Run via Docker

```bash
docker run --rm billying/fx-rate c -d 20210331
docker run --rm billying/fx-rate u -m 2020
```


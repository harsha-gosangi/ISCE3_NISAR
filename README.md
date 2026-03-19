# 🚀 NISAR InSAR Processing Workflow (ISCE3)

<p align="center">
  <b>End-to-End Interferometric Processing using ISCE3</b><br>
  RSLC → RIFG → RUNW → GUNW
</p>

---

## 📌 Overview

This repository provides a **complete workflow** for processing NISAR InSAR data using the **ISCE3 framework**.

It supports:
- 📡 Interferogram generation
- 📉 Dense offset estimation
- 🧩 Rubbersheet correction
- 🌍 Geocoding
- 📈 Deformation analysis

---

## 🧰 Tech Stack

| Tool | Purpose |
|------|--------|
| 🐍 Python 3.9 | Core environment |
| 🛰️ ISCE3 | InSAR processing |
| 🗺️ GDAL | Raster processing |
| 📦 HDF5 / h5py | Data format |
| 🧮 NumPy / SciPy | Computation |
| 📊 Pandas | Data handling |
| 🔓 SNAPHU | Phase unwrapping |
| 🌦️ PyAPS3 | Atmospheric correction |

---

## ⚙️ Installation

### 🔹 Step 1 — Create Environment
```bash
conda create -n isce3 -c conda-forge python=3.9 isce3
conda activate isce3
conda install -c conda-forge \
pandas numpy scipy matplotlib \
hdf5 h5py netcdf4 \
gdal rasterio pyproj shapely \
snaphu
pip install pyaps3
sudo apt update
sudo apt install snaphu
/media/ubuntu-harsha/newvolume2/NISAR/InSAR
python -m nisar.workflows.insar --generate-config > insar.yaml
python -m nisar.workflows.insar insar.yaml

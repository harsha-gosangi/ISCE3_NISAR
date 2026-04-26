# 🚀 NISAR InSAR Processing Workflow (ISCE3)

<p align="center">
  <b>End-to-End Interferometric Processing using ISCE3</b><br>
</p>

---

## 📌 Overview

This repository provides a **complete workflow** for processing NISAR InSAR data using the **ISCE3 framework**.

It enables transformation of RSLC (Radar Single Look Complex) data into geocoded deformation products through a robust interferometric processing chain.


---

## 🖥️ System Compatibility

- 🐧 Linux (Ubuntu 24.04 or above versions) — Recommended  
- 🍎 macOS — Supported  

---

## 🛰️ Dataset Used

```
https://search.asf.alaska.edu/#/?dataset=NISAR&prodConfig=PR

NISAR_L1_PR_RSLC_005_172_A_008_2005_DHDH_A_20251122T024618_20251122T024652_X05007_N_F_J_001
NISAR_L1_PR_RSLC_006_172_A_008_2005_DHDH_A_20251204T024618_20251204T024653_X05007_N_F_J_001
```

---

## 🧰 Tech Stack

| Tool | Purpose |
|------|--------|
| 🐍 Python 3.13 | Core environment |
| 🛰️ ISCE3 | InSAR processing engine |
| 🗺️ GDAL | Raster & geospatial processing |
| 📦 HDF5 / h5py | Data format handling |
| 🧮 NumPy / SciPy | Scientific computation |
| 📊 Pandas | Data analysis |
| 🔓 SNAPHU | Phase unwrapping |
| 🌦️ PyAPS3 | Atmospheric correction |

---

## ⚙️ Installation & Execution

### 🟢 Step 1 — Create Conda Environment
```bash
conda create -n isce3 python=3.13
```

---

### 🟢 Step 2 — Activate Environment
```bash
conda activate isce3
```

---

### 🟢 Step 3 — Install ISCE3
```bash
conda install isce3 -c conda-forge
```

---

### 🟢 Step 4 — Install GDAL
```bash
conda install gdal -c conda-forge
```

---

### 🟢 Step 5 — Install Python Libraries
```bash
pip install pyaps3 pandas h5py numpy scipy matplotlib netcdf4 rasterio pyproj shapely snaphu
```

---

### 🟢 Step 6 — Install GDAL HDF5 Support
```bash
conda install -c conda-forge libgdal-hdf5
```

---

### 🟢 Step 7 — Generate Run Configuration
```bash
python -m nisar.workflows.insar --generate-config > insar.yaml
```

---

### 🟢 Step 8 — Run InSAR Workflow
```bash
python -m nisar.workflows.insar insar.yaml
```
insar.yaml is located on the docs folder
---

## ✅ Workflow Summary

```text
Environment Setup → Dependency Installation → Configuration → InSAR Processing
```

---

## ⚠️ Important Notes

- Always generate a fresh `insar.yaml`  
- Ensure DEM fully covers your study area  

---


## 🔄 Processing Pipeline

```
RSLC
 ↓
Coregistration
 ↓
Interferogram (RIFG)
 ↓
Dense Offset Estimation
 ↓
Rubbersheet Correction
 ↓
Phase Filtering
 ↓
Phase Unwrapping (SNAPHU)
 ↓
Geocoding
 ↓
RUNW → GUNW
```

---


## 🧪 Common Issues & Fixes

### YAML Error
```bash
python -m nisar.workflows.insar --generate-config > insar.yaml
```
---

## 🌈 Interferogram Output

<p align="center">
  <img src="interferogram.png" width="70%">
</p>

---

## 🌍 Applications

- 🌎 Earthquake deformation analysis  
- 🌋 Volcano monitoring  
- 🧊 Glacier motion tracking   
- 🌱 Land subsidence studies  

---

## 👨‍💻 Author

**Harsha Vardhan Gosangi**  
Research Scholar
Geoinformatics 

---
## 🙏 Acknowledgement

This work is based on the **ISCE3 (InSAR Scientific Computing Environment)** framework.

We thank the ISCE3 developers for their contributions to open-source SAR processing tools.

---
## ⭐ Support

If this project helped you, consider giving it a ⭐ on GitHub!

---

## 📜 License

For research and educational purposes only.

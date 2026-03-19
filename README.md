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

- ✅ Ubuntu 20.04 / 22.04 (Recommended)  

---

## 🛰️ Dataset Used

```
NISAR_L1_PR_RSLC_005_172_A_008_2005_DHDH_A_20251122T024618_20251122T024652_X05007_N_F_J_001
NISAR_L1_PR_RSLC_006_172_A_008_2005_DHDH_A_20251204T024618_20251204T024653_X05007_N_F_J_001
```

---

## 🧰 Tech Stack

| Tool | Purpose |
|------|--------|
| 🐍 Python 3.9 | Core environment |
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

- Use **Python 3.9** for stable results  
- Avoid mixing `pip` and `conda` for core libraries  
- Always generate a fresh `insar.yaml`  
- Start processing with **freqA only**  
- Ensure DEM fully covers your study area  

---

## 📝 Configuration (insar.yaml)

```yaml
input_file_group:
  reference_rslc_file: /path/to/reference.h5
  secondary_rslc_file: /path/to/secondary.h5

dynamic_ancillary_file_group:
  dem_file: /path/to/dem.tif

product_path_group:
  product_path: ./output
```

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

### SNAPHU Error
```bash
conda install -c conda-forge snaphu
```

### Rubbersheet Error
→ Use only freqA

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
- 🏗️ Infrastructure monitoring  
- 🌱 Land subsidence studies  

---

## 👨‍💻 Author

**Harsha Vardhan Gosangi**  
Research Scholar – Geoinformatics  

---

## ⭐ Support

If this project helped you, consider giving it a ⭐ on GitHub!

---

## 📜 License

For research and educational purposes only.

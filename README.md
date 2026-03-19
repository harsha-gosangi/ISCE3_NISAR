# 🚀 NISAR InSAR Processing Workflow (ISCE3)

<p align="center">
  <b>End-to-End Interferometric Processing using ISCE3</b><br>
</p>

---

## 📌 Overview

This repository provides a **complete workflow** for processing NISAR InSAR data using the **ISCE3 framework**.

It enables transformation of RSLC (Radar Single Look Complex) data into geocoded deformation products through a robust interferometric processing chain.

### 🔍 Key Capabilities
- 📡 Interferogram generation  
- 📉 Dense offset estimation  
- 🧩 Rubbersheet correction  
- 🌍 Geocoding  
- 📈 Surface deformation analysis  

---

## 🛰️ Dataset Used

```
NISAR_L1_PR_RSLC_005_172_A_008_2005_DHDH_A_20251122T024618_20251122T024652_X05007_N_F_J_001
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
Create a new conda environment named `isce3`.

---

### 🟢 Step 2 — Activate Environment
```bash
conda activate isce3
```
Activate the environment.

---

### 🟢 Step 3 — Install GDAL
```bash
conda install gdal -c conda-forge
```

---

### 🟢 Step 4 — Install ISCE3
```bash
conda install isce3 -c conda-forge
```

---

### 🟢 Step 5 — Reinstall GDAL
```bash
conda install gdal -c conda-forge
```

---

### 🟢 Step 6 — Install Python Libraries
```bash
pip install pyaps3 pandas h5py pandas numpy scipy matplotlib hdf5 h5py netcdf4 gdal rasterio pyproj shapely snaphu
```

---

### 🟢 Step 7 — Install GDAL HDF5 Support
```bash
conda install -c conda-forge libgdal-hdf5
```

---

### 🟢 Step 8 — Reinstall GDAL (Link Fix)
```bash
conda install gdal -c conda-forge
```

---

### 🟢 Step 9 — Final GDAL Check
```bash
conda install gdal -c conda-forge
```

---

### 🟢 Step 10 — Generate Run Configuration
```bash
python -m nisar.workflows.insar --generate-config > insar.yaml
```

---

### 🟢 Step 11 — Run InSAR Workflow
```bash
python -m nisar.workflows.insar insar.yaml
```

---

## ✅ Workflow Summary

```text
Environment Setup → Dependencies → Configuration → InSAR Processing
```

---

## 📝 Configuration (insar.yaml)

Before execution, update:

- 📂 Reference RSLC file  
- 📂 Secondary RSLC file  
- 🏔️ DEM file  
- 📤 Output directory  

### Example
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

## 📊 Output Products

- 🌈 Wrapped interferogram (RIFG)  
- 📐 Unwrapped phase (RUNW)  
- 📉 Coherence maps  
- 📍 Dense offset fields  
- 🌍 Geocoded deformation products (GUNW)  

---

## ⚠️ Important Notes

- ⚠️ ISCE3 is most stable with **Python 3.9**
- ❌ Avoid Python 3.13 for production runs  
- ❌ Avoid mixing pip & conda (except PyAPS3)  
- 🔄 Always regenerate `insar.yaml`  
- 🎯 Start with **freqA only**  
- 🗺️ Ensure DEM coverage is complete  

---

## 🧪 Common Issues & Fixes

### YAML Validation Error
```bash
python -m nisar.workflows.insar --generate-config > insar.yaml
```

### SNAPHU Error
```bash
conda install -c conda-forge snaphu
```

### Rubbersheet Error
→ Use only freqA

### Missing Modules
```bash
conda install pandas numpy scipy
```

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
Research Scholar – Remote Sensing & Geoinformatics  

---

## ⭐ Support

If this project helped you, consider giving it a ⭐ on GitHub!

---

## 📜 License

This project is intended for research and educational purposes only.

## 🏔️ DEM Preparation Script

This script downloads and clips a Digital Elevation Model (DEM) using the `elevation` library and `rasterio`.

It generates a DEM compatible with the ISCE3 InSAR workflow.

---

## 📌 What This Script Does

- 🌍 Downloads DEM data (SRTM1 or SRTM3)  
- ✂️ Clips DEM to a given bounding box (lat/lon)  
- 💾 Saves output as GeoTIFF  
- 📐 Preserves spatial reference and transform  

---

## 📦 Requirements

```bash
pip install elevation rasterio
```

## 🌍 Bounding Box (bbox) Format

The bounding box defines the geographic area for DEM extraction.

Format:

```python
bbox = (xmin, ymin, xmax, ymax)
```

Where:

- `xmin` → minimum longitude (west)
- `ymin` → minimum latitude (south)
- `xmax` → maximum longitude (east)
- `ymax` → maximum latitude (north)

👉 Coordinate system: **EPSG:4326 (WGS84)**

---

## 📌 Example 1 — India Region

```python
bbox = (72.0, 18.0, 78.0, 23.0)
```

Covers:
- West → 72°E  
- South → 18°N  
- East → 78°E  
- North → 23°N  

---

## 📌 Example 2 — Small Area (City Level)

```python
bbox = (77.55, 12.90, 77.75, 13.10)
```

👉 Example: Bengaluru region

---

## 📌 Example 3 — Your Current Case

```python
bbox = (14.107, 11.309, 39.99, 43.177)
```

👉 Covers a large region (Africa–Europe span)

---

## 🧭 How to Get Bounding Box Coordinates

### 🔹 Method 1 — Google Maps

1. Open Google Maps  
2. Right-click → "What's here?"  
3. Note latitude & longitude  
4. Choose area corners → build bbox  

---

### 🔹 Method 2 — QGIS

1. Load your AOI (Area of Interest)  
2. Go to:
   ```
   Layer → Properties → Information
   ```
3. Copy **Extent** values  

---

### 🔹 Method 3 — From SAR Data (Advanced)

Bounding box can be extracted from RSLC metadata using Python.

---

## ⚠️ Important Tips

- Longitude = **X axis**  
- Latitude = **Y axis**  
- Always follow order:  
  ```
  (min_lon, min_lat, max_lon, max_lat)
  ```
- Make bbox slightly larger than your study area  

---

## ✅ Quick Check

```python
# Correct
bbox = (xmin, ymin, xmax, ymax)

# ❌ Wrong (DO NOT swap)
bbox = (lat, lon, lat, lon)
```
---

## ⚙️ Usage

```python
import elevation
import rasterio
from rasterio.windows import from_bounds

def prepare_dem(bbox, out_path, dem_type="SRTM1"):
    """
    bbox = (xmin, ymin, xmax, ymax) in lon/lat (EPSG:4326)
    """

    tmp_dem = "tmp_dem.tif"

    elevation.clip(
        bounds=bbox,
        output=tmp_dem,
        product=dem_type
    )

    with rasterio.open(tmp_dem) as src:
        window = from_bounds(*bbox, transform=src.transform)
        out_img = src.read(1, window=window)
        out_transform = src.window_transform(window)
        out_meta = src.meta.copy()

    out_meta.update({
        "height": out_img.shape[0],
        "width": out_img.shape[1],
        "transform": out_transform
    })

    with rasterio.open(out_path, "w", **out_meta) as dst:
        dst.write(out_img, 1)

    print(f"DEM saved: {out_path}")


if __name__ == "__main__":

    bbox = (14.107, 11.309, 39.99, 43.177)

    prepare_dem(bbox, out_path="SRTM1_mosaic_clip.tif")
    prepare_dem(bbox, out_path="SRTM3_mosaic_clip.tif", dem_type="SRTM3")
```

---

## 📁 Example Usage

```python
prepare_dem(bbox, out_path="SRTM1_mosaic_clip.tif")
prepare_dem(bbox, out_path="SRTM3_mosaic_clip.tif", dem_type="SRTM3")
```

---

## 🧠 Notes

- SRTM1 → higher resolution (~30m) → best for InSAR  
- SRTM3 → lower resolution (~90m) → faster processing  
- Ensure DEM fully covers your study area  
- Output DEM is directly usable in ISCE3  

---

## 🔗 Integration with ISCE3

```yaml
dynamic_ancillary_file_group:
  dem_file: /path/to/SRTM1_mosaic_clip.tif
```

---

## ⚠️ Common Issues

**DEM download fails**
- Check internet connection  
- Reduce bounding box size  

**Rasterio errors**
```bash
pip install --upgrade rasterio
```

---

## ✅ Output Example

```
DEM saved: SRTM1_mosaic_clip.tif
```

---

## 🚀 Use Cases

- NISAR / ISCE3 InSAR processing  
- Terrain correction  
- Geocoding workflows  
- Elevation-based analysis  

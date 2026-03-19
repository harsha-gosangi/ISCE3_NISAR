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

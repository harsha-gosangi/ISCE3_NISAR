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

    print(f"✅ DEM saved: {out_path}")


# ----------------------------
# SCRIPT ENTRY POINT
# ----------------------------
if __name__ == "__main__":

    bbox = (14.107, 11.309, 39.99, 43.177)

    prepare_dem(bbox, out_path="SRTM1_mosaic_clip.tif")
    prepare_dem(bbox, out_path="SRTM3_mosaic_clip.tif", dem_type="SRTM3")


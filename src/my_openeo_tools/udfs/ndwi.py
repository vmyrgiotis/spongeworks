from openeo.udf import XarrayDataCube
import numpy as np
import xarray as xr


def apply_datacube(cube: XarrayDataCube, context: dict) -> XarrayDataCube:
    arr = cube.get_array()

    # Support backends using either 'bands' or 'band'.
    band_dim = "bands" if "bands" in arr.dims else ("band" if "band" in arr.dims else None)
    if band_dim is None:
        raise ValueError(f"No band dimension found. Available dims: {arr.dims}")

    b03 = arr.sel({band_dim: "B03"}) * 0.0001
    b08 = arr.sel({band_dim: "B08"}) * 0.0001
    scl = arr.sel({band_dim: "SCL"})

    # Mask cloud/shadow classes: 3 (shadow), 8/9 (cloud)
    clear_mask = ~scl.isin([3, 8, 9])
    ndwi = xr.where(clear_mask, (b03 - b08) / (b03 + b08), np.nan)

    # Return one-band cube named NDWI.
    ndwi = ndwi.expand_dims({band_dim: ["NDWI"]})
    return XarrayDataCube(ndwi)

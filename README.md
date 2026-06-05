# SpongeWorks

SpongeWorks is a notebook-driven Earth Observation workflow for flood monitoring and related indicators over user-defined areas of interest (AOIs).

The main workflow is implemented in the notebook `Notebook - SpongeWorks.ipynb`.

## What the Notebook Does

The notebook builds a processing chain that:

- defines AOIs and a period of interest;
- fetches EO products through openEO and STAC APIs;
- saves yearly/period outputs as GeoTIFF and NetCDF files;
- generates map images for visual inspection and reporting.

## Implemented Processing Blocks

1. Area and period setup
- Loads AOIs from site-specific vector files.
- Builds a bounding box around AOIs for EO queries.

2. Sentinel-2 NDWI
- (Optional extraction block) queries Sentinel-2 L2A, masks cloud/shadow classes, computes NDWI, and downloads GeoTIFF outputs.
- Loads NDWI rasters, builds a time-indexed xarray dataset, computes anomaly index relative to baseline mean, and writes NetCDF.
- Produces per-date NDWI PNG maps clipped/reprojected to AOI context.

3. Sentinel-1 backscatter (VV/VH)
- Loads backscatter NetCDF and prepares VV/VH channels.
- Computes VH/VV ratio and a simple water mask using threshold rules.
- Produces per-date PNG panels (VV, VH/VV ratio, water mask).

4. Soil Moisture (SSM)
- (Optional extraction block) queries `CGLS_SSM_V1_EUROPE` and downloads rasters.
- Builds a time-indexed SSM dataset and saves NetCDF.
- Produces per-date SSM PNG maps.

5. Global Flood Monitoring (GFM)
- Includes STAC-based retrieval and plotting blocks (currently commented in parts of the notebook).

## Repository Outputs

Generated outputs are written to:

- `eo_data/` for downloaded/processed EO data (GeoTIFF, NetCDF)
- `images/` for generated figures

These directories are intentionally excluded from version control.

## Environment and Running

This repository uses Python 3.12+ and dependencies declared in `pyproject.toml`.

Typical workflow:

```bash
uv sync
uv run jupyter lab
```

Then open `Notebook - SpongeWorks.ipynb` and run the relevant cells for your site and time window.

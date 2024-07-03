# HFDiscrim

<p align="center">
  <img src="https://github.com/yachliu/HFDiscrim/blob/main/images/hfdiscrim-logo.png" alt="image" width="400"/>
  <p>HFDiscrim effectively combines single-run and multi-run features to characterize chromatographic peaks</p>
</p>

## Docker image
```shell
docker pull meiyulab/hfdiscrim:1.0.0
```
## Container creation and startup
Create a container (named hfdiscrim_work) based on the image `meiyulab/hfdiscrim:1.0.0` and simultaneously mount the local folder `/path/to/hfdiscrim` to the folder `/hfdiscrim` (in the container) by running the following command in your terminal:
```shell
docker run -it --name hfdiscrim_work -v /path/to/hfdiscrim:/hfdiscrim meiyulab/hfdiscrim:1.0.0 /bin/bash
```
Please change /path/to/hfdiscrim to your own path.

## HFDiscirm arguments
|parameters|descriptions|
|---|---|
|--db_fpath|The output of pyprophet (merged.osw).|
|--chrom_dpath|Directory of openswath output (.chrom.sqMass).|
|--work_dpath|Directory for output files.|
|--seed|Random seed for decoy generation (default: 123).|
|--map_size|The size of the temporary database (default: 32).|
|--fdr_precursor|FDR of precursor level (default: 0.01).|
|--n_mrg|The number of candidate MRGroup (default: 3).|
|--nrt_width_percent|Percentage of the search range in normalized retention time (default: 0.02).| 

## Citation
Please cite this.

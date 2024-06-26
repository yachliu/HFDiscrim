import click
from multiprocessing import cpu_count

from joint import mrgd

CONTEXT_SETTINGS = dict(help_option_names = ['-h', '--help'], max_content_width = 120)

def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('HFDiscrim Version 1.0.0')
    ctx.exit()
    
@click.command(context_settings = CONTEXT_SETTINGS)
@click.option('--version', is_flag = True, callback = print_version, expose_value = False, is_eager = True, help = "Print version and exit.")
@click.option("--db_fpath", required = True, type = click.Path(exists = True), help = "The output of pyprophet (merged.osw).")
@click.option("--chrom_dpath", required = True, type = click.Path(exists = True), help = "Directory of openswath output (.chrom.sqMass).")
@click.option("--work_dpath", required = True, type = click.Path(exists = False), help = "Directory for output files.")
@click.option("--n_threads", default = cpu_count(), show_default = True, type = int, help = "Number of threads.")
@click.option("--seed", default = 123, show_default = True, type = int, help = "Random seed for decoy generation.")
@click.option("--map_size", default = 32, show_default = True, type = int, help = "The size of the temporary database.")
@click.option("--fdr_precursor", default = "0.01", show_default = True, type = float, help = "FDR of precursor level.")
@click.option("--nrt_width_percent", default = "0.02", show_default = True, type = float, help = "Percentage of the search range in normalized retention time.")
def HFDiscrim(db_fpath, chrom_dpath, work_dpath, n_threads, seed, map_size, fdr_precursor, nrt_width_percent):
    mrgd(db_fpath, chrom_dpath, work_dpath, n_threads, map_size, fdr_precursor, nrt_width_percent, seed)
    
if __name__ == "__main__":
    HFDiscrim()
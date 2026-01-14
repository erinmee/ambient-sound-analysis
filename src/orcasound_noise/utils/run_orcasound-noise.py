import pandas as pd
from orcasound_noise.pipeline.pipeline import NoiseAnalysisPipeline
from orcasound_noise.utils import Hydrophone
import datetime as dt
import pstats, cProfile
#from orcasound_noise.pipeline.acoustic_util import plot_spec

def main():
    pipeline = NoiseAnalysisPipeline(Hydrophone.PORT_TOWNSEND,
                                     delta_f=1, bands=None,
                                     delta_t=60, mode='safe')
    
    psd_path, broadband_path = pipeline.generate_parquet_file(dt.datetime(2023, 3, 22, 12, 0), 
                                                            dt.datetime(2023, 3, 22, 12, 10), 
                                                            upload_to_s3=False)

if __name__ == '__main__':
    cProfile.run("main()", "full_profile.pstats")
    stats = pstats.Stats("full_profile.pstats").strip_dirs().sort_stats("cumtime")
    stats.print_stats(30)           # top 30 cumulative-time functions
    stats.print_callees("wav_to_array")  # what wav_to_array calls and how long

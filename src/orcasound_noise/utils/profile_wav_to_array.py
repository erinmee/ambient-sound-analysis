# profile_wav_to_array.py
import pstats, cProfile, tempfile, datetime as dt
from orcasound_noise.pipeline.acoustic_util import wav_to_array

wav_path = "../test_files/live001.wav"  # point to a real input
t0 = dt.datetime(2023, 3, 22, 12, 0)

def main():
    # Keep kwargs the same as your real call to mirror behavior
    wav_to_array(wav_path, t0=t0, delta_t=60, delta_f=1, transforms=[], bands=None)

if __name__ == "__main__":
    cProfile.run("main()", "wav_profile.pstats")
    stats = pstats.Stats("wav_profile.pstats").strip_dirs().sort_stats("cumtime")
    stats.print_stats(30)           # top 30 cumulative-time functions
    stats.print_callees("wav_to_array")  # what wav_to_array calls and how long
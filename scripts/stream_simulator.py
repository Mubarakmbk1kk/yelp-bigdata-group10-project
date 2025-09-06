"""
Stream-simulator: write small CSV chunks into a folder to simulate streaming ingestion.
Run in a separate Colab cell to emit files while your Spark Structured Streaming job reads them.
"""
import pandas as pd, time, os
SRC = "/content/yelp_philly/yelp_philly_restaurants.csv"  # adjust if different
OUTDIR = "/content/stream_input"
CHUNKSIZE = 2000
os.makedirs(OUTDIR, exist_ok=True)
for i, chunk in enumerate(pd.read_csv(SRC, chunksize=CHUNKSIZE)):
    fname = os.path.join(OUTDIR, f"part_{i:04d}.csv")
    chunk.to_csv(fname, index=False)
    print("wrote", fname)
    time.sleep(2)

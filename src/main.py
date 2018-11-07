import argparse
import mongoDB_python

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This script computes the performance of mongoDB with Python.")
    parser.add_argument("--count", help="number of operations", required="True")
    parser.add_argument("--average", help="number of runs", default=10)
    args = parser.parse_args()

    count = int(args.count)
    average = int(args.average)
    mongoDB_python.compute_performance(count, average)


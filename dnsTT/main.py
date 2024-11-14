import time

from pathlib import Path
from threading import Thread


from db_postgres import PostgresDB, PCities, PSales, PBranches, PProducts


BATCH_SIZE = 100000


def db_insert(batch):
    pass


def timer(f):
    def g(*args, **kwargs):
        start_time = time.time()
        f()
        stop_time = time.time()
        print(stop_time - start_time)
    return g


def get_lines(file):
    with file.open("r", encoding="utf8") as f:
        for line in f:
            yield line

@timer
def main() -> None:
    data_dir = Path(Path.cwd().parent.parent / "DNSTestTask" / "test_task" / "data")
    for file in data_dir.iterdir():


        c = 0
        batch = list()
        for line in get_lines(file):


            if len(batch) < BATCH_SIZE:
                batch.append(data_dict)
            else:
                db_insert(batch)
                batch.clear()
        db_insert(batch)

    print(c)

if __name__ == '__main__':
    main()
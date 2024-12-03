import multiprocessing
import datetime


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            reading_file = file.readline()
            clear_n = reading_file.replace('\n', '')
            if not reading_file:
                break
            all_data.append(clear_n)

if __name__ == '__main__':

    filenames = [f'file {number}.txt' for number in range(1, 5)]
    start_time_line_call = datetime.datetime.now()
    for filename in filenames:
        read_info(filename)
    end_time_line_call = datetime.datetime.now()
    print(end_time_line_call - start_time_line_call)

    start_time_process = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end_time_process = datetime.datetime.now()
    print(end_time_process - start_time_process)
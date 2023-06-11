import request
import multiprocessing

def main():
    # referensi: https://www.geeksforgeeks.org/multiprocessing-python-set-1
    processes = []
    for i in range(5):
        processes.append(multiprocessing.Process(target=request.send_request, args=(i,)))
        processes[i].start()

    for process in processes:
        process.join()

if __name__ == "__main__":
    main()
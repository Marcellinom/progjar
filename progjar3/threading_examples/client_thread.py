import request
import threading

def main():
    # referensi: https://www.geeksforgeeks.org/multithreading-python-set-1/
    threads = []
    for i in range(5):
        threads.append(threading.Thread(target=request.send_request, args=(i,)))
        threads[i].start()
        
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
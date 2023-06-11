import request
import concurrent.futures

def main():
    # referensi: https://realpython.com/python-string-formatting/
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(request.send_request, range(5))

if __name__ == "__main__":
    main()
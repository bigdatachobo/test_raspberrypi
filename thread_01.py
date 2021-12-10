import threading, requests, time
 
def getHtml(url):

    sta = time.time()
    resp = requests.get(url)
    time.sleep(1)
    end = time.time()

    print(url, len(resp.text), ' chars')
    print(f"getHtml\nstart time: {sta}\nend time: {end}\ntime lapse: {time.time() - sta}")
    print()

def sum(low, high):

    sta = time.time()
    # total = 0
    # for i in range(low, high):
    #     total += i
    total = high*(high+1) / 2
    end = time.time()

    print("Subthread", total)
    print(f"Subthread\nstart time: {sta}\nend time: {end}\ntime lapse: {time.time() - sta}")
    print()
 
t1 = threading.Thread(target=getHtml, args=('http://google.com',))
t2 = threading.Thread(target=sum, args=(1, 100000))

if __name__ == '__main__':
    t1.start()
    t2.start()

    t1.join()
    t2.join()
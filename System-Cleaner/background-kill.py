import psutil

for proc in psutil.process_iter(['pid', 'name']):
    if 'python' in proc.info['name'].lower():
        try:
            proc.kill()
        except:
            pass

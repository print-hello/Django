import subprocess


p = subprocess.Popen('cmd.exe /c' + 'python E:\\django\\storenvy_django\\storenvy_web\\manage.py runserver 0.0.0.0:8000', 
                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
p.wait()
import os
import json
import base64
from glob import glob


class FileInterface:
    def list(self,params=[]):
        try:
            filelist = glob('*.*')
            return dict(status='OK',data=filelist)
        except Exception as e:
            return dict(status='ERROR',data=str(e))

    def get(self,params=[]):
        try:
            filename = params[0]
            if (filename == ''):
                return None
            fp = open(f"files/{filename}",'rb')
            isifile = base64.b64encode(fp.read()).decode()
            return dict(status='OK',data_namafile=filename,data_file=isifile)
        except Exception as e:
            return dict(status='ERROR',data=str(e))
    def upload(self, params=[]):
        try:
            filename = params[0]
            image_file = open(f"{filename}",'rb')
            isifile = base64.b64encode(image_file.read()).decode()
            if (isifile == ''):
                return None
            fp = open(f"files/{filename}",'wb')
            fp.write(base64.b64decode(isifile))
            return dict(status='OK', data_filename=filename)
        except Exception as e:
            return dict(status='ERROR',data=str(e))
    def delete(self, params=[]):
        try:
            filename = params[0]
            path = f"files/{filename}"
            if os.path.exists(path):
                os.remove(path)
                return dict(status='OK', message=f"File '{filename}' berhasil dihapus.")
            else:
                return dict(status='OK', message=f"File '{filename}' tidak ditemukan.")
        except Exception as e:
            return dict(status='ERROR',data=str(e))



if __name__=='__main__':
    f = FileInterface()
    print(f.list())
    print(f.get(['pokijan.jpg']))

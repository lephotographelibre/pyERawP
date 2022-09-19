from rawkit.raw import Raw
from rawkit.options import WhiteBalance

with Raw(filename='/ssdhome/jm/PycharmProjects/pyERawP/RAW/A.CR2') as raw:
    raw.options.white_balance = WhiteBalance(camera=False, auto=True)
    raw.save(filename='/ssdhome/jm/PycharmProjects/pyERawP/out/image.ppm')


from rawkit.raw import Raw
from rawkit.options import WhiteBalance

with Raw(filename='/ssdhome/jm/PycharmProjects/pyERawP/RAW/B.CR2') as raw:
    raw.options.white_balance = WhiteBalance(camera=False, auto=True)
    # raw.save(filename='/ssdhome/jm/PycharmProjects/pyERawP/out/image.ppm')
    raw.save_thumb(filename='/ssdhome/jm/PycharmProjects/pyERawP/out/B_CR2.jpg')
    raw.close()
    exit()

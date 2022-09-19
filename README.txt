Python Raw Extract JPEG Thumbnail

pyERawP - Python Extract RAW Preview

The Python Packages tool window provides the quickest and neat way to preview and install packages for the currently
selected Python interpreter. This window is enabled by default, and you can find it in the lower group of the tool windows.
At any time you can open it using the main menu:
View | Tool Windows | Python Packages.
rawkit --> Install

or pip install rawkit

https://github.com/photoshell/rawkit
https://rawkit.readthedocs.io/en/v0.6.0/


-- Extract Thumb

save_thumb(filename=None)
Save the thumbnail data.

Parameters:	filename (str) – The name of an image file to save.
Raises:	rawkit.errors.NoFileSpecified – If filename is None.
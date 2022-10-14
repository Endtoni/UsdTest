@echo off
set PATH=C:\Program Files\Autodesk\Maya2022\bin;C:\Program Files\Autodesk\MayaUSD\Maya2022\0.8.0\mayausd\USD3\bin;C:\Program Files\Autodesk\MayaUSD\Maya2022\0.8.0\mayausd\USD3\lib;%PATH%
set PYTHONPATH=C:\Program Files\Autodesk\MayaUSD\Maya2022\0.8.0\mayausd\USD3\lib\python;%PYTHONPATH%

mayapy -m pip install PyOpenGL==3.1.0
mayapy "C:\Program Files\Autodesk\MayaUSD\Maya2022\0.8.0\mayausd\USD3\bin\usdview" newName.usda
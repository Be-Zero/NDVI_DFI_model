# coding:utf-8
import arcpy
from arcpy.sa import *

arcpy.CheckOutExtension("spatial")  # 检查工具箱

in_path_V_M = r"E:\Sentinel-2\index\NDVI\2021\S2A_MSIL2A_20210103T033131_N9999_R018_T49SCT_20211210T111526.tif"  # 输入文件路径
in_path_D_M = r"E:\Sentinel-2\index\DFI\2021\S2A_MSIL2A_20210103T033131_N9999_R018_T49SCT_20211210T111526.tif"  # 输入文件路径

out_path_f_pv = r"E:\project\NDVI_DFI_model\f_pv\S2A_MSIL2A_20210103T033131_N9999_R018_T49SCT_20211210T111526.tif"
out_path_f_npv = r"E:\project\NDVI_DFI_model\f_npv\S2A_MSIL2A_20210103T033131_N9999_R018_T49SCT_20211210T111526.tif"
out_path_f_bs = r"E:\project\NDVI_DFI_model\f_bs\S2A_MSIL2A_20210103T033131_N9999_R018_T49SCT_20211210T111526.tif"
out_path_test = r"E:\TMP"

tmp_path = r"E:\TMP\S2A_MSIL2A_20210103T033131_N9999_R018_T49SCT_20211210T111526.tif"

(Raster(out_path_f_bs) + Raster(out_path_f_pv) + Raster(out_path_f_npv)).save(tmp_path)
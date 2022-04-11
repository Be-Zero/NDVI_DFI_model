# coding:utf-8
import arcpy
from arcpy.sa import *
import os

arcpy.CheckOutExtension("spatial")  # 检查工具箱

in_path_R = r"E:\Sentinel-2\2021\R\2021"  # 输入文件路径
in_path_NIR = r"E:\Sentinel-2\2021\NIR\2021"  # 输入文件路径
out_ndvi_path = r"E:\Sentinel-2\2021\NDVI\2021"  # 输出文件路径
tmp_path = r"E:\TMP"

arcpy.env.workspace = in_path_R  # 设置当前工作目录
files = arcpy.ListRasters("*", "tif")  # 查找目录中的 tif 格式文件
arcpy.env.workspace = tmp_path  # 设置当前工作目录
for file in files:  # 遍历
    try:
        ndvi = (Raster(in_path_NIR + os.sep + file) - Raster(in_path_R + os.sep + file)) / (Raster(in_path_NIR + os.sep + file) + Raster(in_path_R + os.sep + file))  # 计算 ndvi 指数
        ndvi.save(out_ndvi_path + os.sep + file)  # 将 ndvi 指数存为 tif 格式
        print file + " is done!"  # 完成提示

    except:
        print file + " has a bug."  # 筛选出错误文件

# file = r"S2B_MSIL2A_20211114T033009_N9999_R018_T49SCU_20211212T032357.tif"
# ndvi = (Raster(in_path_NIR + os.sep + file) - Raster(in_path_R + os.sep + file)) / (Raster(in_path_NIR + os.sep + file) + Raster(in_path_R + os.sep + file))  # 计算 ndvi 指数
# ndvi.save(out_ndvi_path + os.sep + file)  # 将 ndvi 指数存为 tif 格式
# coding:utf-8
import arcpy
from arcpy.sa import *
import os

arcpy.CheckOutExtension("spatial") # 检查工具箱
in_path_R = r"E:\Sentinel-2\2021\R\2021" # 输入文件路径
in_path_NIR = r"E:\Sentinel-2\2021\NIR\2021" # 输入文件路径
in_path_SWIR1 = r"E:\Sentinel-2\2021\SWIR1\2021" # 输入文件路径
in_path_SWIR2 = r"E:\Sentinel-2\2021\SWIR2\2021" # 输入文件路径
out_dfi_path = r"E:\Sentinel-2\2021\DFI\2021" # 输出文件路径
tmp_path = r"E:\TMP"

arcpy.env.workspace = in_path_R # 设置当前工作目录
files = arcpy.ListRasters("*", "tif") # 查找目录中的 tif 格式文件
arcpy.env.workspace = tmp_path # 设置当前工作目录
for file in files: # 遍历
    try:
        SWIR1 = Raster(in_path_SWIR1 + os.sep + file) # 读取波段
        SWIR2 = Raster(in_path_SWIR2 + os.sep + file) # 读取波段
        NIR = Raster(in_path_NIR + os.sep + file) # 读取波段
        R = Raster(in_path_R + os.sep + file) # 读取波段
        left = int(arcpy.GetRasterProperties_management(SWIR1, "LEFT").getOutput(0)) # 读取图像位置范围
        bottom = int(arcpy.GetRasterProperties_management(SWIR1, "BOTTOM").getOutput(0)) # 读取图像位置范围
        right = int(arcpy.GetRasterProperties_management(SWIR1, "RIGHT").getOutput(0)) # 读取图像位置范围
        top = int(arcpy.GetRasterProperties_management(SWIR1, "TOP").getOutput(0)) # 读取图像位置范围
        ones = CreateConstantRaster(1, "FLOAT", 10, Extent(left, bottom, right, top)) # 创建常量栅格
        dfi = 100 * (ones - SWIR1 / SWIR2) * R / NIR # 计算 dfi
        dfi.save(out_dfi_path + os.sep + file) # 将 dfi 指数存为 tif 格式
        print file + " is done!" # 完成提示
    except:
        print file + " has a bug." # 筛选出错误文件
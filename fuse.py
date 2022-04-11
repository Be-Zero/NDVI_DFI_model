# coding:utf-8
import arcpy
from arcpy.sa import *
import os

arcpy.CheckOutExtension("spatial") # 检查工具箱

in_path_R = r"E:\R\2021" # 输入文件路径
in_path_NIR = r"E:\NIR\2021" # 输入文件路径
in_path_SWIR1 = r"E:\SWIR1\2021" # 输入文件路径
in_path_SWIR2 = r"E:\SWIR2\2021" # 输入文件路径
in_path_C = r"E:\C\2021" # 输入文件路径
in_path_VRE1 = r"E:\VRE1\2021" # 输入文件路径
in_path_VRE2 = r"E:\VRE2\2021" # 输入文件路径
in_path_VRE3 = r"E:\VRE3\2021" # 输入文件路径
in_path_NN = r"E:\NN\2021" # 输入文件路径
in_path_WV = r"E:\WV\2021" # 输入文件路径
in_path_B = r"E:\B\2021" # 输入文件路径
in_path_G = r"E:\G\2021" # 输入文件路径

out_path = r"E:\fuse\2021" # 输出文件路径
tmp_path = r"E:\TMP"

arcpy.env.workspace = in_path_R # 设置当前工作目录
files = arcpy.ListRasters("*", "tif") # 查找目录中的 tif 格式文件
arcpy.env.workspace = tmp_path # 设置当前工作目录

for file in files: # 遍历
    try:
        arcpy.CompositeBands_management([Raster(in_path_C + os.sep + file),
                                         Raster(in_path_B + os.sep + file),
                                         Raster(in_path_G + os.sep + file),
                                         Raster(in_path_R + os.sep + file),
                                         Raster(in_path_VRE1 + os.sep + file),
                                         Raster(in_path_VRE2 + os.sep + file),
                                         Raster(in_path_VRE3 + os.sep + file),
                                         Raster(in_path_NIR + os.sep + file),
                                         Raster(in_path_NN + os.sep + file),
                                         Raster(in_path_WV + os.sep + file),
                                         Raster(in_path_SWIR1 + os.sep + file),
                                         Raster(in_path_SWIR2 + os.sep + file)],
                                         out_path + os.sep + file)
        print file + " is done!" # 完成提示
    except:
        print file + " has a bug." # 筛选出错误文件
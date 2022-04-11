# coding:utf-8
import arcpy
from arcpy.sa import *
import os

def get_R(out_path):
    files = arcpy.ListRasters("*", "tif")  # 查找目录中的 tif 格式文件
    for file in files: # 遍历
        try:
            arcpy.MakeRasterLayer_management(file, "red", band_index="1") # 提取 R 波段
            Raster("red").save(out_path + os.sep + file)
            print file + " is done!"  # 完成提示
        except:
            print file + " has a bug."  # 筛选出错误文件


def get_B(out_path):
    files = arcpy.ListRasters("*", "tif")  # 查找目录中的 tif 格式文件
    for file in files: # 遍历
        try:
            arcpy.MakeRasterLayer_management(file, "blue", band_index="3") # 提取 B 波段
            Raster("blue").save(out_path + os.sep + file)
            print file + " is done!"  # 完成提示
        except:
            print file + " has a bug."  # 筛选出错误文件


def get_G(out_path):
    files = arcpy.ListRasters("*", "tif")  # 查找目录中的 tif 格式文件
    for file in files: # 遍历
        try:
            arcpy.MakeRasterLayer_management(file, "green", band_index="2") # 提取 G 波段
            Raster("green").save(out_path + os.sep + file)
            print file + " is done!"  # 完成提示
        except:
            print file + " has a bug."  # 筛选出错误文件


def get_NIR(out_path):
    files = arcpy.ListRasters("*", "tif")  # 查找目录中的 tif 格式文件
    for file in files: # 遍历
        try:
            arcpy.MakeRasterLayer_management(file, "nir", band_index="4") # 提取 NIR 波段
            Raster("nir").save(out_path + os.sep + file)
            print file + " is done!"  # 完成提示
        except:
            print file + " has a bug."  # 筛选出错误文件


def get_VRE1(out_path):
    files = arcpy.ListRasters("*", "tif")  # 查找目录中的 tif 格式文件
    for file in files: # 遍历
        try:
            arcpy.MakeRasterLayer_management(file, "vre1", band_index="1") # 提取 R 波段
            arcpy.Resample_management(Raster("vre1"), out_path + os.sep + file, 10, "NEAREST")  # 对波段上采样
            print file + " is done!"  # 完成提示
        except:
            print file + " has a bug."  # 筛选出错误文件


def get_VRE2(out_path):
    files = arcpy.ListRasters("*", "tif")  # 查找目录中的 tif 格式文件
    for file in files: # 遍历
        try:
            arcpy.MakeRasterLayer_management(file, "vre2", band_index="2") # 提取 R 波段
            arcpy.Resample_management(Raster("vre2"), out_path + os.sep + file, 10, "NEAREST")  # 对波段上采样
            print file + " is done!"  # 完成提示
        except:
            print file + " has a bug."  # 筛选出错误文件


def get_VRE3(out_path):
    files = arcpy.ListRasters("*", "tif")  # 查找目录中的 tif 格式文件
    for file in files: # 遍历
        try:
            arcpy.MakeRasterLayer_management(file, "vre3", band_index="3") # 提取 R 波段
            arcpy.Resample_management(Raster("vre3"), out_path + os.sep + file, 10, "NEAREST")  # 对波段上采样
            print file + " is done!"  # 完成提示
        except:
            print file + " has a bug."  # 筛选出错误文件


def get_NN(out_path):
    files = arcpy.ListRasters("*", "tif")  # 查找目录中的 tif 格式文件
    for file in files: # 遍历
        try:
            arcpy.MakeRasterLayer_management(file, "nn", band_index="4") # 提取 R 波段
            arcpy.Resample_management(Raster("nn"), out_path + os.sep + file, 10, "NEAREST")  # 对波段上采样
            print file + " is done!"  # 完成提示
        except:
            print file + " has a bug."  # 筛选出错误文件


def get_SWIR1(out_path):
    files = arcpy.ListRasters("*", "tif")  # 查找目录中的 tif 格式文件
    for file in files: # 遍历
        try:
            arcpy.MakeRasterLayer_management(file, "swir1", band_index="6") # 提取 SWIR1 波段
            arcpy.Resample_management(Raster("swir1"), out_path + os.sep + file, 10, "NEAREST")  # 对波段上采样
            print file + " is done!"  # 完成提示
        except:
            print file + " has a bug."  # 筛选出错误文件


def get_SWIR2(out_path):
    files = arcpy.ListRasters("*", "tif")  # 查找目录中的 tif 格式文件
    for file in files: # 遍历
        try:
            arcpy.MakeRasterLayer_management(file, "swir2", band_index="5") # 提取 SWIR2 波段
            arcpy.Resample_management(Raster("swir2"), out_path + os.sep + file, 10, "NEAREST")  # 对波段上采样
            print file + " is done!"  # 完成提示
        except:
            print file + " has a bug."  # 筛选出错误文件


def get_C(out_path):
    files = arcpy.ListRasters("*", "tif")  # 查找目录中的 tif 格式文件
    for file in files: # 遍历
        try:
            arcpy.MakeRasterLayer_management(file, "c", band_index="1") # 提取 SWIR2 波段
            arcpy.Resample_management(Raster("c"), out_path + os.sep + file, 10, "NEAREST")  # 对波段上采样
            print file + " is done!"  # 完成提示
        except:
            print file + " has a bug."  # 筛选出错误文件


def get_WV(out_path):
    files = arcpy.ListRasters("*", "tif")  # 查找目录中的 tif 格式文件
    for file in files: # 遍历
        try:
            arcpy.MakeRasterLayer_management(file, "wv", band_index="2") # 提取 SWIR2 波段
            arcpy.Resample_management(Raster("wv"), out_path + os.sep + file, 10, "NEAREST")  # 对波段上采样
            print file + " is done!"  # 完成提示
        except:
            print file + " has a bug."  # 筛选出错误文件


if __name__ == "__main__":
    arcpy.CheckOutExtension("spatial") # 检查工具箱

    in_path_data1 = r"E:\Data1\2021" # 输入文件路径
    in_path_data2 = r"E:\Data2\2021" # 输入文件路径
    in_path_data3 = r"E:\Data3\2021"  # 输入文件路径

    C_path = r"E:\C\2021"  # 输出文件路径
    B_path = r"E:\B\2021"  # 输出文件路径
    G_path = r"E:\G\2021"  # 输出文件路径
    R_path = r"E:\R\2021" # 输出文件路径
    VRE1_path = r"E:\VRE1\2021"  # 输出文件路径
    VRE2_path = r"E:\VRE2\2021"  # 输出文件路径
    VRE3_path = r"E:\VRE3\2021"  # 输出文件路径
    NIR_path = r"E:\NIR\2021" # 输出文件路径
    NN_path = r"E:\NN\2021"  # 输出文件路径
    WV_path = r"E:\WV\2021"  # 输出文件路径
    SWIR1_path = r"E:\SWIR1\2021" # 输出文件路径
    SWIR2_path = r"E:\SWIR2\2021" # 输出文件路径

    arcpy.env.workspace = in_path_data1  # 设置当前工作目录
    print "begin to get R band:"
    get_R(R_path)
    print "begin to get G band:"
    get_G(G_path)
    print "begin to get B band:"
    get_B(B_path)
    print "begin to get NIR band:"
    get_NIR(NIR_path)

    arcpy.env.workspace = in_path_data2  # 设置当前工作目录
    print "begin to get SWIR1 band:"
    get_SWIR1(SWIR1_path)
    print "begin to get SWIR2 band:"
    get_SWIR2(SWIR2_path)
    print "begin to get VRE1 band:"
    get_VRE1(VRE1_path)
    print "begin to get VRE2 band:"
    get_VRE2(VRE2_path)
    print "begin to get VRE3 band:"
    get_VRE3(VRE3_path)
    print "begin to get NN band:"
    get_NN(NN_path)

    arcpy.env.workspace = in_path_data3  # 设置当前工作目录
    print "begin to get C band:"
    get_C(C_path)
    print "begin to get WV band:"
    get_WV(WV_path)
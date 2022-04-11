# coding:utf-8
import arcpy
from arcpy.sa import *

arcpy.CheckOutExtension("spatial")  # 检查工具箱

in_path_V_M = r"E:\Sentinel-2\index\NDVI\2021\S2A_MSIL2A_20210103T033131_N9999_R018_T49SCT_20211210T111526.tif"  # 输入文件路径
in_path_D_M = r"E:\Sentinel-2\index\DFI\2021\S2A_MSIL2A_20210103T033131_N9999_R018_T49SCT_20211210T111526.tif"  # 输入文件路径

out_path_f_pv = r"E:\project\NDVI_DFI_model\f_pv\S2A_MSIL2A_20210103T033131_N9999_R018_T49SCT_20211210T111526.tif"
out_path_f_npv = r"E:\project\NDVI_DFI_model\f_npv\S2A_MSIL2A_20210103T033131_N9999_R018_T49SCT_20211210T111526.tif"
out_path_f_bs = r"E:\project\NDVI_DFI_model\f_bs\S2A_MSIL2A_20210103T033131_N9999_R018_T49SCT_20211210T111526.tif"
out_path_f_rgb = r"E:\project\NDVI_DFI_model\f_rgb\S2A_MSIL2A_20210103T033131_N9999_R018_T49SCT_20211210T111526.tif"
tmp_path = r"E:\TMP"

arcpy.env.workspace = tmp_path  # 设置当前工作目录

V_M = Raster(in_path_V_M)  # NDVI
D_M = Raster(in_path_D_M)  # DFI

left = int(arcpy.GetRasterProperties_management(V_M, "LEFT").getOutput(0))  # 读取图像位置范围
bottom = int(arcpy.GetRasterProperties_management(V_M, "BOTTOM").getOutput(0))  # 读取图像位置范围
right = int(arcpy.GetRasterProperties_management(V_M, "RIGHT").getOutput(0))  # 读取图像位置范围
top = int(arcpy.GetRasterProperties_management(V_M, "TOP").getOutput(0))  # 读取图像位置范围

V_PV = CreateConstantRaster(0.303574, "FLOAT", 10, Extent(left, bottom, right, top))  # 创建常量栅格
V_NPV = CreateConstantRaster(-0.037383, "FLOAT", 10, Extent(left, bottom, right, top))  # 创建常量栅格
V_BS = CreateConstantRaster(-0.019250, "FLOAT", 10, Extent(left, bottom, right, top))  # 创建常量栅格
D_PV = CreateConstantRaster(9.621453, "FLOAT", 10, Extent(left, bottom, right, top))  # 创建常量栅格
D_NPV = CreateConstantRaster(12.017750, "FLOAT", 10, Extent(left, bottom, right, top))  # 创建常量栅格
D_BS = CreateConstantRaster(-2.838076, "FLOAT", 10, Extent(left, bottom, right, top))  # 创建常量栅格
ones = CreateConstantRaster(1, "FLOAT", 10, Extent(left, bottom, right, top))  # 创建常量栅格

f_pv = ((D_M - D_NPV) * (V_NPV - V_BS) - (V_M - V_NPV) * (D_NPV - D_BS)) / ((V_PV - V_NPV) * (D_BS - D_NPV) - (D_PV - D_NPV) * (V_BS - V_NPV))
f_pv.save(out_path_f_pv)

f_npv = ((D_M - D_PV) * (V_BS - V_PV) - (V_M - V_PV) * (D_BS - D_PV)) / ((V_PV - V_NPV) * (D_BS - D_PV) - (D_PV - D_NPV) * (V_BS - V_PV))
f_npv.save(out_path_f_npv)

f_bs = ((D_M-D_NPV) * (V_PV - V_NPV) - (V_M - V_NPV) * (D_PV - D_NPV)) / ((V_BS - V_NPV) * (D_NPV - D_PV) - (D_BS - D_NPV) * (V_NPV - V_PV))
f_bs.save(out_path_f_bs)

arcpy.CompositeBands_management([f_npv, f_pv, f_bs], out_path_f_rgb)
# coding:utf-8
import arcpy
from arcpy.sa import *


def get_ppi(ppi, in_path_ndvi, in_path_dfi, out_path_ndvi, out_path_dfi):
    ExtractByMask(Raster(in_path_ndvi), ppi).save(out_path_ndvi)  # 将 ndvi 指数存为 tif 格式
    ExtractByMask(Raster(in_path_dfi), ppi).save(out_path_dfi)  # 将 dfi 指数存为 tif 格式


if __name__ == "__main__":
    arcpy.CheckOutExtension("spatial") # 检查工具箱

    in_path_NDVI = r"E:\Sentinel-2\index\NDVI\2021\S2A_MSIL2A_20210103T033131_N9999_R018_T49SCT_20211210T111526.tif"  # 输入文件路径
    in_path_DFI = r"E:\Sentinel-2\index\DFI\2021\S2A_MSIL2A_20210103T033131_N9999_R018_T49SCT_20211210T111526.tif"  # 输入文件路径
    in_path_ppi = r"E:\project\NDVI_DFI_model\PPI\ppi.dat"  # 输入文件路径

    out_path_ndvi_5 = r"E:\project\NDVI_DFI_model\NDVI_5\S2A_MSIL2A_20210103T033131_N9999_R018_T49SCT_20211210T111526.tif"
    out_path_dfi_5 = r"E:\project\NDVI_DFI_model\DFI_5\S2A_MSIL2A_20210103T033131_N9999_R018_T49SCT_20211210T111526.tif"
    out_path_ndvi_10 = r"E:\project\NDVI_DFI_model\NDVI_10\S2A_MSIL2A_20210103T033131_N9999_R018_T49SCT_20211210T111526.tif"
    out_path_dfi_10 = r"E:\project\NDVI_DFI_model\DFI_10\S2A_MSIL2A_20210103T033131_N9999_R018_T49SCT_20211210T111526.tif"
    out_path_ndvi_3 = r"E:\project\NDVI_DFI_model\NDVI_3\S2A_MSIL2A_20210103T033131_N9999_R018_T49SCT_20211210T111526.tif"
    out_path_dfi_3 = r"E:\project\NDVI_DFI_model\DFI_3\S2A_MSIL2A_20210103T033131_N9999_R018_T49SCT_20211210T111526.tif"
    out_path_ndvi_0 = r"E:\project\NDVI_DFI_model\NDVI_0\S2A_MSIL2A_20210103T033131_N9999_R018_T49SCT_20211210T111526.tif"
    out_path_dfi_0 = r"E:\project\NDVI_DFI_model\DFI_0\S2A_MSIL2A_20210103T033131_N9999_R018_T49SCT_20211210T111526.tif"
    tmp_path = r"E:\TMP"

    arcpy.env.workspace = tmp_path  # 设置当前工作目录

    # extract new ppi
    ppi_ge_0 = ExtractByAttributes(Raster(in_path_ppi), "VALUE > 0")
    # ppi_ge_3 = ExtractByAttributes(Raster(in_path_ppi), "VALUE > 3")
    # ppi_ge_5 = ExtractByAttributes(Raster(in_path_ppi), "VALUE > 5")
    # ppi_ge_10 = ExtractByAttributes(Raster(in_path_ppi), "VALUE > 10")

    get_ppi(ppi_ge_0, in_path_NDVI, in_path_DFI, out_path_ndvi_0, out_path_dfi_0)
    # get_ppi(ppi_ge_3, in_path_NDVI, in_path_DFI, out_path_ndvi_3, out_path_dfi_3)
    # get_ppi(ppi_ge_5, in_path_NDVI, in_path_DFI, out_path_ndvi_5, out_path_dfi_5)
    # get_ppi(ppi_ge_10, in_path_NDVI, in_path_DFI, out_path_ndvi_10, out_path_dfi_10)

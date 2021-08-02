#  xrt_denoiser - $file.filename
#  Copyright (c) 2021. Minato Ryan
#  Last Edit:2021/7/29
#  This software is released under the MIT License.

LOG_PATH = "log.txt"

FOLDER_LIST = [{
    "new_path": "data/target_data/Catalogued",
    "ori_path": "data/ori_data",
    "log_path": "data/list/MyCatalogueA_Total.txt",
    },
    {
        "new_path": "data/target_data/Catalogued",
        "ori_path": "data/ori_data",
        "log_path": "data/list/MyCatalogueB_Total.txt"
    },
    {
        "new_path": "data/target_data/No_Catalogue",
        "ori_path": "data/ori_data",
        "log_path": "data/list/NoAll_Catalogue2019A_Total.txt"
    },
    {
        "new_path": "data/target_data/No_Catalogue",
        "ori_path": "data/ori_data",
        "log_path": "data/list/NoAll_CatalogueA_Total.txt"
    },
{
        "new_path": "data/target_data/No_Catalogue",
        "ori_path": "data/ori_data",
        "log_path": "data/list/NoAll_CatalogueAs_Total.txt"
    }
]
ML_IMAGES_ROOT = "data/train_data/"

BATCH_SIZE = 256
SHUFFLE_BUFFER_SIZE = 100
EPOCHS = 30

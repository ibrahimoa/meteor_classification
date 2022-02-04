import os
import random
from shutil import copyfile
from pathlib import Path
from os import getcwd
from os.path import join


# a SOURCE directory containing the files
# a TRAINING directory that a portion of the files will be copied to
# a TESTING directory that a portion of the files will be copie to
# a SPLIT SIZE to determine the portion
# The files should also be randomized, so that the training set is a random
# X% of the files, and the test set is the remaining files
# SO, for example, if SOURCE is PetImages/Cat, and SPLIT SIZE is .9
# Then 90% of the images in PetImages/Cat will be copied to the TRAINING dir
# and 10% of the images will be copied to the TESTING dir
# Also -- All images should be checked, and if they have a zero file length,
# they will not be copied over

def split_data(SOURCE, TRAINING, VALIDATION, TESTING, SPLIT_TRAIN, SPLIT_VALID, SPLIT_TEST):
    # YOUR CODE STARTS HERE
    if SPLIT_TEST + SPLIT_TRAIN + SPLIT_VALID != 1:
        print('Split sum must de 1')
        return
    contentList = os.listdir(SOURCE)

    random.sample(contentList, len(contentList))
    for i in range(int(SPLIT_TRAIN * len(contentList))):
        if i % 300 == 0:
            print(i)
        try:
            copyfile(os.path.join(SOURCE, contentList[i]), os.path.join(TRAINING, contentList[i]))
        except:
            pass
    for i in range(int(SPLIT_TRAIN * len(contentList)), int((SPLIT_TRAIN + SPLIT_VALID) * len(contentList))):
        if i % 300 == 0:
            print(i)
        try:
            copyfile(os.path.join(SOURCE, contentList[i]), os.path.join(VALIDATION, contentList[i]))
        except:
            pass
    for i in range(int((SPLIT_TRAIN + SPLIT_VALID) * len(contentList)), len(contentList)):
        if i % 300 == 0:
            print(i)
        try:
            copyfile(os.path.join(SOURCE, contentList[i]), os.path.join(TESTING, contentList[i]))
        except:
            pass


data_dir = join(Path(getcwd()).parent, "meteorData")

METEORS_SOURCE_DIR = join(data_dir, "meteors")
NON_METEORS_SOURCE_DIR = join(data_dir, "non_meteors")

TRAIN_METEORS_DIR = join(data_dir, "train/meteors")
VALIDATION_METEORS_DIR = join(data_dir, "validation/meteors")
TEST_METEORS_DIR = join(data_dir, "test/meteors")

TRAIN_NON_METEORS_DIR = join(data_dir, "train/non_meteors")
VALIDATION_NON_METEORS_DIR = join(data_dir, "validation/non_meteors")
TEST_NON_METEORS_DIR = join(data_dir, "test/non_meteors")

if __name__ == "__main__":
    split_data(METEORS_SOURCE_DIR, TRAIN_METEORS_DIR, VALIDATION_METEORS_DIR, TEST_METEORS_DIR, 0.85, 0.15, 0.00)
    split_data(NON_METEORS_SOURCE_DIR, TRAIN_NON_METEORS_DIR, VALIDATION_NON_METEORS_DIR, TEST_NON_METEORS_DIR, 0.90,
               0.10, 0.00)

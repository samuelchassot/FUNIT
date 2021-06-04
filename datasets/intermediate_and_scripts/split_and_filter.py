#split and filter the maximum amount of images according to the most restricting datasets in INIT dataset

from math import floor

#filenames of the files containing the paths for the dataset images
TRAIN_FILENAME_PATHS = ["cloudy_list.txt", "night_list.txt", "sunny_list.txt"]
TEST_FILENAME_PATHS  = ["rainy_list.txt"]

#filenames for the output files containing the paths to the corresponding images
TRAIN_FILENAME = "roads_list_train.txt"
TEST_FILENAME  = "roads_list_test.txt"

#this corresponds to an overall of taking about 5% of the INIT dataset
NUMBER_OF_IMAGES_PER_CLASS = 600

#return all the paths in the corresponding files
def retrieve_paths(filename_paths):
    paths_list = []
    for filename_path in filename_paths:
        with open(filename_path) as file:
            paths = file.readlines()
            paths_list.append(paths)
    return paths_list

train_paths_list = retrieve_paths(TRAIN_FILENAME_PATHS)
test_paths_list  = retrieve_paths(TEST_FILENAME_PATHS)

#find a limiting class
min_train_paths = len(min(train_paths_list, key=lambda p: len(p)))
min_test_paths  = len(min(train_paths_list, key=lambda p: len(p)))

if min_train_paths < NUMBER_OF_IMAGES_PER_CLASS or min_test_paths < NUMBER_OF_IMAGES_PER_CLASS:
    raise Exception("There is not enough images for at least one class < NUMBER_OF_IMAGES_PER_CLASS={}".format(NUMBER_OF_IMAGES_PER_CLASS))

def filter_and_save_datasets(filename, paths_list, number_of_images=NUMBER_OF_IMAGES_PER_CLASS):
    with open(filename, 'w') as result_file:
        for path in paths_list:
            for i in range(0, len(path), floor(len(path)/number_of_images)):
                result_file.write(path[i])

filter_and_save_datasets(TRAIN_FILENAME, train_paths_list)
filter_and_save_datasets(TEST_FILENAME,  test_paths_list)

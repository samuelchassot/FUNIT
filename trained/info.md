# trained images generated results

3 - 4 - 5: with the reduced dataset (after freeing space on the cluster), with night as test 
    (datasets are here: https://github.com/danielementary/Unsupervised-Image-to-Image-Translation/tree/64f476012bb29188ca70379c236b509cb89621d3
        and they are in night_list.txt, rainy_list.txt, to_keep_sunny.txt, to_keep_cloud.txt)

    from the 20.04.2021 to the 02.05.2021, with config:

    ```
    # Copyright (C) 2019 NVIDIA Corporation.  All rights reserved.
    # Licensed under the CC BY-NC-SA 4.0 license
    # (https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode).

    # logger options
    image_save_iter: 5000         # How often do you want to save output images during training
    image_display_iter: 100       # How often do you want to display output images during training
    snapshot_save_iter: 5000      # How often do you want to save trained models
    log_iter: 1                   # How often do you want to log the training stats

    # optimization options
    max_iter: 500000              # maximum number of training iterations
    weight_decay: 0.0001          # weight decay
    lr_gen: 0.0001                # learning rate for the generator
    lr_dis: 0.0001                # learning rate for the discriminator
    init: kaiming                 # initialization [gaussian/kaiming/xavier/orthogonal]
    gan_w: 1                      # weight of adversarial loss for image translation
    fm_w: 1                       # weight on distance between gan features of style and translated image
    r_w: 0.1                      # weight of image reconstruction loss

    # model options
    gen:
    nf: 64                      # number of base filters in the generator
    n_res_blks: 2               # number of residual blocks in content encoder/decoder
    nf_mlp: 256                 # number of base filters in MLP module
    latent_dim: 64              # dimension of the latent code for the class model
    n_mlp_blks: 3               # number of mlp blocks
    n_downs_content: 3          # number of downsampling layers in content encoder
    n_downs_class: 4            # number of downsampling layers in class model encoder
    dis:
    nf: 64                      # base number of filters
    n_res_blks: 10              # number of residual blocks in the discriminator
    num_classes: 4              # number of classes in the training set

    # data options
    num_workers: 4
    batch_size: 4
    new_size: 140                 # first resize the shortest image side to this size
    crop_image_height: 128        # random crop image of this height
    crop_image_width: 128         # random crop image of this width
    data_folder_train: ./datasets/roads
    data_list_train: ./datasets/roads_list_train.txt
    data_folder_test: ./datasets/roads
    data_list_test: ./datasets/roads_list_test.txt
    ```

    3: 22.04.2021
    4: 27.04.2021
    5: 29.04.2021

    We could generate proper results for that run with the folder `outputs_02.05.2021`


    dataset is here: https://github.com/samuelchassot/FUNIT/tree/58d203e6f71448ec88de05047d8eb4de7c03321c


6: reduced dataset with same number of images in all classes (set to the number of images in the smallest i.e. night), with night as test. intermediary tests during training
    (datasets are here: https://github.com/danielementary/Unsupervised-Image-to-Image-Translation/tree/ac4b4cf0fc17b814bac2525224f8793da954379d
        and they are reduced_cloudy.txt reduced_rainy.txt reduced_night.txt reduced_sunny.txt )
7: reduced dataset with same number of images in all classes (set to the number of images in the smallest i.e. night), with night as test. After 480'000 iterations
    (datasets are here: https://github.com/danielementary/Unsupervised-Image-to-Image-Translation/tree/ac4b4cf0fc17b814bac2525224f8793da954379d
        and they are reduced_cloudy.txt reduced_rainy.txt reduced_night.txt reduced_sunny.txt )

8: with retinanet classes: all classes are sunny, cloudy, rainy, night, cloudy_XXX, ... randomly attributed to test/train with a ratio of 85% in train. Problem: we want all nights as test, I made a mistake.
    after 230'000 iterations (see : commit dea96e03b7287ab54104d95de109cc39f102db38 on FUNIT 
                                            https://github.com/danielementary/Unsupervised-Image-to-Image-Translation/tree/dea96e03b7287ab54104d95de109cc39f102db38/dataset/retinanet/train_test)






# outputs folders

- `/ivrldata1/students/2021-spring-cs413-team3/FUNIT_outputs/outputs_20.04.2021/` and `/scratch/2021-spring-cs413-team3/Unsupervised-Image-to-Image-Translation/FUNIT/outputs_02.05.2021/` are the same config but the first one didn't want to resume so I did a new one. Both ran on the same dataset and the 1st for 250'000 it and the second for 470'000 it

stored now `/ivrldata1/students/2021-spring-cs413-team3/models/outputs_unbalanced_470K`
    Dataset is available here: https://github.com/samuelchassot/FUNIT/tree/519c61faaf7873e61a324eddabf1f0d6498c3e3b

        ```
        # Copyright (C) 2019 NVIDIA Corporation.  All rights reserved.
        # Licensed under the CC BY-NC-SA 4.0 license
        # (https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode).

        # logger options
        image_save_iter: 5000         # How often do you want to save output images during training
        image_display_iter: 100       # How often do you want to display output images during training
        snapshot_save_iter: 5000      # How often do you want to save trained models
        log_iter: 1                   # How often do you want to log the training stats

        # optimization options
        max_iter: 500000              # maximum number of training iterations
        weight_decay: 0.0001          # weight decay
        lr_gen: 0.0001                # learning rate for the generator
        lr_dis: 0.0001                # learning rate for the discriminator
        init: kaiming                 # initialization [gaussian/kaiming/xavier/orthogonal]
        gan_w: 1                      # weight of adversarial loss for image translation
        fm_w: 1                       # weight on distance between gan features of style and translated image
        r_w: 0.1                      # weight of image reconstruction loss

        # model options
        gen:
        nf: 64                      # number of base filters in the generator
        n_res_blks: 2               # number of residual blocks in content encoder/decoder
        nf_mlp: 256                 # number of base filters in MLP module
        latent_dim: 64              # dimension of the latent code for the class model
        n_mlp_blks: 3               # number of mlp blocks
        n_downs_content: 3          # number of downsampling layers in content encoder
        n_downs_class: 4            # number of downsampling layers in class model encoder
        dis:
        nf: 64                      # base number of filters
        n_res_blks: 10              # number of residual blocks in the discriminator
        num_classes: 4              # number of classes in the training set

        # data options
        num_workers: 4
        batch_size: 4
        new_size: 140                 # first resize the shortest image side to this size
        crop_image_height: 128        # random crop image of this height
        crop_image_width: 128         # random crop image of this width
        data_folder_train: ./datasets/roads
        data_list_train: ./datasets/roads_list_train.txt
        data_folder_test: ./datasets/roads
        data_list_test: ./datasets/roads_list_test.txt
        ```

- `/scratch/2021-spring-cs413-team3/Unsupervised-Image-to-Image-Translation/FUNIT/trained/outputs_used_for_7/` is the one with the smaller dataset with the same number of images in each class, test is night. 

stored now `/ivrldata1/students/2021-spring-cs413-team3/models/outputs_balanced_483K`
    Stopped after: 483'000 iterations
    Dataset is available here: https://github.com/samuelchassot/FUNIT/tree/b90c4610ff856a1780264c18a469ca46a5f0d46d
    (reduced one, see config for name)

        ```
        # Copyright (C) 2019 NVIDIA Corporation.  All rights reserved.
        # Licensed under the CC BY-NC-SA 4.0 license
        # (https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode).

        # logger options
        image_save_iter: 5000         # How often do you want to save output images during training
        image_display_iter: 100       # How often do you want to display output images during training
        snapshot_save_iter: 5000      # How often do you want to save trained models
        log_iter: 1                   # How often do you want to log the training stats

        # optimization options
        max_iter: 500000              # maximum number of training iterations
        weight_decay: 0.0001          # weight decay
        lr_gen: 0.0001                # learning rate for the generator
        lr_dis: 0.0001                # learning rate for the discriminator
        init: kaiming                 # initialization [gaussian/kaiming/xavier/orthogonal]
        gan_w: 1                      # weight of adversarial loss for image translation
        fm_w: 1                       # weight on distance between gan features of style and translated image
        r_w: 0.1                      # weight of image reconstruction loss

        # model options
        gen:
        nf: 64                      # number of base filters in the generator
        n_res_blks: 2               # number of residual blocks in content encoder/decoder
        nf_mlp: 256                 # number of base filters in MLP module
        latent_dim: 64              # dimension of the latent code for the class model
        n_mlp_blks: 3               # number of mlp blocks
        n_downs_content: 3          # number of downsampling layers in content encoder
        n_downs_class: 4            # number of downsampling layers in class model encoder
        dis:
        nf: 64                      # base number of filters
        n_res_blks: 10              # number of residual blocks in the discriminator
        num_classes: 4              # number of classes in the training set

        # data options
        num_workers: 4
        batch_size: 8
        new_size: 140                 # first resize the shortest image side to this size
        crop_image_height: 128        # random crop image of this height
        crop_image_width: 128         # random crop image of this width
        data_folder_train: ./datasets/roads
        data_list_train: ./datasets/roads_train_reduced.txt
        data_folder_test: ./datasets/roads
        data_list_test: ./datasets/roads_test_reduced.txt
        ```

- `/scratch/2021-spring-cs413-team3/Unsupervised-Image-to-Image-Translation/FUNIT/trained/outputs_retinanet_random_classes_used_for_8/` with classes outputs by retinanet


- `/ivrldata1/students/2021-spring-cs413-team3/models/outputs_9_with_retinanet_500K`: model trained with images using retinanet, with all night classes as test and others as train. trained for 500K iterations

    Datasets are here: https://github.com/samuelchassot/FUNIT/commit/4e86695a6179cc12925f70c381218951d8038c09
    `training_with_retinanet.txt`, `testing_with_retinanet.txt`

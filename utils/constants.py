def nb_dims(dataset):
    if dataset == "uciadl":
        return 3
    if dataset == "uciasl3":
        return 8
    if dataset == "uciasl95":
        return 8
    if dataset == "uciarabic":
        return 13
    else:
        return 1

def nb_classes(dataset):
    if dataset == "uciadl":
        return 7
    if dataset == "uciasl3":
        return 3
    if dataset == "uciasl95":
        return 95 
    if dataset == "uciarabic":
        return 10
    if dataset == "ucihillvalley":
        return 2
    if dataset == "ucihillvalleynoise":
        return 2 
    if dataset == "50words":
        return 50 #270
    if dataset == "Adiac":
        return 37 #176
    if dataset == "ArrowHead":
        return 3 #251
    if dataset == "Beef":
        return 5 #470
    if dataset == "BeetleFly":
        return 2 #512
    if dataset == "BirdChicken":
        return 2 #512
    if dataset == "Car":
        return 4 #577
    if dataset == "CBF":
        return 3 #128
    if dataset == "ChlorineConcentration":
        return 3 #166
    if dataset == "CinC_ECG_torso":
        return 4 #1639
    if dataset == "Coffee":
        return 2 #286
    if dataset == "Computers":
        return 2 #720
    if dataset == "Cricket_X":
        return 12 #300
    if dataset == "Cricket_Y":
        return 12 #300
    if dataset == "Cricket_Z":
        return 12 #300
    if dataset == "DiatomSizeReduction":
        return 4 #345
    if dataset == "DistalPhalanxOutlineAgeGroup":
        return 3 #80
    if dataset == "DistalPhalanxOutlineCorrect":
        return 2 #80
    if dataset == "DistalPhalanxTW":
        return 6 #80
    if dataset == "Earthquakes":
        return 2 #512
    if dataset == "ECG200":
        return 2 #96
    if dataset == "ECG5000":
        return 5 #140
    if dataset == "ECGFiveDays":
        return 2 #136
    if dataset == "ElectricDevices":
        return 7 #96
    if dataset == "FaceAll":
        return 14 # 131
    if dataset == "FaceFour":
        return 4 # 350
    if dataset == "FacesUCR":
        return 14 # 131
    if dataset == "FISH":
        return 7 # 463
    if dataset == "FordA":
        return 2 #500
    if dataset == "FordB":
        return 2 # 500
    if dataset == "Gun_Point":
        return 2 # 150
    if dataset == "Ham":
        return 2 # 431
    if dataset == "HandOutlines":
        return 2 # 2709
    if dataset == "Haptics":
        return 5 # 1092
    if dataset == "Herring":
        return 2 # 512
    if dataset == "InlineSkate":
        return 7 # 1882
    if dataset == "InsectWingbeatSound":
        return 11 # 256
    if dataset == "ItalyPowerDemand":
        return 2 # 24
    if dataset == "LargeKitchenAppliances":
        return 3 # 720
    if dataset == "Lighting2":
        return 2 # 637
    if dataset == "Lighting7":
        return 7 # 319
    if dataset == "MALLAT":
        return 8 # 1024
    if dataset == "Meat":
        return 3 # 448
    if dataset == "MedicalImages":
        return 10 # 99
    if dataset == "MiddlePhalanxOutlineAgeGroup":
        return 3 #80
    if dataset == "MiddlePhalanxOutlineCorrect":
        return 2 #80
    if dataset == "MiddlePhalanxTW":
        return 6 #80
    if dataset == "MoteStrain":
        return 2 #84
    if dataset == "NonInvasiveFatalECG_Thorax1":
        return 42 #750
    if dataset == "NonInvasiveFatalECG_Thorax2":
        return 42 #750
    if dataset == "OliveOil":
        return 4 #570
    if dataset == "OSULeaf":
        return 6 #427
    if dataset == "PhalangesOutlinesCorrect":
        return 2 #80
    if dataset == "Phoneme":
        return 39 #1024
    if dataset == "Plane":
        return 7 #144
    if dataset == "ProximalPhalanxOutlineAgeGroup":
        return 3 #80
    if dataset == "ProximalPhalanxOutlineCorrect":
        return 2 #80
    if dataset == "ProximalPhalanxTW":
        return 6 #80
    if dataset == "RefrigerationDevices":
        return 3 #720
    if dataset == "ScreenType":
        return 3 #720
    if dataset == "ShapeletSim":
        return 2 #500
    if dataset == "ShapesAll":
        return 60 # 512
    if dataset == "SmallKitchenAppliances":
        return 3 #720
    if dataset == "SonyAIBORobotSurfaceII":
        return 2 #65
    if dataset == "SonyAIBORobotSurface":
        return 2 #70
    if dataset == "StarLightCurves":
        return 3 #1024
    if dataset == "Strawberry":
        return 2 #235
    if dataset == "SwedishLeaf":
        return 15 # 128
    if dataset == "Symbols":
        return 6 #398
    if dataset == "synthetic_control":
        return 6 #60
    if dataset == "ToeSegmentation1":
        return 2 #277
    if dataset == "ToeSegmentation2":
        return 2 #343
    if dataset == "Trace":
        return 4 #275
    if dataset == "TwoLeadECG":
        return 2 #82
    if dataset == "Two_Patterns":
        return 4 #128
    if dataset == "uWaveGestureLibrary_X":
        return 8 # 315
    if dataset == "uWaveGestureLibrary_Y":
        return 8 # 315
    if dataset == "uWaveGestureLibrary_Z":
        return 8 # 315
    if dataset == "UWaveGestureLibraryAll":
        return 8 # 945
    if dataset == "wafer":
        return 2 #152
    if dataset == "Wine":
        return 2 #234
    if dataset == "WordsSynonyms":
        return 25 #270
    if dataset == "Worms":
        return 5 #900
    if dataset == "WormsTwoClass":
        return 2 #900
    if dataset == "yoga":
        return 2 #426
    exit('missing dataset')


def class_modifier_add(dataset):
    if dataset == "50words":
        return -1 #270
    if dataset == "Adiac":
        return -1 #176
    if dataset == "ArrowHead":
        return 0 #251
    if dataset == "Beef":
        return -1 #470
    if dataset == "BeetleFly":
        return -1 #512
    if dataset == "BirdChicken":
        return -1 #512
    if dataset == "Car":
        return -1 #577
    if dataset == "CBF":
        return -1 #128
    if dataset == "ChlorineConcentration":
        return -1 #166
    if dataset == "CinC_ECG_torso":
        return -1 #1639
    if dataset == "Coffee":
        return 0 #286
    if dataset == "Computers":
        return -1 #720
    if dataset == "Cricket_X":
        return -1 #300
    if dataset == "Cricket_Y":
        return -1 #300
    if dataset == "Cricket_Z":
        return -1 #300
    if dataset == "DiatomSizeReduction":
        return -1 #345
    if dataset == "DistalPhalanxOutlineAgeGroup":
        return -1 #80
    if dataset == "DistalPhalanxOutlineCorrect":
        return 0 #80
    if dataset == "DistalPhalanxTW":
        return -3 #80
    if dataset == "Earthquakes":
        return 0 #512
    if dataset == "ECG200":
        return 1 #96
    if dataset == "ECG5000":
        return -1 #140
    if dataset == "ECGFiveDays":
        return -1 #136
    if dataset == "ElectricDevices":
        return -1 #96
    if dataset == "FaceAll":
        return -1 # 131
    if dataset == "FaceFour":
        return -1 # 350
    if dataset == "FacesUCR":
        return -1 # 131
    if dataset == "FISH":
        return -1 # 463
    if dataset == "FordA":
        return 1 #500
    if dataset == "FordB":
        return 1 # 500
    if dataset == "Gun_Point":
        return -1 # 150
    if dataset == "Ham":
        return -1 # 431
    if dataset == "HandOutlines":
        return 0 # 2709
    if dataset == "Haptics":
        return -1 # 1092
    if dataset == "Herring":
        return -1 # 512
    if dataset == "InlineSkate":
        return -1 # 1882
    if dataset == "InsectWingbeatSound":
        return -1 # 256
    if dataset == "ItalyPowerDemand":
        return -1 # 24
    if dataset == "LargeKitchenAppliances":
        return -1 # 720
    if dataset == "Lighting2":
        return 1 # 637
    if dataset == "Lighting7":
        return 0 # 319
    if dataset == "MALLAT":
        return -1 # 1024
    if dataset == "Meat":
        return -1 # 448
    if dataset == "MedicalImages":
        return -1 # 99
    if dataset == "MiddlePhalanxOutlineAgeGroup":
        return -1 #80
    if dataset == "MiddlePhalanxOutlineCorrect":
        return 0 #80
    if dataset == "MiddlePhalanxTW":
        return -3 #80
    if dataset == "MoteStrain":
        return -1 #84
    if dataset == "NonInvasiveFatalECG_Thorax1":
        return -1 #750
    if dataset == "NonInvasiveFatalECG_Thorax2":
        return -1 #750
    if dataset == "OliveOil":
        return -1 #570
    if dataset == "OSULeaf":
        return -1 #427
    if dataset == "PhalangesOutlinesCorrect":
        return 0 #80
    if dataset == "Phoneme":
        return -1 #1024
    if dataset == "Plane":
        return -1 #144
    if dataset == "ProximalPhalanxOutlineAgeGroup":
        return -1 #80
    if dataset == "ProximalPhalanxOutlineCorrect":
        return 0 #80
    if dataset == "ProximalPhalanxTW":
        return -3 #80
    if dataset == "RefrigerationDevices":
        return -1 #720
    if dataset == "ScreenType":
        return -1 #720
    if dataset == "ShapeletSim":
        return 0 #500
    if dataset == "ShapesAll":
        return -1 # 512
    if dataset == "SmallKitchenAppliances":
        return -1 #720
    if dataset == "SonyAIBORobotSurfaceII":
        return -1 #65
    if dataset == "SonyAIBORobotSurface":
        return -1 #70
    if dataset == "StarLightCurves":
        return -1 #1024
    if dataset == "Strawberry":
        return -1 #235
    if dataset == "SwedishLeaf":
        return -1 # 128
    if dataset == "Symbols":
        return -1 #398
    if dataset == "synthetic_control":
        return -1 #60
    if dataset == "ToeSegmentation1":
        return 0 #277
    if dataset == "ToeSegmentation2":
        return 0 #343
    if dataset == "Trace":
        return -1 #275
    if dataset == "TwoLeadECG":
        return -1 #82
    if dataset == "Two_Patterns":
        return -1 #128
    if dataset == "uWaveGestureLibrary_X":
        return -1 # 315
    if dataset == "uWaveGestureLibrary_Y":
        return -1 # 315
    if dataset == "uWaveGestureLibrary_Z":
        return -1 # 315
    if dataset == "UWaveGestureLibraryAll":
        return -1 # 945
    if dataset == "wafer":
        return 1 #152
    if dataset == "Wine":
        return -1 #234
    if dataset == "WordsSynonyms":
        return -1 #270
    if dataset == "Worms":
        return -1 #900
    if dataset == "WormsTwoClass":
        return -1 #900
    if dataset == "yoga":
        return -1 #426
    exit('missing dataset')

def class_modifier_multi(dataset):
    if dataset == "50words":
        return 1 #270
    if dataset == "Adiac":
        return 1 #176
    if dataset == "ArrowHead":
        return 1 #251
    if dataset == "Beef":
        return 1 #470
    if dataset == "BeetleFly":
        return 1 #512
    if dataset == "BirdChicken":
        return 1 #512
    if dataset == "Car":
        return 1 #577
    if dataset == "CBF":
        return 1 #128
    if dataset == "ChlorineConcentration":
        return 1 #166
    if dataset == "CinC_ECG_torso":
        return 1 #1639
    if dataset == "Coffee":
        return 1 #286
    if dataset == "Computers":
        return 1 #720
    if dataset == "Cricket_X":
        return 1 #300
    if dataset == "Cricket_Y":
        return 1 #300
    if dataset == "Cricket_Z":
        return 1 #300
    if dataset == "DiatomSizeReduction":
        return 1 #345
    if dataset == "DistalPhalanxOutlineAgeGroup":
        return 1 #80
    if dataset == "DistalPhalanxOutlineCorrect":
        return 1 #80
    if dataset == "DistalPhalanxTW":
        return 1 #80
    if dataset == "Earthquakes":
        return 1 #512
    if dataset == "ECG200":
        return 0.5 #96
    if dataset == "ECG5000":
        return 1 #140
    if dataset == "ECGFiveDays":
        return 1 #136
    if dataset == "ElectricDevices":
        return 1 #96
    if dataset == "FaceAll":
        return 1 # 131
    if dataset == "FaceFour":
        return 1 # 350
    if dataset == "FacesUCR":
        return 1 # 131
    if dataset == "FISH":
        return 1 # 463
    if dataset == "FordA":
        return 0.5 #500
    if dataset == "FordB":
        return 0.5 # 500
    if dataset == "Gun_Point":
        return 1 # 150
    if dataset == "Ham":
        return 1 # 431
    if dataset == "HandOutlines":
        return 1 # 2709
    if dataset == "Haptics":
        return 1 # 1092
    if dataset == "Herring":
        return 1 # 512
    if dataset == "InlineSkate":
        return 1 # 1882
    if dataset == "InsectWingbeatSound":
        return 1 # 256
    if dataset == "ItalyPowerDemand":
        return 1 # 24
    if dataset == "LargeKitchenAppliances":
        return 1 # 720
    if dataset == "Lighting2":
        return 0.5 # 637
    if dataset == "Lighting7":
        return 1 # 319
    if dataset == "MALLAT":
        return 1 # 1024
    if dataset == "Meat":
        return 1 # 448
    if dataset == "MedicalImages":
        return 1 # 99
    if dataset == "MiddlePhalanxOutlineAgeGroup":
        return 1 #80
    if dataset == "MiddlePhalanxOutlineCorrect":
        return 1 #80
    if dataset == "MiddlePhalanxTW":
        return 1 #80
    if dataset == "MoteStrain":
        return 1 #84
    if dataset == "NonInvasiveFatalECG_Thorax1":
        return 1 #750
    if dataset == "NonInvasiveFatalECG_Thorax2":
        return 1 #750
    if dataset == "OliveOil":
        return 1 #570
    if dataset == "OSULeaf":
        return 1 #427
    if dataset == "PhalangesOutlinesCorrect":
        return 1 #80
    if dataset == "Phoneme":
        return 1 #1024
    if dataset == "Plane":
        return 1 #144
    if dataset == "ProximalPhalanxOutlineAgeGroup":
        return 1 #80
    if dataset == "ProximalPhalanxOutlineCorrect":
        return 1 #80
    if dataset == "ProximalPhalanxTW":
        return 1 #80
    if dataset == "RefrigerationDevices":
        return 1 #720
    if dataset == "ScreenType":
        return 1 #720
    if dataset == "ShapeletSim":
        return 1 #500
    if dataset == "ShapesAll":
        return 1 # 512
    if dataset == "SmallKitchenAppliances":
        return 1 #720
    if dataset == "SonyAIBORobotSurfaceII":
        return 1 #65
    if dataset == "SonyAIBORobotSurface":
        return 1 #70
    if dataset == "StarLightCurves":
        return 1 #1024
    if dataset == "Strawberry":
        return 1 #235
    if dataset == "SwedishLeaf":
        return 1 # 128
    if dataset == "Symbols":
        return 1 #398
    if dataset == "synthetic_control":
        return 1 #60
    if dataset == "ToeSegmentation1":
        return 1 #277
    if dataset == "ToeSegmentation2":
        return 1 #343
    if dataset == "Trace":
        return 1 #275
    if dataset == "TwoLeadECG":
        return 1 #82
    if dataset == "Two_Patterns":
        return 1 #128
    if dataset == "uWaveGestureLibrary_X":
        return 1 # 315
    if dataset == "uWaveGestureLibrary_Y":
        return 1 # 315
    if dataset == "uWaveGestureLibrary_Z":
        return 1 # 315
    if dataset == "UWaveGestureLibraryAll":
        return 1 # 945
    if dataset == "wafer":
        return 0.5 #152
    if dataset == "Wine":
        return 1 #234
    if dataset == "WordsSynonyms":
        return 1 #270
    if dataset == "Worms":
        return 1 #900
    if dataset == "WormsTwoClass":
        return 1 #900
    if dataset == "yoga":
        return 1 #426
    exit('missing dataset')

def max_seq_len(dataset):
    if dataset == "uciadl":
        return 500
    if dataset == "uciasl3":
        return 100
    if dataset == "uciasl95":
        return 100
    if dataset == "uciarabic":
        return 40
    if dataset == "ucihillvalley":
        return 100
    if dataset == "ucihillvalleynoise":
        return 100
    if dataset == "50words":
        return 270
    if dataset == "Adiac":
        return 176
    if dataset == "ArrowHead":
        return 251
    if dataset == "Beef":
        return 470
    if dataset == "BeetleFly":
        return 512
    if dataset == "BirdChicken":
        return 512
    if dataset == "Car":
        return 577
    if dataset == "CBF":
        return 128
    if dataset == "ChlorineConcentration":
        return 166
    if dataset == "CinC_ECG_torso":
        return 1639
    if dataset == "Coffee":
        return 286
    if dataset == "Computers":
        return 720
    if dataset == "Cricket_X":
        return 300
    if dataset == "Cricket_Y":
        return 300
    if dataset == "Cricket_Z":
        return 300
    if dataset == "DiatomSizeReduction":
        return 345
    if dataset == "DistalPhalanxOutlineAgeGroup":
        return 80
    if dataset == "DistalPhalanxOutlineCorrect":
        return 80
    if dataset == "DistalPhalanxTW":
        return 80
    if dataset == "Earthquakes":
        return 512
    if dataset == "ECG200":
        return 96
    if dataset == "ECG5000":
        return 140
    if dataset == "ECGFiveDays":
        return 136
    if dataset == "ElectricDevices":
        return 96
    if dataset == "FaceAll":
        return 131
    if dataset == "FaceFour":
        return 350
    if dataset == "FacesUCR":
        return 131
    if dataset == "FISH":
        return 463
    if dataset == "FordA":
        return 500
    if dataset == "FordB":
        return 500
    if dataset == "Gun_Point":
        return 150
    if dataset == "Ham":
        return 431
    if dataset == "HandOutlines":
        return 2709
    if dataset == "Haptics":
        return 1092
    if dataset == "Herring":
        return 512
    if dataset == "InlineSkate":
        return 1882
    if dataset == "InsectWingbeatSound":
        return 256
    if dataset == "ItalyPowerDemand":
        return 24
    if dataset == "LargeKitchenAppliances":
        return 720
    if dataset == "Lighting2":
        return 637
    if dataset == "Lighting7":
        return 319
    if dataset == "MALLAT":
        return 1024
    if dataset == "Meat":
        return 448
    if dataset == "MedicalImages":
        return 99
    if dataset == "MiddlePhalanxOutlineAgeGroup":
        return 80
    if dataset == "MiddlePhalanxOutlineCorrect":
        return 80
    if dataset == "MiddlePhalanxTW":
        return 80
    if dataset == "MoteStrain":
        return 84
    if dataset == "NonInvasiveFatalECG_Thorax1":
        return 750
    if dataset == "NonInvasiveFatalECG_Thorax2":
        return 750
    if dataset == "OliveOil":
        return 570
    if dataset == "OSULeaf":
        return 427
    if dataset == "PhalangesOutlinesCorrect":
        return 80
    if dataset == "Phoneme":
        return 1024
    if dataset == "Plane":
        return 144
    if dataset == "ProximalPhalanxOutlineAgeGroup":
        return 80
    if dataset == "ProximalPhalanxOutlineCorrect":
        return 80
    if dataset == "ProximalPhalanxTW":
        return 80
    if dataset == "RefrigerationDevices":
        return 720
    if dataset == "ScreenType":
        return 720
    if dataset == "ShapeletSim":
        return 500
    if dataset == "ShapesAll":
        return 512
    if dataset == "SmallKitchenAppliances":
        return 720
    if dataset == "SonyAIBORobotSurfaceII":
        return 65
    if dataset == "SonyAIBORobotSurface":
        return 70
    if dataset == "StarLightCurves":
        return 1024
    if dataset == "Strawberry":
        return 235
    if dataset == "SwedishLeaf":
        return 128
    if dataset == "Symbols":
        return 398
    if dataset == "synthetic_control":
        return 60
    if dataset == "ToeSegmentation1":
        return 277
    if dataset == "ToeSegmentation2":
        return 343
    if dataset == "Trace":
        return 275
    if dataset == "TwoLeadECG":
        return 82
    if dataset == "Two_Patterns":
        return 128
    if dataset == "uWaveGestureLibrary_X":
        return 315
    if dataset == "uWaveGestureLibrary_Y":
        return 315
    if dataset == "uWaveGestureLibrary_Z":
        return 315
    if dataset == "UWaveGestureLibraryAll":
        return 945
    if dataset == "wafer":
        return 152
    if dataset == "Wine":
        return 234
    if dataset == "WordsSynonyms":
        return 270
    if dataset == "Worms":
        return 900
    if dataset == "WormsTwoClass":
        return 900
    if dataset == "yoga":
        return 426
    exit('missing dataset')

# not used but here just in case
def train_max(dataset):
    if dataset == "50words":
        return 5.0184 #270
    if dataset == "Adiac":
        return 2.651 #176
    if dataset == "ArrowHead":
        return 2.554 #251
    if dataset == "Beef":
        return 3.7205 #470
    if dataset == "BeetleFly":
        return 2.055 #512
    if dataset == "BirdChicken":
        return 2.1244 #512
    if dataset == "Car":
        return 1.9907 #577
    if dataset == "CBF":
        return 3.2446 #128
    if dataset == "ChlorineConcentration":
        return 7.4423 #166
    if dataset == "CinC_ECG_torso":
        return 10.536 #1639
    if dataset == "Coffee":
        return 2.1771 #286
    if dataset == "Computers":
        return 21.596 #720
    if dataset == "Cricket_X":
        return 11.494 #300
    if dataset == "Cricket_Y":
        return 6.8385 #300
    if dataset == "Cricket_Z":
        return 11.924 #300
    if dataset == "DiatomSizeReduction":
        return 1.9848 #345
    if dataset == "DistalPhalanxOutlineAgeGroup":
        return 2.0253 #80
    if dataset == "DistalPhalanxOutlineCorrect":
        return 2.4602 #80
    if dataset == "DistalPhalanxTW":
        return 1.9998 #80
    if dataset == "Earthquakes":
        return 7.7281 #512
    if dataset == "ECG200":
        return 4.1991 #96
    if dataset == "ECG5000":
        return 4.0581 #140
    if dataset == "ECGFiveDays":
        return 5.4211 #136
    if dataset == "ElectricDevices":
        return 9.6959 #96
    if dataset == "FaceAll":
        return 4.8762 # 131
    if dataset == "FaceFour":
        return 5.9081 # 350
    if dataset == "FacesUCR":
        return 8.7394 # 131
    if dataset == "FISH":
        return 2.1259 # 463
    if dataset == "FordA":
        return 4.3151 #500
    if dataset == "FordB":
        return 4.9302 # 500
    if dataset == "Gun_Point":
        return 2.0534 # 150
    if dataset == "Ham":
        return 8.0329 # 431
    if dataset == "HandOutlines":
        return 1.7784 # 2709
    if dataset == "Haptics":
        return 3.1231 # 1092
    if dataset == "Herring":
        return 2.1343 # 512
    if dataset == "InlineSkate":
        return 4.3393 # 1882
    if dataset == "InsectWingbeatSound":
        return 6.4213 # 256
    if dataset == "ItalyPowerDemand":
        return 2.4248 # 24
    if dataset == "LargeKitchenAppliances":
        return 26.796 # 720
    if dataset == "Lighting2":
        return 23.131 # 637
    if dataset == "Lighting7":
        return 17.413 # 319
    if dataset == "MALLAT":
        return 2.7619 # 1024
    if dataset == "Meat":
        return 3.3902 # 448
    if dataset == "MedicalImages":
        return 7.2224 # 99
    if dataset == "MiddlePhalanxOutlineAgeGroup":
        return 1.7223 #80
    if dataset == "MiddlePhalanxOutlineCorrect":
        return 1.8756 #80
    if dataset == "MiddlePhalanxTW":
        return 1.7123 #80
    if dataset == "MoteStrain":
        return 2.4684 #84
    if dataset == "NonInvasiveFatalECG_Thorax1":
        return 4.7941 #750
    if dataset == "NonInvasiveFatalECG_Thorax2":
        return 4.6769 #750
    if dataset == "OliveOil":
        return 3.7188 #570
    if dataset == "OSULeaf":
        return 3.6695 #427
    if dataset == "PhalangesOutlinesCorrect":
        return 2.4457 #80
    if dataset == "Phoneme":
        return 8.0905 #1024
    if dataset == "Plane":
        return 2.9112 #144
    if dataset == "ProximalPhalanxOutlineAgeGroup":
        return 1.9029 #80
    if dataset == "ProximalPhalanxOutlineCorrect":
        return 1.9029 #80
    if dataset == "ProximalPhalanxTW":
        return 1.8496 #80
    if dataset == "RefrigerationDevices":
        return 5.902 #720
    if dataset == "ScreenType":
        return 26.796 #720
    if dataset == "ShapeletSim":
        return 1.8917 #500
    if dataset == "ShapesAll":
        return 2.8188 # 512
    if dataset == "SmallKitchenAppliances":
        return 26.795 #720
    if dataset == "SonyAIBORobotSurfaceII":
        return 4.2307 #65
    if dataset == "SonyAIBORobotSurface":
        return 3.6263 #70
    if dataset == "StarLightCurves":
        return 5.2883 #1024
    if dataset == "Strawberry":
        return 3.7227 #235
    if dataset == "SwedishLeaf":
        return 3.2216 # 128
    if dataset == "Symbols":
        return 2.2048 #398
    if dataset == "synthetic_control":
        return 2.412 #60
    if dataset == "ToeSegmentation1":
        return 3.9324 #277
    if dataset == "ToeSegmentation2":
        return 3.9256 #343
    if dataset == "Trace":
        return 3.9667 #275
    if dataset == "TwoLeadECG":
        return 1.8705 #82
    if dataset == "Two_Patterns":
        return 1.9394 #128
    if dataset == "uWaveGestureLibrary_X":
        return 4.4341 # 315
    if dataset == "uWaveGestureLibrary_Y":
        return 7.654 # 315
    if dataset == "uWaveGestureLibrary_Z":
        return 4.7786 # 315
    if dataset == "UWaveGestureLibraryAll":
        return 7.6284 # 945
    if dataset == "wafer":
        return 11.787 #152
    if dataset == "Wine":
        return 3.2006 #234
    if dataset == "WordsSynonyms":
        return 5.0028 #270
    if dataset == "Worms":
        return 4.1961 #900
    if dataset == "WormsTwoClass":
        return 4.1961 #900
    if dataset == "yoga":
        return 2.405 #426
    exit('missing dataset')

# not used but here just in case
def train_min(dataset):
    if dataset == "50words":
        return -2.3543 #270
    if dataset == "Adiac":
        return -1.9878 #176
    if dataset == "ArrowHead":
        return -2.2571 #251
    if dataset == "Beef":
        return -3.29 #470
    if dataset == "BeetleFly":
        return -2.5168 #512
    if dataset == "BirdChicken":
        return -2.8248 #512
    if dataset == "Car":
        return -2.2105 #577
    if dataset == "CBF":
        return -2.3169 #128
    if dataset == "ChlorineConcentration":
        return -11.839 #166
    if dataset == "CinC_ECG_torso":
        return -8.5936 #1639
    if dataset == "Coffee":
        return -2.0642 #286
    if dataset == "Computers":
        return -3.7477 #720
    if dataset == "Cricket_X":
        return -4.7662 #300
    if dataset == "Cricket_Y":
        return -9.7745 #300
    if dataset == "Cricket_Z":
        return -4.7583 #300
    if dataset == "DiatomSizeReduction":
        return -1.7728 #345
    if dataset == "DistalPhalanxOutlineAgeGroup":
        return -1.9137 #80
    if dataset == "DistalPhalanxOutlineCorrect":
        return -2.1799 #80
    if dataset == "DistalPhalanxTW":
        return -1.8965 #80
    if dataset == "Earthquakes":
        return -0.73019 #512
    if dataset == "ECG200":
        return -2.6172 #96
    if dataset == "ECG5000":
        return -5.7976 #140
    if dataset == "ECGFiveDays":
        return -6.5112 #136
    if dataset == "ElectricDevices":
        return -9.6959 #96
    if dataset == "FaceAll":
        return -4.4847 # 131
    if dataset == "FaceFour":
        return -4.6876 # 350
    if dataset == "FacesUCR":
        return -3.9591 # 131
    if dataset == "FISH":
        return -1.9506 # 463
    if dataset == "FordA":
        return -4.5565 #500
    if dataset == "FordB":
        return -4.088 # 500
    if dataset == "Gun_Point":
        return -2.3692 # 150
    if dataset == "Ham":
        return -2.0538 # 431
    if dataset == "HandOutlines":
        return -2.8909 # 2709
    if dataset == "Haptics":
        return -11.147 # 1092
    if dataset == "Herring":
        return -2.1856 # 512
    if dataset == "InlineSkate":
        return -2.2635 # 1882
    if dataset == "InsectWingbeatSound":
        return -1.0819 # 256
    if dataset == "ItalyPowerDemand":
        return -1.991 # 24
    if dataset == "LargeKitchenAppliances":
        return -1.5751 # 720
    if dataset == "Lighting2":
        return -1.396 # 637
    if dataset == "Lighting7":
        return -1.7812 # 319
    if dataset == "MALLAT":
        return -1.6073 # 1024
    if dataset == "Meat":
        return -1.5425 # 448
    if dataset == "MedicalImages":
        return -2.3919 # 99
    if dataset == "MiddlePhalanxOutlineAgeGroup":
        return -1.7195 #80
    if dataset == "MiddlePhalanxOutlineCorrect":
        return -1.7195 #80
    if dataset == "MiddlePhalanxTW":
        return -1.5848 #80
    if dataset == "MoteStrain":
        return -8.4093 #84
    if dataset == "NonInvasiveFatalECG_Thorax1":
        return -5.7322 #750
    if dataset == "NonInvasiveFatalECG_Thorax2":
        return -5.4157 #750
    if dataset == "OliveOil":
        return -1.0011 #570
    if dataset == "OSULeaf":
        return -3.1573 #427
    if dataset == "PhalangesOutlinesCorrect":
        return -2.1589 #80
    if dataset == "Phoneme":
        return -13.324 #1024
    if dataset == "Plane":
        return -2.1133 #144
    if dataset == "ProximalPhalanxOutlineAgeGroup":
        return -1.4834 #80
    if dataset == "ProximalPhalanxOutlineCorrect":
        return -1.4834 #80
    if dataset == "ProximalPhalanxTW":
        return -1.4691 #80
    if dataset == "RefrigerationDevices":
        return -5.46652 #720
    if dataset == "ScreenType":
        return -2.9218 #720
    if dataset == "ShapeletSim":
        return -1.8113 #500
    if dataset == "ShapesAll":
        return -3.2201 # 512
    if dataset == "SmallKitchenAppliances":
        return -5.0674 #720
    if dataset == "SonyAIBORobotSurfaceII":
        return -4.138 #65
    if dataset == "SonyAIBORobotSurface":
        return -2.7267 #70
    if dataset == "StarLightCurves":
        return -2.6779 #1024
    if dataset == "Strawberry":
        return-2.1276 #235
    if dataset == "SwedishLeaf":
        return -3.4116 # 128
    if dataset == "Symbols":
        return -2.3109 #398
    if dataset == "synthetic_control":
        return -2.4538 #60
    if dataset == "ToeSegmentation1":
        return -3.5831 #277
    if dataset == "ToeSegmentation2":
        return -2.6365 #343
    if dataset == "Trace":
        return -2.2211 #275
    if dataset == "TwoLeadECG":
        return -3.1489 #82
    if dataset == "Two_Patterns":
        return -1.9393 #128
    if dataset == "uWaveGestureLibrary_X":
        return -4.4383 # 315
    if dataset == "uWaveGestureLibrary_Y":
        return -4.1034 # 315
    if dataset == "uWaveGestureLibrary_Z":
        return -3.5484 # 315
    if dataset == "UWaveGestureLibraryAll":
        return -4.434 # 945
    if dataset == "wafer":
        return -3.054 #152
    if dataset == "Wine":
        return -1.9424 #234
    if dataset == "WordsSynonyms":
        return -2.2607 #270
    if dataset == "Worms":
        return -4.8873 #900
    if dataset == "WormsTwoClass":
        return -4.8873 #900
    if dataset == "yoga":
        return 2.405 #426
    exit('missing dataset')

# not used but here just in case
def train_size(dataset):
    if dataset == "50words":
        return 450
    if dataset == "Adiac":
        return 390
    if dataset == "ArrowHead":
        return 36
    if dataset == "Beef":
        return 30
    if dataset == "BeetleFly":
        return 20
    if dataset == "BirdChicken":
        return 20
    if dataset == "Car":
        return 60
    if dataset == "CBF":
        return 30
    if dataset == "ChlorineConcentration":
        return 467
    if dataset == "CinC_ECG_torso":
        return 40
    if dataset == "Coffee":
        return 28
    if dataset == "Computers":
        return 250
    if dataset == "Cricket_X":
        return 390
    if dataset == "Cricket_Y":
        return 390
    if dataset == "Cricket_Z":
        return 390
    if dataset == "DiatomSizeReduction":
        return 16
    if dataset == "DistalPhalanxOutlineAgeGroup":
        return 139
    if dataset == "DistalPhalanxOutlineCorrect":
        return 276
    if dataset == "DistalPhalanxTW":
        return 139
    if dataset == "Earthquakes":
        return 139
    if dataset == "ECG200":
        return 100
    if dataset == "ECG5000":
        return 500
    if dataset == "ECGFiveDays":
        return 23
    if dataset == "ElectricDevices":
        return 8926
    if dataset == "FaceAll":
        return 560
    if dataset == "FaceFour":
        return 350
    if dataset == "FacesUCR":
        return 24
    if dataset == "FISH":
        return 175
    if dataset == "FordA":
        return 1320
    if dataset == "FordB":
        return 810
    if dataset == "Gun_Point":
        return 50
    if dataset == "Ham":
        return 109
    if dataset == "HandOutlines":
        return 370
    if dataset == "Haptics":
        return 155
    if dataset == "Herring":
        return 64
    if dataset == "InlineSkate":
        return 100
    if dataset == "InsectWingbeatSound":
        return 220
    if dataset == "ItalyPowerDemand":
        return 67
    if dataset == "LargeKitchenAppliances":
        return 375
    if dataset == "Lighting2":
        return 60
    if dataset == "Lighting7":
        return 70
    if dataset == "MALLAT":
        return 55
    if dataset == "Meat":
        return 60
    if dataset == "MedicalImages":
        return 381
    if dataset == "MiddlePhalanxOutlineAgeGroup":
        return 154
    if dataset == "MiddlePhalanxOutlineCorrect":
        return 291
    if dataset == "MiddlePhalanxTW":
        return 154
    if dataset == "MoteStrain":
        return 20
    if dataset == "NonInvasiveFatalECG_Thorax1":
        return 1800
    if dataset == "NonInvasiveFatalECG_Thorax2":
        return 1800
    if dataset == "OliveOil":
        return 30
    if dataset == "OSULeaf":
        return 200
    if dataset == "PhalangesOutlinesCorrect":
        return 1800
    if dataset == "Phoneme":
        return 214
    if dataset == "Plane":
        return 105
    if dataset == "ProximalPhalanxOutlineAgeGroup":
        return 400
    if dataset == "ProximalPhalanxOutlineCorrect":
        return 600
    if dataset == "ProximalPhalanxTW":
        return 205
    if dataset == "RefrigerationDevices":
        return 375
    if dataset == "ScreenType":
        return 375
    if dataset == "ShapeletSim":
        return 20
    if dataset == "ShapesAll":
        return 600
    if dataset == "SmallKitchenAppliances":
        return 375
    if dataset == "SonyAIBORobotSurfaceII":
        return 20
    if dataset == "SonyAIBORobotSurface":
        return 27
    if dataset == "StarLightCurves":
        return 1000
    if dataset == "Strawberry":
        return 370
    if dataset == "SwedishLeaf":
        return 500
    if dataset == "Symbols":
        return 25
    if dataset == "synthetic_control":
        return 300
    if dataset == "ToeSegmentation1":
        return 40
    if dataset == "ToeSegmentation2":
        return 36
    if dataset == "Trace":
        return 100
    if dataset == "TwoLeadECG":
        return 23
    if dataset == "Two_Patterns":
        return 1000
    if dataset == "uWaveGestureLibrary_X":
        return 896
    if dataset == "uWaveGestureLibrary_Y":
        return 896
    if dataset == "uWaveGestureLibrary_Z":
        return 896
    if dataset == "UWaveGestureLibraryAll":
        return 896
    if dataset == "wafer":
        return 1000
    if dataset == "Wine":
        return 57
    if dataset == "WordsSynonyms":
        return 267
    if dataset == "Worms":
        return 77
    if dataset == "WormsTwoClass":
        return 77
    if dataset == "yoga":
        return 300
    exit('missing dataset')

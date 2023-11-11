import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def clean_samples(df_samples):
    df_samples.replace([np.inf, -np.inf], np.nan, inplace=True)
    df_samples.dropna(how="all", inplace=True)
    df_samples.fillna(0, inplace=True)
    df_samples.reset_index(inplace=True, drop=True)
    for c in list(df_samples.columns):
        if c != 'class':
            df_samples[c] = df_samples[c].astype(float)
    return df_samples

def map_classes_to_id(df_samples):
    for i, c in enumerate(list(df_samples['class'].unique())):
        df_samples.loc[df_samples['class']==c, ['class']] = i
        print(i,c)
    return df_samples

def select_class_to_predict(df_samples, class_name):
    df_samples.loc[df_samples['class']!=class_name, 'class'] = 0
    df_samples.loc[df_samples['class']==class_name, 'class'] = 1
    return df_samples

def prepare_df_sample(df_samples, class_type, class_name=None):
    df_samples_clean = clean_samples(df_samples)
    if class_type == 'bool':
        if class_name in list(df_samples_clean['class'].unique()):
            df_samples_class = select_class_to_predict(df_samples_clean, class_name)
            return df_samples_class
        else:
            print(f"Class {class_name} not in dataset class values.-")
    elif class_type == 'map':
        df_samples_class = map_classes_to_id(df_samples_clean)
        return df_samples_class
    else:
        print("Posible class_type values: 'bool' or 'map'.-")


# **********************************************************************************

def split_sample(df_samples):
    X = df_samples.drop(columns='class')
    y = df_samples.loc[:,'class']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.4, random_state=42, stratify=y)

    y=y.astype('int')
    y_train=y_train.astype('int')
    y_test=y_test.astype('int')

    return X, y, X_train, X_test, y_train, y_test 

def train_model(X_train, X_test, y_train, y_test, model_name, params_list):
    if model_name == 'kmeans':
        if len(params_list == 1):
            k = params_list[0]
            clf = KNeighborsClassifier(k)
            clf.fit(X_train, y_train)
            score = clf.score(X_test, y_test)
            print('score: ',score, ' - k: ', k)
            return clf
        else:
            print("kmeans model only takes one param.-")

def search_model(df_samples, model_name, params_search):
    X, y, X_train, X_test, y_train, y_test = split_sample(df_samples)
    for k in range(params_search):                      
        train_model(X_train, X_test, y_train, y_test, model_name, k)


# **********************************************************************************

def predict_model(df_band, df_samples, model_name, params_list):
    X = df_samples.drop(columns='class')
    y = df_samples.loc[:,'class']

    model = train_model(X, X, y, y, model_name, params_list)
    y_pred_model = model.predict(df_band)
    df_band['clase'] = y_pred_model

    return df_band


""" def save_classifiedraster():
    # load classify image
    img_not_georef_open = rasterio.open(img_sat_aoi_folder+"area_de_estudio_"+sat_img_folders+"_class.tif")
    img_not_georef = img_not_georef_open.read()
    # load a band of the original satellite image
    img_georef_open = rasterio.open(img_sat_aoi_folder+'area_de_estudio_'+sat_img_folders+'.tif')
    img_georef = img_georef_open.read(1)

    # extract and modify the original image metadata
    meta = img_georef_open.meta
    meta.update(count=1)

    # replace the array values
    img_georef = img_not_georef[0]

    # save the image with modify values
    with rasterio.open(img_sat_aoi_folder+"area_de_estudio_"+sat_img_folders+"_class_georef.tif", 'w', **meta) as dst:
        dst.write(np.array([img_georef]).astype(rasterio.float32)) 

    img_not_georef_open.close()
    img_georef_open.close()
    dst.close() """

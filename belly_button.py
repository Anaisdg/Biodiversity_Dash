import pandas as pd

bio_diversity_metadata = pd.read_csv("DataSets/Belly_Button_Biodiversity_Metadata.csv")



otu = pd.read_csv("DataSets/belly_button_biodiversity_otu_id.csv")



metadata = pd.read_csv("DataSets/metadata_columns.csv")



samples = pd.read_csv("DataSets/belly_button_biodiversity_samples.csv")

def names():

    sample_names = list(samples)
    sample_names = sample_names[1:]
    return sample_names

if __name__ == "__main__":
    names()

def otu_list():

    otu_descriptions = list(otu.lowest_taxonomic_unit_found)

    return otu_descriptions

if __name__ == "__main__":
    otu_list()

def json():

    idx = 0
    new_col = bio_diversity_metadata['SAMPLEID']
    bio_diversity_metadata.insert(loc=idx, column='sample', value=new_col)


    bio_diversity_metadata['sample'] = 'BB_' + bio_diversity_metadata['sample'].astype(str)

    df = bio_diversity_metadata[['sample','AGE','BBTYPE','ETHNICITY','GENDER','LOCATION','SAMPLEID']]


    df = df.set_index('sample')


    json_dict = df.to_dict('index')

    return json_dict

if __name__ == "__main__":
    json()

def washing():


    df2 = bio_diversity_metadata[['sample','WFREQ']]



    df2 = df2.set_index('sample')



    washing_dict = df2.to_dict('index')

    print(washing_dict)

    return washing_dict

if __name__ == "__main__":
    washing()

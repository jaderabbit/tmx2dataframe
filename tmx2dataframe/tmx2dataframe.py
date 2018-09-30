import pandas as pd
from xml.dom import minidom


def process_tuv(tuv):
    lang = tuv.attributes['lang'].value
    seg = tuv.getElementsByTagName('seg')[0]
    txt = seg.childNodes[0].data
    return lang, txt

def read(path):

    """Read function takes in a path to TMX translation file and outputs the metadata and a pandas dataframe.

    Args:
        param1 (str): The path to the TMX translation file

    Returns:
        dict: The header of the TMX file, which contains metadata
        DataFrame: A Pandas Dataframe. Each line item consists of source_language, source_sentence, target_language, target_sentence

    """
    # parse an xml file by name
    tmx = minidom.parse(path)

    # Get metadata
    metadata = {}
    header = tmx.getElementsByTagName('header')[0]
    for key in header.attributes.keys():
        metadata[key] = header.attributes[key].value
        
    srclang = metadata['srclang']

    # Get translation sentences
    body = tmx.getElementsByTagName('body')[0]
    translation_units = body.getElementsByTagName('tu')
    items = []
    for tu in translation_units:
        srclang, srcsentence = process_tuv(tu.getElementsByTagName('tuv')[0])
        targetlang, targetsentence = process_tuv(tu.getElementsByTagName('tuv')[1])
        item = {
            'source_language': srclang,
            'source_sentence': srcsentence,
            'target_language': targetlang,
            'target_sentence': targetsentence
        }
        items.append(item)

    df = pd.DataFrame(items)
    return metadata, df

    
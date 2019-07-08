import pandas as pd
from xml.dom import minidom

def getText(nodelist):
    """Helper function to return the text content from an XML node, joined as a single string.
    """
    rc = []
    for node in nodelist:
        if node.nodeType == minidom.Node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)

def process_tuv(tuv):
    """Function to process a single TMX 'TUV' unit - a unit of text in a particular language.

    Args:
        tuv (Node):     The <tuv> node to process.
    
    Returns:
        lang (String):  The locale/language code of the <tuv> element.
        txt (String):   The text contained in the <tuv> element.
    """
    if 'lang' in tuv.attributes:
        lang = tuv.attributes['lang'].value
    else: 
        lang = tuv.attributes['xml:lang'].value
    seg = tuv.getElementsByTagName('seg')[0]
    
    # If the node has direct text content data, process it as a string
    if hasattr(seg.childNodes[0], 'data'):
        txt = seg.childNodes[0].data
    
    # If it doesn't have a 'data' attribute, it most likely contains child tags such as placeholders (<ph>). Therefore, include these as XML strings.
    else:
        if len(seg.childNodes) > 0 :
            txt = getText(seg.childNodes)
        else:
            print("no child nodes")
    return lang, txt

def read(path):

    """Read function takes in a path to TMX translation file and outputs the metadata and a pandas dataframe.

    Args:
        param1 (str): The path to the TMX translation file

    Returns:
        dict: The header of the TMX file, which contains metadata
        DataFrame: A Pandas Dataframe. The column names will be the locale/language codes, and the row content will be the translations for each locale.

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
        tuvs = tu.getElementsByTagName('tuv')
        tudata = {}
        for tuv in tuvs:
            lang, sentence = process_tuv(tuv)
            tudata[lang] = sentence
        items.append(tudata)

    df = pd.DataFrame(items)
    return metadata, df

    

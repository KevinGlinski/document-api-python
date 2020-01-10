import xml.etree.ElementTree as ET

class Thumbnail(object):
    """A class representing Tableau workbook thumbnail, embedded in workbook files or
    in TDS files.

    """

    def __init__(self, dsxml, filename=None):
        """
        Constructor.  Default is to create thumbnail from xml.

        """
        self._datasourceXML = dsxml
        self._datasourceTree = ET.ElementTree(self._datasourceXML)
        self._height = self._datasourceXML.get('height')
        self._width = self._datasourceXML.get('width')
        self._name = self._datasourceXML.get('name')
        self._image_data = self._datasourceXML.text

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    @property
    def name(self):
        return self._name

    @property
    def image_data(self):
        return self._image_data        

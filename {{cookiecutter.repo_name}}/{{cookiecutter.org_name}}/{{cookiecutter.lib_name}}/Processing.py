import json
import pkgutil
import typing

import numpy
import numpy.typing

def get_processing_data() -> numpy.typing.NDArray[typing.Any]:
    data = pkgutil.get_data(__name__, "resources/ProcessingData.json")
    assert data is not None
    processing_data = json.loads(data)
    return numpy.full((processing_data["height"], processing_data["width"]), processing_data["value"])

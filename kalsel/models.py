from shapely.wkt import loads

def intersect(wc, ac):
    """Calculates the intersection between two objects
    """
    for wg in wc:
        for ag in ac:
            intersections.append(ag.intersects(ac))

    return intersections

def get_geometry(fid):
    layer = fid.GetLayerByIndex(0)
    feature = layer.GetFeature(0)
    geometry = feature.GetGeometryRef()
    #geometry for polygon as WKT, inner rings, outer rings etc. 
    return geometry

def calculate(wetland, adm):
    """Multiplies the layers
    """
    wc = loads(get_geometry(wetland))
    ac = loads(get_geometry(adm))
    intersections = []

    # Do the intersection between wetland and adm
    intersections = intersect(wc, ac)

    # Do something else

    return intersections

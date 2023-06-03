import requests, zipfile, io
import tempfile
import gtfs_kit as gk
import geopandas as gpd


def main():
    """
    Return gdf of GTFS feed w/ route shape
    """
    gtfs_url = r"https://assets.metrolinx.com/raw/upload/Documents/Metrolinx/Open%20Data/GO-GTFS.zip"

    with tempfile.TemporaryDirectory() as tmpdirname:
        req = requests.get(gtfs_url,stream=True)
        zipf = zipfile.ZipFile(io.BytesIO(req.content))
        zipf.extractall(tmpdirname)
        feed = (gk.read_feed(tmpdirname, dist_units='km'))
        feed.validate()
        geometry_data= gk.shapes.geometrize_shapes(feed).merge(feed.trips,on='shape_id', how='left')
        geometry_data = geometry_data.drop(columns=['trip_short_name','direction_id','wheelchair_accessible','bikes_allowed','route_variant','trip_id','service_id'])
        geometry_data['line_id'] = geometry_data['route_id'].apply(lambda x: x.split('-')[1])
        geometry_data=geometry_data.astype({'block_id':str,'line_id':str}).drop_duplicates(subset=['trip_headsign','block_id','shape_id','route_id']).rename(columns = {'block_id':'long_name'})
        geometry_data.to_file('go_gtfs.gpkg', driver='GPKG', layer='go_gtfs')
        return geometry_data


if __name__ == "__main__":
    main()
    """
    Return dict of df
    """
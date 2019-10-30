import zipfile
import requests
import geopandas as gp
import io
from pathlib import Path

# add .kml to the user input dir in download_utm_tiles(), then the end does not have to appended

def download_utm_tiles():
    """
    Function to solely download the NASA's kml file containing vectors of the global UTM grid.
    As the file needs ~100MB memory, the user is asked to download the file manually with the following code
    ----------------------------
    No input
    ----------------------------
    returns:
        0
            
    # wilma
    # 
    # """

    import urllib
    url = "https://hls.gsfc.nasa.gov/wp-content/uploads/2016/03/S2A_OPER_GIP_TILPAR_MPC__20151209T095117_V20150622T000000_21000101T000000_B00.kml"
    bool = True

    while bool == True:
        usr_inp = input("Are you sure if you want to download the NASA's global UTM-tiles?"
                     "\n~100MB memory is required"
                     "\n[y/N]")

        if usr_inp == "y":
            bool == False
            local_path = input("Location directory of file needed. Type:"
                               "")
            local_path = local_path + ".kml"

            print(f"Downloading kml-file from url {url}...")
            urllib.request.urlretrieve(url, local_path)

        elif bool == "N":
            print("aborted."
                  "It's cleary to big for your Mac."
                  "LINUX LOVE")
            bool == False

        else:
            print("Input not readable.")


def download_hls_s2_tiles():
    """
    Brauchen wir diese Funktion eigentlich noch?
    ----------------------------
    input:
    ----------------------------
    returns:
        path to shapefile with nasa hls test sites

    """

    url = "https://hls.gsfc.nasa.gov/wp-content/uploads/2018/10/hls_s2_tiles.zip"
    local_path = "ignored/test_tiles/"

    print(f"Downloading shapefile from url {url}...")
    request = requests.get(url)
    zip = zipfile.ZipFile(io.BytesIO(request.content))
    print("DONE")
    zip.extractall(path=local_path)

    path_to_test_tiles = local_path + "hls_s2_tiles.shp"

    return path_to_test_tiles

def get_tiles_from_shape(user_polygon):
    pass


def get_tiles_from_UTM(path_to_UTM_file):

    path_to_UTM_file = Path("/home/aleko-kon/projects/geo419/nasa-hls/ignored/UTM_tiles.kml")
    path_to_UTM_file = Path(input("Please input the path to the UTM-file"))
    # path_to_UTM_file = Path(download_utm_tiles())         # will work when the function called returns local path
    except:
        # if not create the .kml file or give the src dir for the file

        # if kml exists give src dir
        # else
            # raise: not found, please download and save in path

    Path.exists(path_to_UTM_file)

        # wenn die UTM-tile.kml Datei schon existiert, dann nicht mehr download_utm_tiles call

    # Enable fiona driver, then read kml-file
    gp.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'
    UTM_tiles = gp.read_file(path_to_UTM_file, driver='KML')

    # search for user polygon - how to make dir inputs properly?
    # path_to_user_polygon = input("enter the local path to the shapefile of your working area")
    path_to_user_polygon = Path("/home/aleko-kon/projects/geo419/nasa-hls/ignored/user_shape/dummy_region.shp")

    # convert user_polygon into Gdf
    user_polygon = gp.GeoDataFrame.from_file(path_to_user_polygon)

    # perform intersection
    intersections= gp.sjoin(user_polygon, UTM_tiles, how="inner", op='intersects')

    # write UTM-codes in list
    tiles = intersections["Name"].tolist()
    print(tiles)

    return tiles


# # Plot the data
# fig, ax = plt.subplots(figsize=(12, 8))
# user_poly.plot(alpha=.5, ax=ax)
# plt.show()

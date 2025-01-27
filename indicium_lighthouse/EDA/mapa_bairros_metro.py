from matplotlib import pyplot as plt
from limpeza_dados import get_dados
from matplotlib.patches import Rectangle

def gerar_mapa():
    data, _ = get_dados()
    loc_points = {
        "staten_island": [
            [40.643748, -74.073632],  # St. George Ferry Terminal
            [40.636949, -74.074835],  # Tompkinsville
            [40.627915, -74.075162],  # Stapleton
            [40.621356, -74.077356],  # Clifton
            [40.603146, -74.084215],  # Grasmere
            [40.596596, -74.087935],  # Old Town
            [40.588841, -74.096376],  # Dongan Hills
            [40.578965, -74.104677],  # Grant City
            [40.554964, -74.151984],  # Great Kills
            [40.543212, -74.164708],  # Eltingville Transit Center
            [40.535264, -74.191265],  # Huguenot
            [40.520847, -74.199820],  # Annadale
            [40.512765, -74.251961],  # Tottenville
            [40.556865, -74.136785],  # Bay Terrace
            [40.573494, -74.108337],   # New Dorp
        ],
        "brooklyn": [
            [40.683595, -73.978927],  # Atlantic Ave - Barclays Center
            [40.577281, -73.981818],  # Coney Island - Stillwell Ave
            [40.717432, -73.956217],  # Bedford Ave
            [40.692404, -73.990151],  # Court St
            [40.693219, -73.990823],  # Borough Hall
            [40.692338, -73.987342],  # Jay St - MetroTech
            [40.632836, -73.947642],  # Flatbush Ave - Brooklyn College
            [40.650494, -73.962876],  # Church Ave
            [40.668897, -73.931528],  # Crown Heights - Utica Ave
            [40.731352, -73.954435],  # Greenpoint Ave
            [40.708130, -73.957734],  # Williamsburg - Marcy Ave
            [40.577621, -73.961376],  # Brighton Beach
            [40.690648, -73.981814],  # Dekalb Ave
            [40.680832, -73.950618],  # Nostrand Ave
            [40.694063, -73.949170]   # Myrtle-Willoughby Aves
        ],
        "bronx": [
            [40.827994, -73.925878],  # Yankee Stadium - 161 St
            [40.861296, -73.897749],  # Fordham Rd (Grand Concourse Line)
            [40.867759, -73.897174],  # Kingsbridge Rd
            [40.818311, -73.927966],  # 149 St - Grand Concourse
            [40.852462, -73.828121],  # Pelham Bay Park
            [40.903125, -73.850620],  # Wakefield - 241 St
            [40.877745, -73.867347],  # Gun Hill Rd (White Plains Line)
            [40.850391, -73.905149],  # Tremont Ave
            [40.841894, -73.842951],  # Westchester Sq - E Tremont Ave
            [40.841042, -73.873426],  # East 180 St
            [40.816104, -73.917860],  # 3 Av - 149 St
            [40.854364, -73.860495],  # Morris Park
            [40.874811, -73.878855],  # Norwood - 205 St
            [40.820948, -73.890549],  # Hunts Point Ave
            [40.874002, -73.887517]   # Bedford Park Blvd
        ],
        "queens": [
            [40.759600, -73.830030],  # Flushing - Main St
            [40.702147, -73.801109],  # Jamaica Center - Parsons/Archer
            [40.721691, -73.844485],  # Forest Hills - 71 Ave
            [40.746644, -73.891338],  # Jackson Heights - Roosevelt Ave
            [40.745630, -73.902984],  # Woodside - 61 St
            [40.748973, -73.937243],  # Queens Plaza
            [40.747023, -73.945264],  # Court Square
            [40.742216, -73.948916],  # Hunters Point Ave
            [40.580903, -73.835592],  # Rockaway Park - Beach 116 St
            [40.702566, -73.816859],  # Jamaica - Van Wyck
            [40.775036, -73.912034],  # Astoria - Ditmars Blvd
            [40.743781, -73.919012],  # Sunnyside - Bliss St
            [40.709162, -73.828305],  # Kew Gardens - Union Tpke
            [40.685952, -73.827684],  # Ozone Park - Lefferts Blvd
            [40.601695, -73.755358]   # Far Rockaway - Mott Ave
        ], 
        "manhattan": [
            [40.755290, -73.987495],  # Times Square - 42 St
            [40.752726, -73.977229],  # Grand Central - 42 St
            [40.750373, -73.991057],  # 34 St - Penn Station
            [40.735736, -73.990568],  # 14 St - Union Square
            [40.707557, -74.011862],  # Wall Street
            [40.777861, -73.951669],  # 86 St (Lexington Ave Line)
            [40.804138, -73.937594],  # 125 St (Harlem - Lexington Ave Line)
            [40.768296, -73.981736],  # 59 St - Columbus Circle
            [40.712582, -74.009781],  # World Trade Center
            [40.725297, -73.996204],  # Broadway - Lafayette St
            [40.718092, -74.000582],  # Canal St
            [40.744081, -73.995657],  # 23 St (7th Ave Line)
            [40.764664, -73.980658],  # 57 St - 7th Ave
            [40.714111, -74.008585],  # Chambers St
            [40.868072, -73.919899]   # Inwood - 207 St
        ]
    }
    
    bairro_groups = data['bairro_group'].unique()
    color = {bairro: plt.cm.viridis(i / len(bairro_groups)) for i, bairro in enumerate(bairro_groups)}

    plt.figure(figsize=(10, 6))

    for bairro in bairro_groups:
        bairro_data = data[data['bairro_group'] == bairro]
        plt.scatter(
            bairro_data['longitude'], bairro_data['latitude'],
            color=color[bairro], label=bairro, edgecolors='black', alpha=1        
        )
    gold_square = Rectangle((0, 0), 1, 1, fc="gold", label="Estação de Metrô")

    handles, labels = plt.gca().get_legend_handles_labels()  
    handles.append(gold_square)  
    labels.append("Estação de Metrô")  

    plt.legend(handles=handles, labels=labels)
    
    for bairro, locations in loc_points.items():
        for loc in locations:
            plt.scatter(
                loc[1], loc[0],
                color='gold', s=50, label="Estação de Metrô", edgecolors='black', marker='s'
            )    
        
    plt.title("Distribuição geográfica dos imóveis por bairro.", fontsize=15)
    plt.xlabel("Longitude", fontsize=12)
    plt.ylabel("Latitude", fontsize=12)

    plt.grid(color='gray')
    plt.show()
    
if __name__=="__main__":
    gerar_mapa()
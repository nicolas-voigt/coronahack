import json
from get_data.db import connect

def load_city_list(filename: str):
    with open(filename) as cityfile:
        data = json.load(cityfile)
    return data

def insert_states(cities, connection):
    query = "INSERT INTO state (name) VALUES (%s)"
    c = connection.cursor()
    states = set([c["BundeslandLabel"] for c in cities])
    states.add("Berlin")  # Berlin is apperently not inside the city list of Wikidata
    c.executemany(query, [(s, ) for s in states])
    connection.commit()

def insert_cities(cities, connection):
    # keys: item, itemLabel, website, coordinates, BundeslandLabel
    c = connection.cursor(buffered=True)  # to avoid mysql.connector.errors.InternalError: Unread result found
    for city in cities:
        c.execute("SELECT id FROM city WHERE name = %s", (city["itemLabel"], ))
        result = c.fetchone()
        if result:
            print(f"Skipped id {result}")
            continue
        bundesland = city["BundeslandLabel"]
        c.execute("SELECT id FROM state WHERE name = %s", (bundesland, ))
        state_id = c.fetchone()[0]

        query = f"INSERT INTO city (name, state_id, coordinates) VALUES ('{city['itemLabel']}', {state_id}, ST_PointFromText('{city['coordinates']}'))"
        c.execute(query)
        connection.commit()

    # Mannheim and Wüllheim have as state Würtemberg-Baden, set it to Baden-Würtemberg
    # SELECT id FROM state WHERE name = "Württemberg-Baden";
    # update city set state_id = 2 where state_id = 11;

    # Hamburg is missing, replace it with the Württemberg-Baden entry
    # update state Set name = "Hamburg" where name = "Württemberg-Baden";
    # INSERT INTO city (name, state_id, coordinates) VALUES ('Hamburg', 11, ST_PointFromText('Point(53.55 10)'));

    # city of Berlin is missing
    # select * from state where name = "Berlin";
    # INSERT INTO city (name, state_id, coordinates) VALUES ('Berlin', 13, ST_PointFromText('Point(52.516 13.383)'));

def main():
    cities = load_city_list("city_list.json")
    connection = connect()
    # insert_states(cities, connection)
    insert_cities(cities, connection)
    connection.close()

if __name__ == '__main__':
    main()
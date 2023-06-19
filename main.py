from fastapi import FastAPI
from fastapi.responses import JSONResponse
from SPARQLWrapper import SPARQLWrapper, JSON

app = FastAPI()

@app.get("/ontology")
async def get_ontology_data():
    # Connect to the Fuseki SPARQL endpoint
    sparql = SPARQLWrapper("http://vocabs.ardc.edu.au/repository/api/sparql/"
    "csiro_international-chronostratigraphic-chart_geologic-time-scale-2020")

    # Set your SPARQL query
    query = """
    PREFIX gts: <http://resource.geosciml.org/ontology/timescale/gts#>

    SELECT *
    WHERE {
        ?a a gts:Age .
    }
    ORDER BY ?a
    LIMIT 3
    """

    sparql.setQuery(query)

    # Execute the SPARQL query and process the results
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    # Return the processed results as an HTTP response
    return JSONResponse(content=results, status_code=200)
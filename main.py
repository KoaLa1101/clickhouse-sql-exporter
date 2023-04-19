import json
import aiohttp
from aiohttp import web

with open("app_config/config.json", "r") as file:
    config = json.load(file)

clickhouse_config = config["clickhouse"]

async def metrics(request):
    with open("app_config/queries.json", "r") as file:
        queries = json.load(file)

    params = {
        "user": clickhouse_config["user"],
        "password": clickhouse_config["password"],
        "database": clickhouse_config["database"]
    }

    async with aiohttp.ClientSession() as session:
        results = {}
        for query_key, query_data in queries.items():
            params["query"] = query_data["sql"]
            async with session.post(clickhouse_config["url"], params=params) as resp:
                results[query_key] = [tuple(map(str.strip, line.split("\t"))) for line in (await resp.text()).split("\n") if line]

    response = []

    for query_key, query_data in queries.items():
        for row in results[query_key]:
            fields_values = {field: value for field, value in zip(query_data["fields"], row)}

            metric_labels = ', '.join(f'{field}="{value}"' for field, value in fields_values.items() if
                                      field not in ["cnt"])

            if "cnt" in fields_values:
                metric_value = fields_values["cnt"]
                if metric_value is None or len(metric_value) < 1:
                    metric_value = 0
                metric_name = f'{query_data["metric_name"]}'

            response.append(f'{metric_name}{{{metric_labels}}} {metric_value}')

    return web.Response(text="\n".join(response))

app = web.Application()
app.router.add_get("/metrics", metrics)

if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=9439)
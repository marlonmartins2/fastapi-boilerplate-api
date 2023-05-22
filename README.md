
<h1 align="center">Boiler Plate Fastapi API</h1>

<h3 align="center">
  # FastAPI-based project skeleton for creating new REST APIs.
</h3>

## :rocket: Stack

- Docker / docker-compose
- Python 3.11 (official stable)
- Integration with Sentry
- PyMongo 4.3.x
- Uvicorn 0.22.x

## :train2: Considerações - Mongo

The `docker-compose.yml` configuration is prepared to run the
project with a mongo instance through docker. Do not change the envs
vars and restore from a development dump to proceed.

## 🏃Preparando para execução

> cloning repository:

```shell
git config pull.rebase true
git clone git@github.com:marlonmartins2/fastapi-boilerplate-api.git

or com htts

git clone https://github.com/marlonmartins2/fastapi-boilerplate-api.git
cd fastapi-boilerplate-api/
```

> Environment variable settings

Environment variables must be added to the project inside the **/fastapi-boilerplate-api** folder. Create the `.env` file based on the example present in `.env.sample`

## :train2: Run Project

Use docker-compose to install and start the system locally, with all its dependencies:

```bash
docker-compose down && docker-compose up --build
```

## :evergreen_tree: Branchs

The project contains the following protected _branches_:

- [_master_](https://github.com/marlonmartins2/fastapi-boilerplate-api/tree/master) : contains the latest version of Production.
- [_dev_](https://github.com/marlonmartins2/fastapi-boilerplate-api/tree/dev) : contains the latest version of Development.

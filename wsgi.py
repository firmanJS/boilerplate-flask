from config import configuration, http

app = http.create_app(configuration.Configuration)
port = int(configuration.Configuration.PORT)

if __name__ == "__main__":
    http.run(app, '0.0.0.0', port, use_reloader=True)

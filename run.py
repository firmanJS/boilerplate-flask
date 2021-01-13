from config import configuration, http

app = http.createApp(configuration.Configuration)
port = int(configuration.Configuration.PORT)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=True)

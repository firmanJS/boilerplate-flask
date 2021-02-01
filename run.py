from config import configuration, http

app = http.createApp(configuration.Configuration)
PORT = int(configuration.Configuration.PORT)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True)

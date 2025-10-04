import axios from "axios";

const geocodeClient = axios.create({
    baseURL: "https://nominatim.openstreetmap.org/",
    headers: {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
})

geocodeClient.interceptors.request.use((config) => {
    if (!config.params) {
        config.params = {}
    }

    config.params.format = "jsonv2"
    return config
})

export {geocodeClient}
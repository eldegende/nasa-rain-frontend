import axios from "axios";
import {geocodeClient} from "./geocode.ts";

const geocodeSearch = (query: string) =>
    geocodeClient.get("search", {params: {q: query}})

export {
    geocodeSearch
}
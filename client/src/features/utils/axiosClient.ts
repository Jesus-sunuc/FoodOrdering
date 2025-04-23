import axios from "axios";

const baseURL = "https://lunchbox6.duckdns.org/api"
//import.meta.env.VITE_API_URL;

export const axiosClient = axios.create({
  baseURL,
});
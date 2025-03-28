import axios from "axios";

const baseURL =
  import.meta.env.MODE === "development"
    ? "http://localhost:8000/api"
    : "https://lunch-box-api-chdtdbcbg8bzbjfh.azurewebsites.net/api";

export const axiosClient = axios.create({
  baseURL,
});
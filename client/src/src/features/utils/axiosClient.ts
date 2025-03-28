import axios from "axios";

const baseURL =
  import.meta.env.MODE === "development"
    ? "http://localhost:8000"
    : "https://lunch-box-api-chdtdbcbg8bzbjfh.westus-01.azurewebsites.net/";

export const axiosClient = axios.create({
  baseURL,
});

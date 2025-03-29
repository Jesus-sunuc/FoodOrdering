import { Route, Routes } from "react-router-dom";
import App from "./src/App";

export const AppRoutes = () => (
  <Routes>
    <Route path="/" element={<App />} />
  </Routes>
);

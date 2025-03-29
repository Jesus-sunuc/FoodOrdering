import { Route, Routes } from "react-router-dom";
import { App } from "../src/src/App";

export const AppRoutes = () => (
  <Routes>
    <Route path="/" element={<App />} />
  </Routes>
);

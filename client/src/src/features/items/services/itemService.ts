// import { camel_to_snake } from "../../utils/apiMapper";
import { axiosClient } from "../../utils/axiosClient";
import { Item } from "../types/Item";

export const itemService = {
  async getItems(): Promise<Item[]> {
    const res = await axiosClient.get("/items");
    return res.data;
  },
  // async addItem(item: Item): Promise<Item> {
  //   const res = await axiosClient.post("/items", camel_to_snake(item));
  //   return res.data;
  // },
  // async updateItem(item: Item): Promise<Item> {
  //   const res = await axiosClient.put(`/items/${item.id}`, camel_to_snake(item));
  //   return res.data;
  // },
  // async deleteItem(id: string) {
  //   return axiosClient.delete(`/items/${id}`);
  // },
};

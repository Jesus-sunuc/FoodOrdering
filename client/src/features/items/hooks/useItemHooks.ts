import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { itemService } from "../services/itemService";

const itemKeys = {
  all: ["items"],
};

export const useGetItemsQuery = () =>
  useQuery({
    queryKey: itemKeys.all,
    queryFn: itemService.getItems,
  });

export const useAddItemMutation = () => {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: itemService.addItem,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: itemKeys.all });
    },
  });
};

export const useUpdateItemMutation = () => {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: itemService.updateItem,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: itemKeys.all });
    },
  });
};

export const useDeleteItemMutation = () => {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: itemService.deleteItem,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: itemKeys.all });
    },
  });
};
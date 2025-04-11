import { useState, useEffect } from "react";
import ItemCard from "./components/ItemCard";
import toast, { Toaster } from "react-hot-toast";
import { Button, Container } from "react-bootstrap";
import ItemModal from "./components/ItemModal";
import { Item } from "./features/items/types/Item";
import "./App.css";
import {
  useAddItemMutation,
  useDeleteItemMutation,
  useGetItemsQuery,
  useUpdateItemMutation,
} from "./features/items/hooks/useItemHooks";

export function App() {
  const [showModal, setShowModal] = useState(false);
  const [editingItem, setEditingItem] = useState<Item | undefined>(undefined);
  const [theme, setTheme] = useState<"light" | "dark">("light");

  const { data: items = [], isLoading } = useGetItemsQuery();
  const addItemMutation = useAddItemMutation();
  const updateItemMutation = useUpdateItemMutation();
  const deleteItemMutation = useDeleteItemMutation();

  const toggleTheme = () => {
    setTheme((prev) => (prev === "light" ? "dark" : "light"));
  };

  const handleAddNew = () => {
    setEditingItem(undefined);
    setShowModal(true);
  };

  const handleSave = (item: Item) => {
    const exists = items.find((i: Item) => i.id === item.id);

    if (exists) {
      updateItemMutation.mutate(item, {
        onSuccess: () => toast.success("Item updated!"),
        onError: () => toast.error("Failed to update item"),
      });
    } else {
      addItemMutation.mutate(item, {
        onSuccess: () => toast.success("Item added!"),
        onError: () => toast.error("Failed to add item"),
      });
    }
  };

  const handleDelete = (id: string) => {
    toast((t) => (
      <span>
        Are you sure?&nbsp;
        <Button
          variant="danger"
          size="sm"
          onClick={() => {
            deleteItemMutation.mutate(id, {
              onSuccess: () => toast.success("Item deleted"),
              onError: () => toast.error("Failed to delete"),
            });
            toast.dismiss(t.id);
          }}
        >
          Yes
        </Button>
        &nbsp;
        <Button
          variant="secondary"
          size="sm"
          onClick={() => toast.dismiss(t.id)}
        >
          No
        </Button>
      </span>
    ));
  };

  const handleEdit = (item: Item) => {
    setEditingItem(item);
    setShowModal(true);
  };

  const notAdmin = import.meta.env.VITE_ENV_NOT_ADMIN === "true";

  useEffect(() => {
    document.body.className =
      theme === "dark" ? "custom-dark" : "bg-light text-dark";
  }, [theme]);

  useEffect(() => {
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme === "light" || savedTheme === "dark") {
      setTheme(savedTheme);
    }
  }, []);

  useEffect(() => {
    localStorage.setItem("theme", theme);
    document.body.className =
      theme === "dark" ? "custom-dark" : "bg-light text-dark";
  }, [theme]);

  return (
    <Container className="py-4">
      <div className="d-flex justify-content-between align-items-center mb-3 mt-4">
        <Button hidden={notAdmin} variant="danger" onClick={handleAddNew}>
          Add New Item
        </Button>
        <Button
          variant={theme === "light" ? "dark" : "light"}
          onClick={toggleTheme}
        >
          <i
            className={`bi fs-5 me-2 ${
              theme === "light" ? "bi-moon-fill" : "bi-sun-fill"
            }`}
          ></i>
          {theme === "light" ? "Dark" : "Light"}
        </Button>
      </div>

      <Toaster />

      {isLoading ? (
        <div className="text-center">
          <div
            className="spinner-border text-success"
            style={{ width: "3rem", height: "3rem" }}
            role="status"
          ></div>
        </div>
      ) : (
        <div className="row">
          {Array.isArray(items) &&
            items.map((item: Item) => (
              <div
                key={item.id}
                className="col-12 col-sm-6 col-md-4 col-lg-3 d-flex"
              >
                <ItemCard
                  item={item}
                  onEdit={handleEdit}
                  onDelete={handleDelete}
                  theme={theme}
                />
              </div>
            ))}
        </div>
      )}

      <ItemModal
        show={showModal}
        onClose={() => setShowModal(false)}
        onSave={handleSave}
        initialData={editingItem}
        theme={theme}
      />
    </Container>
  );
}

export default App;

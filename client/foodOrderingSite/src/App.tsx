import { useState, useEffect } from "react";
import ItemCard from "./components/ItemCard";
import toast, { Toaster } from "react-hot-toast";
import { Item } from "./models/types";
import { Button, Container } from "react-bootstrap";
import ItemModal from "./components/ItemModal";

function App() {
  const [items, setItems] = useState<Item[]>([]);
  const [showModal, setShowModal] = useState(false);
  const [editingItem, setEditingItem] = useState<Item | undefined>(undefined);
  const [theme, setTheme] = useState<"light" | "dark">("light");

  const toggleTheme = () => {
    setTheme((prev) => (prev === "light" ? "dark" : "light"));
  };

  const handleAddNew = () => {
    setEditingItem(undefined);
    setShowModal(true);
  };

  const handleSave = (item: Item) => {
    setItems((prev) => {
      const exists = prev.find((i) => i.id === item.id);
      if (exists) {
        return prev.map((i) => (i.id === item.id ? item : i));
      }
      return [...prev, item];
    });
  };

  const handleDelete = (id: string) => {
    toast((t) => (
      <span>
        Are you sure?&nbsp;
        <Button
          variant="danger"
          size="sm"
          onClick={() => {
            setItems((prev) => prev.filter((item) => item.id !== id));
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

  useEffect(() => {
    document.body.className =
      theme === "dark" ? "bg-dark text-light" : "bg-light text-dark";
  }, [theme]);

  useEffect(() => {
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme === "light" || savedTheme === "dark") {
      setTheme(savedTheme);
    }
  }, []);
  
  useEffect(() => {
    localStorage.setItem("theme", theme);
    document.body.className = theme === "dark" ? "bg-dark text-light" : "bg-light text-dark";
  }, [theme]);
  

  return (
    <Container className="py-4">
      <div className="d-flex justify-content-between align-items-center mb-3">
        <h1>Add New Product</h1>
        <Button
          variant={theme === "light" ? "dark" : "light"}
          onClick={toggleTheme}
        >
          Switch to {theme === "light" ? "Dark" : "Light"} Mode
        </Button>
      </div>

      <Toaster />
      <Button variant="success" className="mb-4" onClick={handleAddNew}>
        Add New Item
      </Button>

      <div className="row">
        {items.map((item) => (
          <div
            key={item.id}
            className="col-12 col-sm-6 col-md-4 col-lg-3 d-flex"
          >
            <ItemCard item={item} onEdit={handleEdit} onDelete={handleDelete} theme={theme}/>
          </div>
        ))}
      </div>

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

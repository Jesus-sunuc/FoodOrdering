import { useState } from "react";
import "./App.css";
import ItemCard from "./components/ItemCard";
import toast, { Toaster } from "react-hot-toast";
import { Item } from "./models/types";
import { Button, Container } from "react-bootstrap";
import ItemModal from "./components/ItemModal";

function App() {
  const [items, setItems] = useState<Item[]>([]);
  const [showModal, setShowModal] = useState(false);
  const [editingItem, setEditingItem] = useState<Item | undefined>(undefined);

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

  return (
    <Container className="py-4">
      <Toaster />
      <h1 className="mb-4">Healthy Food Items</h1>
      <Button variant="success" className="mb-4" onClick={handleAddNew}>
        Add New Item
      </Button>

      <div className="row">
        {items.map((item) => (
          <div
            key={item.id}
            className="col-12 col-sm-6 col-md-4 col-lg-3 d-flex"
          >
            <ItemCard item={item} onEdit={handleEdit} onDelete={handleDelete} />
          </div>
        ))}
      </div>

      <ItemModal
        show={showModal}
        onClose={() => setShowModal(false)}
        onSave={handleSave}
        initialData={editingItem}
      />
    </Container>
  );
}

export default App;

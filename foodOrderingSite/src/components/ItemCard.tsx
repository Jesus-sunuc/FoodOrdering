import React from "react";
import { Item } from "../models/types";
import { Button, Card } from "react-bootstrap";

interface ItemCardProps {
  item: Item;
  onEdit: (item: Item) => void;
  onDelete: (id: string) => void;
}

const ItemCard: React.FC<ItemCardProps> = ({ item, onEdit, onDelete }) => {
  return (
    <Card className="mb-3">
      <Card.Img variant="top" src={item.image} style={{ height: "200px", objectFit: "cover" }} />
      <Card.Body>
        <Card.Title>{item.title}</Card.Title>
        <Card.Text>{item.description}</Card.Text>
        <Button variant="warning" className="me-2" onClick={() => onEdit(item)}>Edit</Button>
        <Button variant="danger" onClick={() => onDelete(item.id)}>Delete</Button>
      </Card.Body>
    </Card>
  );
};

export default ItemCard;

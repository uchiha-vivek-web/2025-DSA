from dataclasses import dataclass

@dataclass
class InventoryItem:
    name:str
    unit_price:float
    quantity_on_hand:int=0

    def total_cost(self) -> float:
        return self.unit_price + self.quantity_on_hand
    

if __name__=="__main__":
    item= InventoryItem(name='widget',unit_price=10.0,quantity_on_hand=2)
    print(f"Total cost for {item.name}: $ {item.total_cost()}")
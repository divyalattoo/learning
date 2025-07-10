class GateRepo:
    def __init__(self):
        self.gate_map = {}
        self.count = 0

    def find_gate_byid(self, gate_id):
        if gate_id in self.gate_map:
            raise ValueError(f"Gate with id {gate_id} already exists.")
        return self.gate_map.get(gate_id, None)

    def add_gate(self, gate):
        if gate.id in self.gate_map:
            raise ValueError(f"Gate with id {gate.id} already exists.")
        id_generated = self.count+1
        gate.id = id_generated
        gate.gate_number = id_generated
        self.count += 1
        self.gate_map[gate.id] = gate
        return gate

    def update_gate(self, gate):
        if gate.id not in self.gate_map:
            raise ValueError(f"Gate with id {gate.id} does not exist.")
        self.gate_map[gate.id] = gate

    def delete_gate(self, gate_id):
        if gate_id not in self.gate_map:
            raise ValueError(f"Gate with id {gate_id} does not exist.")
        del self.gate_map[gate_id]


    # def get_gate(self, gate_id):
    #     cursor = self.db.cursor()
    #     cursor.execute("SELECT * FROM gates WHERE id = ?", (gate_id,))
    #     gate = cursor.fetchone()
    #     cursor.close()
    #     return gate
    #
    # def add_gate(self, gate_data):
    #     cursor = self.db.cursor()
    #     cursor.execute("INSERT INTO gates (name, status) VALUES (?, ?)", (gate_data['name'], gate_data['status']))
    #     self.db.commit()
    #     cursor.close()
    #
    # def update_gate(self, gate_id, gate_data):
    #     cursor = self.db.cursor()
    #     cursor.execute("UPDATE gates SET name = ?, status = ? WHERE id = ?", (gate_data['name'], gate_data['status'], gate_id))
    #     self.db.commit()
    #     cursor.close()
    #
    # def delete_gate(self, gate_id):
    #     cursor = self.db.cursor()
    #     cursor.execute("DELETE FROM gates WHERE id = ?", (gate_id,))
    #     self.db.commit()
    #     cursor.close()
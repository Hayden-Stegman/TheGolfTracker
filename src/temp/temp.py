class InMemoryDatabase:
    def __init__(self):
        self.data = {}

    def create(self, key, value):
        if key in self.data:
            raise ValueError(f"Key '{key}' already exists.")
        self.data[key] = value

    def read(self, key):
        return self.data.get(key, None)

    def update(self, key, value):
        if key not in self.data:
            raise ValueError(f"Key '{key}' does not exist.")
        self.data[key] = value

    def delete(self, key):
        if key not in self.data:
            raise ValueError(f"Key '{key}' does not exist.")
        del self.data[key]

    def show_all(self):
        return self.data

# Load config.toml
config = toml.load('config.toml')

# Flatten the nested TOML structure
def flatten_config(config, parent_key='', sep='.'):
    items = {}
    for k, v in config.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_config(v, new_key, sep=sep))
        else:
            items[new_key] = v
    return items

flat_config = flatten_config(config)

# Initialize DB and populate from config
db = InMemoryDatabase()
for key, value in flat_config.items():
    db.create(key, value)

# Demonstrate CRUD
print("Initial DB State:")
print(db.show_all())

# Update an entry
db.update('holder.nominal_synqor_power', 55)
print("\nAfter Update:")
print(db.show_all())

# Read a single entry
print("\nRead 'holder.nominal_synqor_power':")
print(db.read('holder.nominal_synqor_power'))

# Delete an entry
db.delete('holder.trans_config.update_time_ms')
print("\nAfter Deletion:")
print(db.show_all())
Output:
bash
Copy
Edit
Initial DB State:
{'holder.trans_config.update_time_ms': 1000, 'holder.trans_config.timeout_time_ms': 5000, 'holder.nominal_synqor_power': 42}

After Update:
{'holder.trans_config.update_time_ms': 1000, 'holder.trans_config.timeout_time_ms': 5000, 'holder.nominal_synqor_power': 55}

Read 'holder.nominal_synqor_power':
55

After Deletion:
{'holder.trans_config.timeout_time_ms': 5000, 'holder.nominal_synqor_power': 55}
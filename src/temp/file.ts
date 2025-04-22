class MemortyStorage {
    // Using a Map to store key-value pairs in memory
    private map: Map<string, any>;

    constructor() {
        this.map = new Map<string, any>();
    }

    create(key: string, value: string): void {
        if (this.map.has(key)) {
            throw new Error("Key already exists");
        }
        this.map.set(key, value);
    }

    update(key: string, value: string): void {
        if (!this.map.has(key)) {
            throw new Error("Key does not exist");
        }
        this.map.set(key, value);
    }

    read(key: string): any {
        if (this.map.has(key)) {
            return this.map.get(key);
        }
        return null; // Return null if the key does not exist
    }

    delete(key: string): void {
        if (!this.map.has(key)) {
            throw new Error("Key does not exist");
        }
        this.map.delete(key);
    }
}

export default MemortyStorage;

const config = {
    database: {
        server: "192.168.1.1",
        port: 5432,
        enabled: true,
    },
    owner: {
        name: "John Doe",
        dob: "1980-01-01",
    },
    features: {
        logging: true,
        max_connections: 100,
        sub_feature: {
            enabled: false,
            timeout: 30,
        },
    },
};

function flatten_config(config: any, parent_key='', separator='.') {
    let items = new Map<string, any>();

    for (let key in config) {
        let subcon = config[key];
        let new_key = parent_key ? parent_key + separator + key : key;
        if (typeof subcon === 'object' && !Array.isArray(subcon)) {
            const nestedItems = flatten_config(subcon, new_key, separator);
            nestedItems.forEach((value, nestedKey) => {
                items.set(nestedKey, value);
            });
        } else {
            items.set(new_key, subcon);
        }
    }
    return items;
}

console.log(flatten_config(config));
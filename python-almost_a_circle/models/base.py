#!/usr/bin/python3
"""Base class for managing ID attribute across all shapes."""
import json
import csv


class Base:
    """Base class with ID management and serialization utilities."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance.

        Args:
            id (int, optional): If provided, assign to id. Otherwise,
                auto-increment __nb_objects and use that.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dicts."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        dict_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of dictionaries from a JSON string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes set from a dictionary."""
        # Create a dummy instance with mandatory attributes
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)      # width, height
        elif cls.__name__ == "Square":
            dummy = cls(1)          # size
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from a JSON file."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, encoding="utf-8") as f:
                json_str = f.read()
        except FileNotFoundError:
            return []
        dict_list = cls.from_json_string(json_str)
        return [cls.create(**d) for d in dict_list]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize list_objs to a CSV file."""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.width, obj.height,
                                     obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize instances from a CSV file."""
        filename = cls.__name__ + ".csv"
        instances = []
        try:
            with open(filename, newline="") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        d = {"id": int(row[0]), "width": int(row[1]),
                             "height": int(row[2]), "x": int(row[3]),
                             "y": int(row[4])}
                    elif cls.__name__ == "Square":
                        d = {"id": int(row[0]), "size": int(row[1]),
                             "x": int(row[2]), "y": int(row[3])}
                    instances.append(cls.create(**d))
        except FileNotFoundError:
            pass
        return instances

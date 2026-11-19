"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

This program demonstrates how Python dictionaries function
as hash tables by showing insert, lookup, update, delete,
and edge-case operations.
"""


def main():

    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # CREATE A HASH TABLE
    # ===============================

    print("\n=== INSERT OPERATIONS ===")

    # Python dictionaries function as hash tables.
    # Each key is processed using a hash function.
    # The resulting hash helps Python quickly locate
    # the associated value.

    inventory = {}

    inventory["L100"] = "Laptop"
    inventory["P200"] = "Printer"
    inventory["M300"] = "Monitor"
    inventory["K400"] = "Keyboard"
    inventory["T500"] = "Tablet"

    print("\nInventory:")
    print(inventory)

    # ===============================
    # LOOKUP OPERATIONS
    # ===============================

    print("\n=== LOOKUP OPERATIONS ===")

    # Dictionary lookups use the key's hash value
    # to retrieve data efficiently.

    print("\nL100:", inventory["L100"])
    print("P200:", inventory["P200"])

    # ===============================
    # UPDATE OPERATIONS
    # ===============================

    print("\n=== UPDATE OPERATIONS ===")

    print("\nBefore update:")
    print(inventory)

    # Assigning a new value to an existing key
    # replaces the previous value.

    inventory["L100"] = "Gaming Laptop"

    print("\nAfter update:")
    print(inventory)

    # ===============================
    # DELETE OPERATIONS
    # ===============================

    print("\n=== DELETE OPERATIONS ===")

    print("\nBefore delete:")
    print(inventory)

    # Deleting a key removes the key-value pair
    # from the dictionary.

    del inventory["K400"]

    print("\nAfter delete:")
    print(inventory)

    # ===============================
    # EDGE CASES
    # ===============================

    print("\n=== EDGE CASES ===")

    # Edge Case 1:
    # Lookup of a missing key using get()
    # prevents a KeyError.

    print("\nMissing key lookup:")
    print(inventory.get("X999", "Equipment not found"))

    # Edge Case 2:
    # Safe deletion of a missing key using pop()
    # with a default value.

    removed = inventory.pop("X999", None)

    if removed is None:
        print("\nAttempted delete of missing key handled safely.")

    # Edge Case 3:
    # Demonstrate an empty dictionary.

    empty_inventory = {}

    print("\nEmpty dictionary:")
    print(empty_inventory)


if __name__ == "__main__":
    main()
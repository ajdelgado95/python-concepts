| Feature              | **List**                          | **Tuple**                         | **Set**                          | **Dictionary**                  |
|----------------------|------------------------------------|------------------------------------|-----------------------------------|----------------------------------|
| **Definition**       | Ordered, mutable collection of items. | Ordered, immutable collection of items. | Unordered, mutable collection of unique items. | Unordered, mutable collection of key-value pairs. |
| **Syntax**           | `[1, 2, 3]`                       | `(1, 2, 3)`                       | `{1, 2, 3}`                      | `{'a': 1, 'b': 2}`              |
| **Order**            | Maintains insertion order (since Python 3.7). | Maintains insertion order (since Python 3.7). | Unordered.                      | Maintains insertion order (since Python 3.7). |
| **Mutability**       | Mutable (items can be added, removed, or modified). | Immutable (items cannot be changed). | Mutable (items can be added/removed). | Keys and values are mutable, but keys must be immutable. |
| **Duplicates**       | Allows duplicates.                | Allows duplicates.                | Does not allow duplicates.       | Keys must be unique; values can be duplicated. |
| **Access**           | Indexed (e.g., `list[0]`).        | Indexed (e.g., `tuple[0]`).       | Not indexed (use loops or check membership). | Accessed via keys (e.g., `dict['key']`). |
| **Use Cases**        | Dynamic collection of items where changes are required. | Fixed collection of items.        | Ensuring unique elements in a collection. | Mapping keys to values for fast lookups. |
| **Performance**      | Slower for lookups (O(n) for `in`). | Similar to lists for access.      | Faster lookups (O(1) for `in`).  | Faster lookups for keys (O(1) for `in`). |
| **Common Methods**   | `append()`, `extend()`, `pop()`, `sort()`. | `count()`, `index()`.             | `add()`, `remove()`, `union()`, `intersection()`. | `keys()`, `values()`, `items()`, `get()`. |
| **Examples**         | `[1, 2, 3, 4]`                    | `(1, 2, 3, 4)`                    | `{1, 2, 3, 4}`                   | `{'a': 1, 'b': 2, 'c': 3}`      |

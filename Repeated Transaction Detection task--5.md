## Problem Statement
Write a Python program that checks a list of amounts for duplicates. When an amount has appeared earlier in the list, print "Duplicate:" followed by that amount.

## Algorithm
1. Set amounts to [100, 250, 100].
2. Create an empty list called seen.
3. For each amount in amounts:
   - If the amount is already in seen, print it as a duplicate.
   - Otherwise, add it to seen.

## Flowchart
```mermaid
flowchart TD
    A([Start]) --> B[Set amounts = 100, 250, 100]
    B --> C[Create empty seen list]
    C --> D[Get next amount]
    D --> E{Are there more amounts?}
    E -- No --> J([End])
    E -- Yes --> F{Is amount in seen?}
    F -- Yes --> G[Print Duplicate and amount]
    F -- No --> H[Add amount to seen]
    G --> D
    H --> D
```
## Pseudocode
START
    amounts ← [100, 250, 100]
    seen ← empty list

    FOR EACH amount IN amounts DO
        IF amount is in seen THEN
            DISPLAY "Duplicate:", amount
        ELSE
            ADD amount TO seen
        END IF
    END FOR
END

## Sample Input
The values are set in the program:
Amounts: 100, 250, 100
Sample Output
Duplicate: 100
